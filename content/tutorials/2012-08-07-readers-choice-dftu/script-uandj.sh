#!/bin/sh
## Replace the following with variables specific to your environment.
EXEC='mpirun pw.x'
PSEUDODIR='~/pseudos'
SCRATCHDIR='/scratch'
for J in 1E-40 0.5 1.0 1.5 2.0; do
    for U in 1E-40 1.0 2.0 3.0 4.0; do 
        for mag in 5 7; do
            if [ "$mag" == "5" ]; then
            zcoord="1.592"
            magnew="4.0"
            else
            zcoord="1.714"
            magnew="6.0"
            fi
            mol='MnH'
            cat > $mol.m$mag.U$U.J$J.in << EOF    
            &control
            calculation='scf'
            restart_mode='from_scratch',
            prefix='$mol.U$U.J$J',
            pseudo_dir = '$PSEUDODIR',
            outdir='$SCRATCHDIR',
            wf_collect=.true.
            /
            &system
            ibrav=1, celldm(1) =20.0
            nat=2, ntyp=2,occupations='fixed',
            ecutwfc =25,ecutrho =250
            tot_charge=0.0,tot_magnetization=$magnew
            nspin=2, starting_magnetization(1)=0.75,
            starting_magnetization(2)=0.05,
            lda_plus_u = .TRUE., lda_plus_u_kind=1,
            Hubbard_U(1)=$U , Hubbard_J(1,1)=$J
            /
            &electrons
            conv_thr = 1.0d-6
            mixing_beta = 0.4
            electron_maxstep=10000,
            /
            ATOMIC_SPECIES
            Mn 54.9 Mn.pbe-sp-van.UPF
            H  1.01 HUSPBE.RRKJ3
            ATOMIC_POSITIONS (angstroms)
            Mn 0.000  0.000 0.000
            H  0.000  0.000 $zcoord
            K_POINTS gamma

EOF
            filetest=`grep '! ' $mol.m$mag.U$U.J$J.out -l | wc -l | awk '{ print $1 }'`
            if [ "$filetest" != "1" ]; then
            printf "Working on U="$U" and J="$J"..."
            $EXEC < $mol.m$mag.U$U.J$J.in > $mol.m$mag.U$U.J$J.out 
            echo " done"
            fi
        done
    done    
done
