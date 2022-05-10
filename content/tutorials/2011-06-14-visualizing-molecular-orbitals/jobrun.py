import os
from sys import exit
from libraries import *
from variables import *
import os
if pwin != '': 
  print "Collected variables from your example input file: "+pwin
  if os.path.exists(pwin) == 1:
    from pwreader import *
#Check variables
# Lattice
if int(ibrav)>11:
  print "This utility will not work for the lattice you have chosen: "+str(ibrav)
  exit()
elif int(ibrav)==5:
  print "This utility will not work for the lattice you have chosen: "+str(ibrav)
  exit()
elif int(ibrav) > 1:
  print "Warning: this utility may not work right for the lattice you have chosen."
celldmx,celldmy,celldmz=float(celldm1),celldm2*float(celldm1),celldm3*float(celldm1)

# Plot details
plotnum=plottyp[plot][0]

# Spin details
if spin == 'all':
  if plotnum==7:
     kptlist=[1,2]
  else:
     spinno=0
#Calculating center of mass
structure=open(prefix+'.xyz','r').readlines()
if len(structure[0].split()) < 2: 
 if int(structure[0])==len(structure)-2:
  start=2
else:
  start=0
xnum,xden,ynum,yden,znum,zden=0.0,0.0,0.0,0.0,0.0,0.0
xmin,xt,xmax,ymin,yt,ymax,zmin,zt,zmax=0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
for lines in range(start,len(structure)):
  mass=elements[structure[lines].split()[0]][0]
  xnum+=float(structure[lines].split()[1])*mass
  ynum+=float(structure[lines].split()[2])*mass
  znum+=float(structure[lines].split()[3])*mass
  xden+=mass
  yden+=mass
  zden+=mass
  xt,yt,zt=structure[lines].split()[1:4]
  delta=elements[structure[lines].split()[0]][1]
  if float(xt)+float(delta)/(50.0/mult) >= xmax: 
     xmax=float(xt)+float(delta)/(50.0/mult)
  if float(xt)-float(delta)/(50.0/mult) <= xmin:
     xmin=float(xt)-float(delta)/(50.0/mult)
  if float(yt)+float(delta)/(50.0/mult) >= ymax: 
     ymax=float(yt)+float(delta)/(50.0/mult)
  if float(yt)-float(delta)/(50.0/mult) <= ymin:
     ymin=float(yt)-float(delta)/(50.0/mult)
  if float(zt)+float(delta)/(50.0/mult) >= zmax: 
     zmax=float(zt)+float(delta)/(50.0/mult)
  if float(zt)-float(delta)/(50.0/mult) <= zmin:
     zmin=float(zt)-float(delta)/(50.0/mult)
comx,comy,comz=xnum/xden,ynum/yden,znum/zden
e1x,e1y,e1z=(xmax-xmin)/(celldmx*.529177),0.0000,0.0000
e2x,e2y,e2z=0.0000,(ymax-ymin)/(celldmz*.529177),0.0000
e3x,e3y,e3z=0.0000,0.0000,(zmax-zmin)/(celldmz*.529177)
ox,oy,oz=xmin/(celldmx*.529177),ymin/(celldmy*.529177),zmin/(celldmz*.529177)
if plotnum != 7:
   bandlist=[1]
else:
   if int(nbandmin)+int(nbandmax) > 0.5:
     bandlist=range(int(nbandmin),int(nbandmax)+1)
if spin != 'all':
   kptlist=[spinno]
if plotnum != 7:
   bandlist=[1]
for kpt in kptlist:
  for band in bandlist:
    ppin=open(prefix,'w')
    pppre=prefix+'.k'+str(kpt)+'.b'+str(band)
    ppin=open(pppre+'.in','w')
    ppsuff='ppout'
    ppin.write('&INPUTPP\n')
    ppin.write('prefix="%s",outdir="%s",filplot="%s"\n' %(prefix,outdir,pppre))
    ppin.write('plot_num=%i\n' %(plotnum))
    if plotnum == 7: 
      ppin.write('kpoint=%i,kband=%i,lsign=.%s.\n/\n' %(kpt,band,plottyp[plot][6]))
    elif plotnum == 6: 
      ppin.write('/\n')
    elif plotnum == 0:
      ppin.write('spin_component=%i/\n' %(spinno))
    else:
      print "Warning! Unrecognized plotnum !"
    ppin.write('&PLOT\n iflag=3\n output_format=3\n')
    ppin.write('fileout="%s"\n' %(pppre+'.'+ppsuff))
    ppin.write('e1(1)=%f,e1(2)=%f,e1(3)=%f\n' %(e1x,e1y,e1z))
    ppin.write('e2(1)=%f,e2(2)=%f,e2(3)=%f\n' %(e2x,e2y,e2z))
    ppin.write('e3(1)=%f,e3(2)=%f,e3(3)=%f\n' %(e3x,e3y,e3z))
    ppin.write('x0(1)=%f,x0(2)=%f,x0(3)=%f\n/\n' %(ox,oy,oz))
    ppin.close()
    print "Running pp.x for kpt:"+str(kpt)+" band:"+str(band)+"..."
    os.system('%s/%s < %s.in > %s.out \n' %(bindir,execname,pppre,pppre))
    print "done."
    extradir="pp-extras"
    if os.path.exists(extradir) != 1:
      os.system('mkdir %s\n' %(extradir))
    if xsf2cub == 'yes':
      os.system('python xsf2cub %s\n' %(pppre+'.'+ppsuff))
      os.system('mv -f %s %s\n' %(pppre+'.'+ppsuff,extradir))
    os.system('mv -f %s %s\n' %(pppre,extradir))
    # If space is scarce... do one of the two instead
    #os.system('rm -f %s\n' %(pppre))
    #os.system('gzip $s/%s*\n' %(extradir,pppre))
