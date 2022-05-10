import os
#Molecule parameters
spin,charge=5,0
molname='MnO'

#U calculation parameters 
job='uscf'
# U is applied to atom number and type indicated in XYZ file in 5th column.

hubbylist=['1D-40'] #linear response U
#hubbylist=['1D-40','0.5','1.0','1.5','2.0','2.5','3.0'] #self-consistent
alphalist=['1D-40','-0.08','-0.05','-0.02','0.02','0.05','0.08']

#Cluster-specific parameters
nodes=1
cpu=2
pseudodir='./'
savedir='./wfns/'
if os.path.exists(savedir) != 1: 
 os.system('mkdir %s\n' %(savedir))
scratchdir='/scratch/myname'
para='mpirun'
bindir='~/espresso-4.3/bin/'
execname='pw.x'
# If running in serial, set para='' and cpu will be ignored.
