import re
import os
import time
import math
import glob
from libraries import *
from variables import *
molname='Fe-bcc'
nat=open(molname+'.xyz','r').readline()
geom=open(molname+'.xyz','r').readlines()
ats,species,typnum,typno,nel=[],[],[],[],0
for n in range(2,len(geom)):
       ats.append(geom[n].split()[0])
       if (len(geom[n].split()) == 5):
          typnum.append(geom[n].split()[0])
       geom[n]=geom[n].split()[0]+' '+geom[n].split()[1]+' '+geom[n].split()[2]+' '+geom[n].split()[3]+'\n'
numlist=range(0,10)
numlist.insert(0,'')
for specs in pseudos.keys():
     for num in numlist:
       nel+=ats.count(specs+str(num))*pseudos[specs][2]
       if ats.count(specs+str(num)):
            species.append(specs+str(num))
typno=[1]
nat,ntyp=len(geom)-2,len(species)
nel-=charge
cell=runs[job][1]
for hubby in hubbylist:
  for hubtyp in typno:
    for alpha in alphalist:
       pre=molname+'.n'+species[hubtyp-1]+'.u'+str(hubby)
       title=molname+', U='+str(hubby)+' on '+species[hubtyp-1]
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
       input.write('ibrav=3,celldm(1)=%f,ecutwfc=%i, ecutrho=%i,\n' %(cell,ecutwfc,ecutrho))
       for at in range(0,ntyp):
            input.write('starting_magnetization(%i)=0.05,\n' %(at+1))
       input.write('\nnspin=2,occupations="smearing",\n')
       input.write('nat=%i,ntyp=%i,\n smearing="methfessel-paxton",degauss=0.005\n' % (nat,ntyp))
       input.write('lda_plus_U=.true.\n')
       for hubnum in range(1,len(species)+1): 
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
         conv2=conv
         diago='1D-2'
       input.write('mixing_beta=%s,conv_thr=%s,diago_thr_init=%s,electron_maxstep=%i\n/\n' %(beta,conv2,diago,estep))

       input.write('ATOMIC_SPECIES\n')
       for at in range(0,ntyp):
         input.write(species[at]+' '+pseudos[re.sub('[0-9]','', species[at])][1]+' '+pseudos[re.sub('[0-9]','',species[at])][0]+'\n')

       input.write('ATOMIC_POSITIONS (crystal)\n')
       for at in range(2,nat+2):
         input.write(geom[at])

       input.write('K_POINTS (automatic)\n 4 4 4 0 0 0\n')
       input.close()

       if ( alpha != '1D-40' ):
         os.system('mkdir %s/%s\n' %(scratchdir,post))
         os.system('cp -pr %s/%s* %s/%s\n' %(savedir,pre,scratchdir,post))
       if ( para != '' ):
         parafront=para+' -np '+str(cpu)
       else:
         parafront=''
       if ( npool != '' ):
         pool='-npool '+str(npool)
       os.system('%s %s/%s %s < %s.in > %s.out \n' %(parafront,bindir,execname,pool,file,file))
       if ( alpha == '1D-40' ):
         os.system('cp -pr %s/%s* %s/\n' %(scratchdir,pre,savedir))
       if ( alpha != '1D-40' ):
         os.system('rm -rf %s/%s/ \n' %(scratchdir,post))
print "All done\n"
