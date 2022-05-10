#Select input file that was used to run pw.x calculation as basis for setting variables.  Associated output file should also be present.  If unavailable, set variables below.

pwin='MnO.c0.s6.u1D-40.a1D-40.in'

# Select plot type
#plot='density','spin-polarization','psi2'  
# refers to total density (0), spin polarization (6), or molecular orbitals (7)
plot='psi2'

# Choose whether or not you want to generate gaussian cube file format:
xsf2cub='yes'
# Spin settings: this is determined first and foremost by input file, but you can also specify here.  Applies most to density or molecular orbitals.
spin='all'
#choices: 'all','up','down'.

#Cluster-specific parameters
nodes=1
cpu=2
para='mpirun'
bindir='~/espresso-4.3/bin/'
execname='pp.x'


# Or (the hard way) set the following variables manually
#prefix=''
#outdir=''

#Script supports ibrav = 0 or 1, also 2-4, 6-11 though possibly with bugs.
#ibrav=1
# cell parameters in bohrs or ratios of bohrs, same as in input format.
# for celldm2 and celldm3, if not set leave = 1. 
#celldm1=
#celldm2=1
#celldm3=1

#Set the bands to calculate for a molecular orbital plot by one of three ways:
# If you want this to be determined from in/out, leave the line below uncommented:
#nbandmin,nbandmax=0,0
# Set the first band to calculate
#nbandmin=12
# Set the maximum band to calculate
#nbandmax=13
# Alternatively, list the bands you wish to calculate:  
#bandlist=[1,2,3,7,10]
#If you use this last option, be sure to set nbandmin and nbandmax = 0.

# Set multiplier for molecule size that determines the box size. If the defaults are too small or too big. Make > 1 if too small, < 1 if too big.
mult=1.0
