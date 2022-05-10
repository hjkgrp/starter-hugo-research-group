from libraries import *
from variables import *
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
       if typnum.count(specs+str(num)):
          typno.append(len(species))
