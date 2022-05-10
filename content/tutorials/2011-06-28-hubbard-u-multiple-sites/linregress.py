### Imports run data from other routines
from math import sqrt
from variables import alphalist,hubbylist,molname,charge,spin,vis 
from atreader import *
import re
### Checks for scipy and matplotlib
try:
  from scipy import linalg
  scipy_loaded = True
except ImportError:
  scipy_loaded = False
try:
  import numpy as np
  import matplotlib.pyplot as plt
  import matplotlib.colors as colors
  import matplotlib.colorbar as colorbar
  import matplotlib.cm as cm
  matplotlib_loaded = True
except ImportError:
  matplotlib_loaded = False
### Checks for json version
try:
   import simplejson as json
except ImportError:
   import json as json
### Basic linear regression routine especially needed if no scipy.
count=0
def linreg(X, Y):
    """
    Summary
        Linear regression of y = ax + b
    Usage
        real, real, real = linreg(list, list)
    Returns coefficients to the regression line "y=ax+b" from x[] and y[], and R^2 Value
    """
    if len(X) != len(Y):  raise ValueError, 'unequal length'
    N = len(X)
    Sx = Sy = Sxx = Syy = Sxy = 0.0
    for x, y in map(None, X, Y):
        Sx = Sx + x
        Sy = Sy + y
        Sxx = Sxx + x*x
        Syy = Syy + y*y
        Sxy = Sxy + x*y
    det = Sxx * N - Sx * Sx
    a, b = (Sxy * N - Sy * Sx)/det, (Sxx * Sy - Sx * Sxy)/det
    meanerror = residual = 0.0
    for x, y in map(None, X, Y):
        meanerror = meanerror + (y - Sy/N)**2
        residual = residual + (y - a * x - b)**2
    RR = 1 - residual/meanerror
    ss = residual / (N-2)
    Var_a, Var_b = ss * N / det, ss * Sxx / det
    return a, b, RR

