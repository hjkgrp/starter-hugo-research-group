import os
#Molecule parameters
molname='Fe-bcc'
charge=0
#U calculation parameters 
job='uscf'
# U is applied to atom number and type indicated in XYZ file in 5th column.

hubbylist=['1D-40'] #linear response U
#hubbylist=['1D-40','0.5','1.0','1.5','2.0','2.5','3.0'] #self-consistent
alphalist=['1D-40','-0.15','-0.10','-0.05','0.05','0.10','0.15']

#Cluster-specific parameters
nodes=1
cpu=16
npool=4
pseudodir='./'
savedir='./wfns/'
if os.path.exists(savedir) != 1: 
 os.system('mkdir %s\n' %(savedir))
scratchdir=''
para='mpirun'
bindir='~/0-Codes/espresso-4.3.2/PW/'
#bindir='~/0-Codes/espresso-4.3.2/bin/'
execname='pw.x'
# If running in serial, set para='' and cpu will be ignored.
