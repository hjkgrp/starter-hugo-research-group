import re
import os
import time
import math
import glob
from libraries import *
from variables import *
from atreader import *
nat,ntyp=len(geom)-2,len(species)
nel-=charge
nelup,neldw=(nel+spin)/2,(nel-spin)/2
cell=runs[job][1]
for hubby in hubbylist:
  rpt=-1
  for hubtyp in typno:
    rpt+=1
    for alpha in alphalist:
       pre=molname+'.s'+str(spin+1)+'.n'+species[hubtyp-1]+'.u'+str(hubby)
       title=molname+', multiplicity='+str(spin+1)+', U='+str(hubby)+' on '+species[hubtyp-1]
       file=pre+'.a'+str(alpha)
       filein,fileout=file+'.in',file+'.out'
       if ( alpha=='1D-40'):
         post=''
       else:
         post='a'+alpha
       input = open(filein, 'w')

       input.write('&CONTROL\n')
       input.write('title = "%s"\n' %(title))
       input.write('calculation = "%s",\n' %(runs[job][0]))
       input.write('restart_mode = "from_scratch",\n')
       input.write('prefix = "%s",\n' %(pre))
       input.write('outdir = "%s/%s",\n' %(scratchdir,post))
       input.write('pseudo_dir = "%s",\n' %(pseudodir))
       input.write('wf_collect=.TRUE.\n')
       input.write('/\n')

       input.write('&SYSTEM\n')
       input.write('ibrav=1,celldm(1)=%f,ecutwfc=%i, ecutrho=%i,\n' %(cell,ecutwfc,ecutrho))
       for at in range(0,ntyp):
            input.write('starting_magnetization(%i)=0.25,' %(at+1))
       input.write('\n nspin=2,occupations="fixed",\n')
       input.write('nat=%i,ntyp=%i,tot_charge=%f,tot_magnetization=%f\n' % (nat,ntyp,charge,spin))
       # if running PW 4.1.2 or earlier comment above line and uncomment line below.
       #input.write('nat=%i,ntyp=%i,nelec=%f,nelup=%f,neldw=%f\n' %(nat,ntyp,nel,nelup,neldw))
       input.write('lda_plus_U=.true.,U_projection_type="norm-atomic"\n')
       # put a loop in here over all possible hubbard types 
       # something like including every hubbard type with an alpha and a U set to zero but if the hubtyp is set in the current loop then alpha = current alpha.
       for hubnum in typno: 
         if (hubtyp == hubnum):
           input.write('Hubbard_U(%i)=%s,Hubbard_alpha(%i)=%s\n' %(hubnum,hubby,hubnum,alpha))
         else:
           input.write('Hubbard_U(%i)=%s,Hubbard_alpha(%i)=%s\n' %(hubnum,'1D-40',hubnum,'1D-40'))
       input.write('/\n')

       input.write('&ELECTRONS\n')
       if ( alpha != '1D-40' ):
         input.write('startingwfc="file", startingpot="file"\n')
         conv2=conv.split('-')[0]+'-'+str(int(conv.split('-')[1])+2)
         diago=conv.split('-')[0]+'-'+str(int(conv.split('-')[1])+4)
       else:
         if ( rpt > 0 ):
            input.write('startingwfc="file", startingpot="file"\n')
         conv2=conv
         diago='1D-2'
       input.write('mixing_beta=%s,conv_thr=%s,diago_thr_init=%s,electron_maxstep=%i\n/\n' %(beta,conv2,diago,estep))

       input.write('ATOMIC_SPECIES\n')
       for at in range(0,ntyp):
         input.write(species[at]+' '+pseudos[re.sub('[0-9]','', species[at])][1]+' '+pseudos[re.sub('[0-9]','',species[at])][0]+'\n')

       input.write('ATOMIC_POSITIONS (angstrom)\n')
       for at in range(2,nat+2):
         input.write(geom[at])

       input.write('K_POINTS (automatic)\n 1 1 1 0 0 0\n')
       input.close()

       if ( alpha != '1D-40' ):
         os.system('mkdir %s/%s\n' %(scratchdir,post))
         os.system('cp -pr %s/%s* %s/%s\n' %(savedir,pre,scratchdir,post)) 
       if ( alpha == '1D-40' ):
         if ( rpt > 0 ):
            for files in glob.glob('wfns/*'+species[hubtyp-2]+'*'):
               os.system('cp -pr %s %s\n' %(files,re.sub(species[hubtyp-2],species[hubtyp-1], files)))
       if ( para != '' ):
         parafront=para
       else:
         parafront=''
       print('%s %s/%s < %s.in > %s.out \n' %(parafront,bindir,execname,file,file))
       if ( alpha == '1D-40' ):
         if ( rpt == 0 ):
           os.system('%s %s/%s < %s.in > %s.out \n' %(parafront,bindir,execname,file,file))
       else:
         os.system('%s %s/%s < %s.in > %s.out \n' %(parafront,bindir,execname,file,file))
       if ( alpha == '1D-40' ):
         os.system('cp -pr %s/%s* %s/\n' %(scratchdir,pre,savedir))
       if ( alpha != '1D-40' ):
         os.system('rm -rf %s/%s/ \n' %(scratchdir,post))
print "All done\n"
