import os
#Molecule parameters
spin,charge=5,0
molname='MnO'
#U calculation parameters 
job='uscf'
# U is applied to each unique atom type indicated by a '1' in the XYZ file in 5th column.

hubbylist=['1D-40'] #linear response U
alphalist=['1D-40','-0.08','-0.05','-0.02','0.02','0.05','0.08']
#Cluster-specific parameters
pseudodir='./'
savedir='./wfns/'
if os.path.exists(savedir) != 1: 
 os.system('mkdir %s\n' %(savedir))
scratchdir='/scratch/myname/'
para='mpirun' # also include here any node-based specifications
nodes=1
cpu=2
bindir='~/espresso-4.3/'
execname='pw.x'
# If running in serial, set para='' and cpu will be ignored.
vis='yes'