### Start collecting occupations from output files
if __name__=='__main__':
    bareresp=[]
    convresp=[]
    xtraresp=[]
    for num in range(0,len(typno)*len(typno)):
      bareresp.append(alphalist[1:1000])
      convresp.append(alphalist[1:1000])
      xtraresp.append(alphalist[1:1000])
    alphalist2=alphalist[1:1000]
    hubbylist2=alphalist[1:1000]
    for lines in range(0,len(alphalist)-1):
     for line2 in range(0,len(typno)*len(typno)):
      bareresp[line2][lines]=0.0
      convresp[line2][lines]=0.0
      xtraresp[line2][lines]=0.0
      alphalist2[lines]=float(alphalist[lines+1])
      hubbylist2[lines]=0.0
    hubbylist2.append(0.0)
    results=open('linrespmat.dat','w')
    if (len(hubbylist) > 1):
       uinl=hubbylist[0:1000]
       uoutl=hubbylist[0:1000]
       for line4 in range(0,len(hubbylist)):
        ### switch between Python and fortran numbering conventions
        if ( 'D' in hubbylist[line4]):
          hubbylist2[line4]=hubbylist[line4].split('D')[0]+'E'+hubbylist[line4].split('D')[1]
        else:
          hubbylist2[line4]=hubbylist[line4]
    count3=-1
    for hubby in hubbylist:
      count3+=1
      for hubtyp in typno: 
       for alpha in alphalist[1:1000]:
        ### Output files from jobrun.py, same format.
        pre=molname+'.s'+str(spin+1)+'.n'+species[hubtyp-1]+'.u'+str(hubby)
        file=pre+'.a'+alpha+'.out'
        output=open(file,'r').readlines()
        count=0
        for lines in range(0,len(output)):
          for hubnums in typno:
           ### We loop over the different Hubbard atom types.
           match=re.search('atom'+' '*(5-len(str(hubnums).split()))+str(hubnums)+'   Tr',output[lines])
           if match is not None:
            if len(typno)<=count<len(typno)*2:
             bareresp[typno.index(hubtyp)*len(typno)+typno.index(hubnums)][alphalist.index(alpha)-1]=float(output[lines].split()[3])
            if 0<=count<len(typno):
             xtraresp[typno.index(hubtyp)*len(typno)+typno.index(hubnums)][alphalist.index(alpha)-1]=float(output[lines].split()[3])
            if count>=len(typno)*2:
             convresp[typno.index(hubtyp)*len(typno)+typno.index(hubnums)][alphalist.index(alpha)-1]=float(output[lines].split()[3])
            count+=1
      chi0,chif=[],[]
      if (len(typno) == 2):
        if scipy_loaded is False:
           ### This is only needed if we don't have scipy and we have a 2x2 
           chii0,chiif,umat=[[0.0,0.0],[0.0,0.0]],[[0.0,0.0],[0.0,0.0]],[[0.0,0.0],[0.0,0.0]]
      for rstyp1 in range(0,len(typno)):
       chi0.append([])
       chif.append([])
       for rstyp2 in range(0,len(typno)):
        chi0[rstyp1].append(linreg(alphalist2,bareresp[rstyp1*len(typno)+rstyp2])[0])
        chif[rstyp1].append(linreg(alphalist2,convresp[rstyp1*len(typno)+rstyp2])[0])
      if scipy_loaded is True:
        ### Scipy matrix inversion
        print "U matrix\n"
        results.write("U matrix\n")
        umat=linalg.inv(chi0)-linalg.inv(chif)
        print umat
        np.savetxt(results,umat)
      elif len(typno)==1:
        ### Manual 2x2 matrix inversion
        det0=chi0[1][1]*chi0[0][0]-chi0[0][1]*chi0[1][0]
        detf=chif[1][1]*chif[0][0]-chif[0][1]*chif[1][0]
        chii0[1][1]=chi0[0][0]/det0
        chiif[1][1]=chif[0][0]/detf
        umat[1][1]=chii0[1][1]-chiif[1][1]
        chii0[0][0]=chi0[1][1]/det0
        chiif[0][0]=chif[1][1]/detf
        umat[0][0]=chii0[0][0]-chiif[0][0]
        chii0[0][1]=-chi0[0][1]/det0
        chii0[1][0]=-chi0[1][0]/det0
        chiif[0][1]=-chif[0][1]/detf
        chiif[1][0]=-chif[1][0]/detf
        umat[0][1]=chii0[0][1]-chiif[0][1]
        umat[1][0]=chii0[1][0]-chiif[1][0]
        print "Umatrix\n"
        print ' '*(6+len(str(umat[0][0]))/2-len(str(typnum[0]))/2), typnum[0],' '*(len(str(umat[1][1]))-len(str(typnum[0]))),typnum[1]
        print typnum[0],' '*(5-len(str(typnum[0]))),umat[0][0],umat[0][1]
        print typnum[1],' '*(5-len(str(typnum[1]))),umat[1][0],umat[1][1]

        results.write("Umatrix\n")
        results.write("%s %s %s %s\n" %(' '*(6+len(str(umat[0][0]))/2-len(str(typnum[0]))/2), typnum[0],' '*(len(str(umat[1][1]))-len(str(typnum[0]))),typnum[1]))
        results.write("%s %s %s %s \n" %(typnum[0],' '*(5-len(str(typnum[0]))),umat[0][0],umat[0][1]))
        results.write("%s %s %s %s\n" %(typnum[1],' '*(5-len(str(typnum[1]))),umat[1][0],umat[1][1]))
      else:
        ### Larger than 2x2 and no scipy.
        results.write("Bare response matrix elements\n")
        json.dump(chi0,results)
        results.write("\nConverged response matrix elements\n")
        json.dump(chif,results)
        results.write("\nRows and columns ordered by atom type order\n")
        json.dump(typnum,results)
    if matplotlib_loaded is True:
     if scipy_loaded is True:
      if vis=='yes':
       ###additional plotting of matrix elements
       fig=plt.figure()
       fig.subplots_adjust(wspace=0.3)
       ticknums,typnums=[-0.5],['']
       for num in range(0,len(typnum)):
          ticknums.append(num)
          typnums.append(typnum[num])
       ticknums.append(len(typnum)-0.5)
       typnums.append('')
       ax = fig.add_subplot(131, title='Bare Resp')
       colors.Normalize(vmin=None, vmax=None, clip=False)
       ax.imshow(chi0, cmap=cm.RdYlBu, interpolation='nearest')
       ax.locs,ax.labels=plt.xticks(ticknums,typnums)
       ax.locs,ax.labels=plt.yticks(ticknums,typnums)
       for q in range(0,len(umat)):
         for s in range(0,len(umat)):
             ax.annotate('%1.2f' %(chi0[s][q]), xy=(q-0.25, s),  xycoords='data',
                horizontalalignment='left', verticalalignment='bottom',color='white')
       ax2 = fig.add_subplot(132, title='Converged Resp')
       ax2.imshow(chif, cmap=cm.RdYlBu, interpolation='nearest')
       ax2.locs,ax.labels=plt.xticks(ticknums,typnums)
       ax2.locs,ax.labels=plt.yticks(ticknums,typnums)
       for q in range(0,len(umat)):
         for s in range(0,len(umat)):
             ax2.annotate('%1.2f' %(chif[s][q]), xy=(q-0.25, s),  xycoords='data',
                horizontalalignment='left', verticalalignment='bottom',color='white')
       ax3 = fig.add_subplot(133,title='U matrix')
       ax3.imshow(umat, cmap=cm.RdYlBu, interpolation='nearest')
       ax3.locs,ax.labels=plt.xticks(ticknums,typnums)
       ax3.locs,ax.labels=plt.yticks(ticknums,typnums)
       for q in range(0,len(umat)):
         for s in range(0,len(umat)):
             ax3.annotate('%1.2f' %(umat[s][q]), xy=(q-0.25, s),  xycoords='data',
                horizontalalignment='left', verticalalignment='bottom', color='white')
       plt.savefig('respmats')
