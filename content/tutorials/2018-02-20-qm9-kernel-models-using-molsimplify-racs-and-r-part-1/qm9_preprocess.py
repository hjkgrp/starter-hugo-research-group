import glob, os, sys
from molSimplify.Informatics.autocorrelation import generate_full_complex_autocorrelations
from molSimplify.Classes.mol3D import mol3D

class quickrun:
    def __init__(self,name,mol,prop):
        self.name =  name
        self.mol = mol
        ## descriptors
        self.set_desc = False
        self.descriptors =  list()
        self.descriptor_names =  list()
        self.prop = prop

    def get_descriptor_vector(self,loud=False,name=False):
        results_dictionary = generate_full_complex_autocorrelations(self.mol,depth=3,loud=loud)
        self.append_descriptors(results_dictionary['colnames'],results_dictionary['results'],'f','all')
        self.set_desc = True
    
    def append_descriptors(self,list_of_names,list_of_props,prefix,suffix):
        for names in list_of_names:
            if hasattr(names, '__iter__'):
                names = ["-".join([prefix,str(i),suffix]) for i in names]
                self.descriptor_names += names
            else:
                names = "-".join([prefix,str(names),suffix])
                self.descriptor_names.append(names)
        for values in list_of_props:
            if hasattr(values, '__iter__'):
                self.descriptors.extend(values)
            else:
                self.descriptors.append(values)

def write_data_csv(list_of_runs):
    with open('QM9_descriptor_file.csv','w') as f:
        f.write('runs, '+",".join(prop_strings)+',')
        n_cols = len(list_of_runs[0].descriptor_names)
        for i,names in enumerate(list_of_runs[0].descriptor_names):
            if i<(n_cols-1):
                f.write(names+',')
            else:
                f.write(names+'\n')
        for runs in list_of_runs:
            try:
                f.write(runs.name)
                for properties in runs.prop:
                    f.write(','+str(properties))
                for properties in runs.descriptors:
                    f.write(','+str(properties))
                f.write('\n')
            except:
                pass

def write_smiles_csv(smi_dict):
    with open('QM9_smiles.csv','w') as f:
        for name in smi_dict.keys():
            try:
                f.write(str(name))
                f.write(',')
                f.write(str(smi_dict[name]))
                f.write('\n')
            except:
                pass

atom_u0_dict = dict()
with open('atomref.txt','r') as f:
    ll = f.readlines()
    for i,l in enumerate(ll):
        if (i>4) & (i<10):
            ls = l.split()
            atom = ls[0]
            u0 = float(ls[2])
            atom_u0_dict.update({atom:u0})
    print('found reference data')


# check and create new folder
if not os.path.isdir('qm9_geos/'):
    os.makedirs('qm9_geos')

# begin parsing
print('starting loop over data, please be patient...')
target_paths=sorted(glob.glob('qm9_data/*.xyz'))
print('found ' + str(len(target_paths)) + ' molecules to read')
count = 0
max_size = 0
list_of_runs = list()
smi_dict = dict()
for geos in target_paths:
    count += 1
    ll = os.path.basename(geos)
    ll = ll.strip('.xyz')
    name = ll.split("_")[1]
    new_geo = 'qm9_geos/'+name+'.xyz'
    with open(geos,'r') as oldf:
        this_correction = 0
        with open(new_geo,'w') as newf:
            natoms = False
            for i,lines in enumerate(oldf.readlines()):
                if ("*^" in lines): # repalce exp with E
                                    # to aid parsing
                    lines = lines.replace('*^','E')
                if (i==0):
                    natoms = int(lines.strip('\n'))
                if (i < (natoms +2)) and not (i==1):
                # this corresponds to geo part of file
                    newf.write(lines) # write to proper xyz
                    if (i>1): # the first line is the number of atoms
                        this_atom = lines.split()[0] # first character is atom symbol
                        this_correction += -1*float(atom_u0_dict[this_atom])
                        # fetch the correction
                if (i==1): # properties line
                    props=lines.strip('\n')
                    props=props.split('\t')                           
                    newf.write("# name "+name+'\n')
                #                            print('prop is ' + str(props[11]))
                    u0 = float(props[11])
                if i == (natoms +3): # SMILEs string 
                   smi = (lines.strip('\n'))
                   smi=smi.split()[0]
                   smi_dict.update({name:smi}) # record the SMILEs`
            u0 += this_correction # update the atomization energy
            prop_strings = ['u0']
            prop = [u0]
    # print(prop_strings,'propstring')
    this_mol = mol3D() # mol3D instance
    this_mol.readfromxyz(new_geo) # read geo
    this_run = quickrun(name,this_mol,prop) # create run object
    this_run.get_descriptor_vector() # get the descriptor
    list_of_runs.append(this_run) # record this run
    sys.stdout.write('\r number of molecules read = '+str(count) + "/"+str(len(target_paths)))
    sys.stdout.flush()

write_data_csv(list_of_runs)
write_smiles_csv(smi_dict)
print(' complete!')
