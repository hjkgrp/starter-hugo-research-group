#Import both the mol3D and atom3D classes from molSimplify
from molSimplify.Classes.mol3D import *
from molSimplify.Classes.atom3D import *

rotaxane = mol3D() #Create an instance of the mol3D class, currently the molecule object is empty
rotaxane.readfromxyz('Rotaxane.xyz') #Now load in the atoms and coordinate information from the .xyz file

metal_atom_index = rotaxane.findMetal() #use the find metal method to indentify metal atoms in our molecule
print(metal_atom_index) #notice the findMetal() returns a list

metal_atom = rotaxane.getAtom(0) #Returns the zeroth atom as a atom3D class object
print(metal_atom.symbol()) #Print the symbol associated with this atom3D object


rotaxane.deleteatom(0) #use the deleteatom() to remove the copper atom

rotaxane.writexyz('No_Metal_Rotaxane') #mol3D files can be written to file using the writexyz() method
