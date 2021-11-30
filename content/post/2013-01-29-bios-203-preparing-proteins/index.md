
---
title: BIOS 203: Preparing proteins
subtitle: 

# Summary for listings and search engines
summary: 

# Link this post with a project
projects: []

# Date published
date: 2013-01-29

# Date updated
lastmod: 

# Is this an unpublished draft?
draft: false

# Show this page in the Featured widget?
featured: false

# Featured image
# Place an image named `featured.jpg/png` in this page's folder and customize its options here.
image:
  caption: 
  focal_point: ""
  placement: 2
  preview_only: false

authors:
- admin

tags:

categories:
- tutorials

---
The protein databank (PDB) has a wealth of structures that have been solved through x-ray crystallography or NMR.  Often when we are simulating proteins, we start directly from such structures in order to infer electronic and geometric properties of these proteins.  Many times, we still need to do significant modification and characterization of our protein PDB files in order to get them ready for our simulations. Today, I will walk you through some basic steps in preparing protein structures and visualizing the cavities inside proteins where interesting reactions and phenomena often occur.


 


1. Tweaking protein structures


We’ll work in [PyMOL](http://www.pymol.org/ "http://www.pymol.org") to prepare a protein structure for further evaluation. [Download pymol here](http://www.pymol.org/ "http://www.pymol.org") and read about some basic visualization tricks in previous tutorials [here](more-visualization-vmd-pymol "More visualization with VMD and PyMOL") and [here](visualizing-trajectories-pymol "Visualizing trajectories with PyMOL").


![](/sites/default/files/SyrB2-panel-for-tut.png)   
**Fig 1.** (Top, left): Cut through of SyrB2 showing channel of delivery of L-Thr substrate, (Top, right): SyrB2 active site consisting of Fe(II), two His, alpha-ketoglutarate, and a chloride. (Bottom): Schematic of SyrB1 substrate binding and SyrB2 halogenation.
 


As an example, we’ll look at SyrB2, a non-heme Fe(II) halogenase (PDB ID: 2FCT) that is in the antifungal syringomycin E biosynthetic pathway.  SyrB2 only halogenates its L-Thr substrate when that substrate is delivered on a phosphopantetheine prosthetic tether through a long channel in the protein to the central active site (Fig. 1). 


 


Load the protein into PyMOL:


PyMOL> fetch 2FCT


 


SyrB2 is crystallized with two copies per unit cell. Extract only the first copy:


PyMOL> sele A, chain A


PyMOL> extract 2FCT\_A, A


PyMOL> delete 2fct


PyMOL> delete A


  


Your pymol view should look like this:



![](/sites/default/files/view1_pymol.jpg)

 


 


 


 


 


 


 


 


 


 


 


 


 


 


 


 


The red crosses represent water molecules, and you can see there are no protons represented in our structure. Now, let’s turn the sequence on to see  what else is in our structure:


PyMOL> set seq\_view, on


Change the sequence view from single letter codes to three letter codes:


PyMOL> set seq\_view\_format, 1


 


Now, if we scroll to the right towards the end of the protein chain, we’ll see we have things in our structure besides just amino acids:



![](/sites/default/files/view2_pymol.jpg)

 


 


 


VAL is our last amino acid residue and we can see the residue numbers skip ahead to 896.


 


Here we have: DSU, AKG, FE2, CL, CL, HOH... 


DSU=detergent molecule from crystallization


AKG, FE2, CL=active site components (one extra CL)


HOH = solvating waters


 


First we’ll delete the detergent molecule (DSU) and all of the waters:


PyMOL> remove resn DSU


PyMOL> remove resn HOH


 


Now, we want to know which CL to delete because it’s not in the active site.


PyMOL> sele CL, resn CL


PyMOL> show spheres, CL


PyMOL> show spheres, resn FE2


 


Clearly, we can see one of the chlorides is close to the active site, while the other is further away:



![](/sites/default/files/view3_pymol.jpg)

 


 


 


 


 


 


 


 


 


 


 


 


 


 


 


 


Let’s remove the extra Cl:


PyMOL> zoom CL, 3


Go to the menu up top and choose Mouse>Selection Mode>Atoms.


Click on the CL that is far from the Fe(II) center. A new selecton called sele will appear. Remove these atoms:


PyMOL> remove sele


Now, we’ve got the basic protein without any hydrogens so let’s save what we have so far as 2FCT\_holo\_noH.pdb by going to File>Save Molecule> and following prompts.


 


Next, we can add hydrogens to our system, but we’ll want to pay special attention to our active site. We will first create a selection using basic selection arguments to isolate our active site:


PyMOL> sele Fe, resn FE2


PyMOL> sele AS, br. all within 2.5 of Fe


PyMOL> zoom AS


PyMOL> show sticks, AS


PyMOL> set sphere\_scale, 0.3


 


You should now see something that looks like this:



![](/sites/default/files/2d51ddcbaa058a736f78826b2e8cb2ff.jpg)

 
You'll want to check the formal charge assignment of the atoms in the active site. You can do this by clicking on the “L” for label in the side panel next to (AS). Label>Other properties>Formal charge.
 


You’ll notice that the Fe(II) has been assigned a charge of zero. The carboxylate on alpha-ketoglutarate also has a zero charge. We’ll change Fe to +1 (close enough) and the oxygen on alpha-ketoglutarate to -1. Choose Mouse> 3 Button editing mode. Click on an oxygen in aKG and go to  Build>Make pk1 negative. Unclick that atom, now click on the iron and choose Build>Make pk1 positive.


 


Now, next to 2FCT\_A, choose “A” for action, Action>Add hydrogens. You should see something like this:



![](/sites/default/files/view4_pymol.jpg)

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
We can see that the hydrogens are now added in the correct place. Let’s save this structure as 2FCT\_holo\_withH.pdb.
 


Let’s turn off the lines for now and turn on a cartoon representation of the protein:


PyMOL> hide labels


PyMOL> hide lines, 2FCT\_A


PyMOL> show cartoon, 2FCT\_A


PyMOL> zoom all


 


You should see something that looks like this:



![](/sites/default/files/view5_pymol.jpg)

 


 


 


 


 


 


 


 


 


 


 


 


 


 


 


 


 


 


 


 


It turns out that in the crystal structure, there is a residue Phe196 that is rotated in such a way to block the most probable channel for PPant entry.


 


We’re going to try both rotating and mutating this residue to increase channel size (relevant later for pore and cavity visualization). First, let’s copy our object to keep it safe going to “A” for Action next to 2FCT\_A and choose “Duplicate object”. A new object, obj01 will be created. Hide this object for now by clicking on its name. Now, let’s take a look at Phe196:


 


PyMOL> sele f196, resi 196 and 2FCT\_A


PyMOL> zoom f196 or AS, 5


 


Now, we’ll first make the F196A mutant. In the menu bar, select Wizard>Mutagenesis and click on the F196 residue. Where it says “No Mutation” in the right panel, click and select “ALA”. You should see something like this:



![](/sites/default/files/view6_pymol.jpg)

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
The new Ala is shown in gray. Click “Apply” then “Done”.  Go to File>Save Molecule> and save as 2FCT\_F196A\_withH.pdb. Hide 2FCT\_A and show obj01 now. We’re going to now rotate F196 in obj01. Don’t forget to:
 


PyMOL> sele f196, resi 196 and obj01


 


Go back to Wizard>Mutagenesis. Click on F196 again. This time change “ALA” to “No mutation”. We can move through the rotamer library for Phe using the buttons at the bottom of our right panel. Choose State 3 of 3.



![](/sites/default/files/view7_pymolb.jpg)

 


 


 


 


 


 


 


 


 


Click “Apply” and “Done”. Go to File>Save Molecule> and save as 2FCT\_F196Rot\_withH.pdb. You should see something like this:



![](/sites/default/files/view8_pymol.jpg)

 


 


 


 


 


 


 


 


 


 


 


 


 


 


 


 


 


 


 


 


 


PyMOL can visualize approximate surfaces for us. Let’s take a look at surfaces of each of our modified structures to see if we have opened our channel sufficiently. Rotate the structure so that you’re looking down at Fe and F196:


PyMOL> set sphere\_scale, 1.0


PyMOL> show surface, obj01


PyMOL> set surface\_color, gray50


Also, go to Setting>Transparency>Surface>40%. Do this separately for the F196A case. You should be able to see the iron center through the channel formed in the protein surface:


![](/sites/default/files/view9and10_pymol.jpg)
 
So, yes, we’ve opened the channel. By comparison, here is what the original structure looked like with a blocked channel:

![](/sites/default/files/view11_pymol.jpg)

 


 


 


 


 


 


 


 


 


 


 


2. Cavity visualization


We’ll use the [Voss Volume Voxelator (3V) web interface](http://3vee.molmovdb.org/ "http://3vee.molmovdb.org") to more accurately calculate cavities in our protein structure. Click on “Channel finder” “Extract all channels”.


 


We’re going to process the following files that we generated earlier:


2FCT\_holo\_withH.pdb


2FCT\_F196A\_withH.pdb


2FCT\_F196Rot\_withH.pdb


 


Make selections about your protein in this interface, namely choose a minimum of 10 channels, high grid resolution, PyMOL compatible, create water PDB and start channel finder, and minimum inner probe radius of 1.5 instead of 3.0.



![](/sites/default/files/3V_ss1.jpg)

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
The program will run in the web interface and it will periodically update you as it runs over the next few minutes. 

![](/sites/default/files/3V_ss2.jpg)

 


 


 


 


 


 


 


 


 


 


 


 


 


 


 


 


 


 


 


The web interface will then show you visualizations of all your channels and also give you a chance to download files that contain your channels and will also render them for you in Chimera. You’ll find that 3V only detects one channel for 2FCT, regardless of the F196A model or F196Rot (left and right below) that looks like this (>800 sq Angstrom volume):


![](/sites/default/files/3vcavityvis.png)
 
Using these same tools, we cannot find any suitable channels for the original structure from the crystal structure. In the future, we’ll use these same tools to prepare volumes for docking and identifying water binding sites.
 


I hope you found this protein preparation mini-tutorials helpful. If you have any questions, please [email me](mailto:hjkulik@mit.edu?subject=Questions%20about%20BIOS%20203%20preparing%20proteins "mailto:hjkulik@mit.edu?subject=Questions about BIOS 203 preparing proteins")!


