---
title: "Ab initio steered molecular dynamics with TeraChem"
subtitle:
aliases: /content/ab-initio-steered-molecular-dynamics-terachem
 

# Summary for listings and search engines
summary: 

# Link this post with a project
projects: []

# Date published
date: 2015-06-08

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
  placement: 1
  preview_only: false

authors:
- admin

tags:

categories:
- tutorials

---
Today I'll briefly review how to set up a steered molecular dynamics calculation in TeraChem. In these steered molecular dynamics calculations, specific atoms (attachment points, APs) are pulled at constant force towards pulling points (PPs) that are some distance in space. These calculations are useful for mimicking mechanochemical depolymerization, but more recently, [we've shown](http://pubs.acs.org/doi/pdf/10.1021/acs.jpca.5b03503) it is also a useful tool for discovering depolymerization pathways and identifying the relative effectiveness of a catalyst by comparing force-dependent cleavage profiles.


In order to run a steering calculation in TeraChem, you'll need a few things:


1) a steering file that contains the pulling points and attachment point identities at a set distance away.



2) an input file set up for molecular dynamics that specifies this is a steered molecular dynamics calculation.


Let's look at 1) first:



Here's an example steering file for a coniferyl alcohol beta-o-4 lignin dimer:

```
2

3 -16.927 2.94 2.54 0.0485511754
13 51.04 -5.42 13.17 0.0485511754
```
The first line specifies the number of pulling points (2).



The second line indicates the first PP-AP pair. First is the atom indexed from 0 (so 3 is the 4th atom in 1-indexing), next 3 numbers are the PP in cartesian coordinates, finally the last column is the pulling force in Ha/bohr. A useful conversion is 1.0 nN = 0.01213779385 Ha/bohr so the above force corresponds to 4.0 nN.



The third line is the same as the 2nd line but for a different PP-AP pair involving atom 13 (14th with 1-indexing).


Now, let's look at 2). Inside your regular input file, you'll want to specify your standard parameters, e.g.:


```
coordinates start.xyz  
charge 0  
basis 6-31g  
method uwpbeh  
levelshift yes  
levelshiftvala 1.0  
levelshiftvalb 0.0  
```
The above cover coordinates, charge, method and basis (uwpbeh/6-31g), levelshifting for unrestricted solutions.  

Then we'll also want MD parameters just as in a standard MD job, e.g.:


```
run md  
nstep 80000  
rescalefreq 80001  
tinit 300  
seed 2824  
integrator reversible\_d  
timestep 0.25  
```
which corresponds to an MD run with NVE dynamics, a specified seed for the random initial velocities, a 0.25fs timestep, and a reversible integrator. Note we've specified a large number of steps, but typically you will manually stop your MD run when the APs reach the PPs.


Finally here is the specific keyword for steered md:  
```
steering steering.txt
```

Note here the 2nd steering refers to a file named 'steering' that was described in 1. You can also name it something else more descriptive. Note, you'll want to set your PPs based on your APs, e.g. using a visualization program such as Avogadro or with a script. You can also add these as dummy atoms to your coordinates in a separate file in order to visualize and check your force vectors.


I've attached starting coordinates, input file, and steering file for this example calculation to this tutorial. You may also read about our approach [here](http://pubs.acs.org/doi/pdf/10.1021/acs.jpca.5b03503).


I hope you've found this mini-review useful for the ab initio steering MD feature in [TeraChem](http://www.petachem.com). Please [let me know](mailto:hjkulikATmitDOTedu) if you have any additional questions.


