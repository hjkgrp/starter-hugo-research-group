import re
from libraries import *
from variables import *

pwout=pwin.strip(".in")+'.out'
n=0
input=open(pwin,'r').readlines()
m=0
for lines in range(0,len(input)):
  currline=re.split('[( ,=)]', input[lines])
  for words in range(0,len(currline)):
     if currline[words]=='prefix':
         prefix=currline[words+2].strip(",")+currline[words+3].strip("\"")
         xyz=open(prefix+'.xyz','w')
     if currline[words]=='outdir':
         outdir=currline[words+2].strip(",")+currline[words+3].strip("\"")
     if currline[words]=='ibrav':
         ibrav=currline[words+1].strip(" ")
     if currline[words]=='celldm':
         if currline[words+1] == '1':
           celldm1=currline[words+2].strip(",")+currline[words+3].strip(",")
           m+=1
         if currline[words+1] == '2':
           celldm2=currline[words+2].strip(",")+currline[words+3].strip(",")
           m+=1
         if currline[words+1] == '3':
           celldm3=currline[words+2].strip(",")+currline[words+3].strip(",")
           m+=1
     if currline[words]=='occupations':
         occtyp=currline[words+1].strip("\"")
     if currline[words]=='nspin':
         nspin=currline[words+1]
     if currline[words]=='ATOMIC_POSITIONS':
         type=currline[words+1].strip(",")+currline[words+2].strip(",")
         n=1
  if n==1:
    if currline[0] != 'K_POINTS':
     if currline[0] != 'ATOMIC_POSITIONS':
       xyz.write(input[lines])
    else:
       n=0
       xyz.close()
input2=open(pwout,'r').readlines()
for lines in range(0,len(input2)):
  currline=re.split('[=]', input2[lines])
  for words in range(0,len(currline)):
     if currline[words]=='     number of Kohn-Sham states': 
      if nbandmax == 0: 
        nbandmax=currline[words+1].strip("\n").strip(" ")
      if nbandmin == 0:
        nbandmin=1
if m==1:
  celldm2=ibravset[str(ibrav)][1]
  celldm3=ibravset[str(ibrav)][2]
if m==2:
  celldm2=ibravset[str(ibrav)][1]
