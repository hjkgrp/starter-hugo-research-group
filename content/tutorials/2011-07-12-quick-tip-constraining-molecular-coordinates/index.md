---
title: "Quick tip: Constraining molecular coordinates"
subtitle:
aliases: /content/quick-tip-constraining-molecular-coordinates
 

# Summary for listings and search engines
summary: 

# Link this post with a project
projects: []

# Date published
date: 2011-07-12

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
Have you ever run a relaxation or a path optimization technique (e.g. nudged elastic band or string metadynamics) on an isolated system only to find that you were getting spurious answers arising from rotation or translation of your system? Have you ever wanted to fix one part of your molecule and only relax another portion of it? Have you ever tried to optimize donor-acceptor distances between two molecules or molecular fragments?  Well, there are actually two distinct ways to optimize structures with some measure of constraint on positions in the [PWscf](http://www.pwscf.org/ "http://www.pwscf.org") portion of [Quantum-ESPRESSO](http://quantum-espresso.org/ "http://quantum-espresso.org").


 


**The simple way: fixing cartesian coordinates**


In the `ATOMIC\_POSITIONS` namelist of your input file, you can add additional flags in the fifth through seventh column alongside each atom to freeze coordinates.  The column ordering of these flags follows the same as the coordinates in the 2nd-4th column and a ‘0’ freezes the particular x-, y-, or z-position of each atom, while a ‘1’ corresponds to allowing the atom to move freely in that direction.  You don’t have to set this flag for each atom, but once you set a single coordinate flag on a given atom, you should set the flag for each x-, y-, and z-coordinate.   This method for freezing coordinates works alongside all other approaches including both nudged elastic band and structural relaxations.


 


**The (slightly) harder way: defining internal coordinate constraints**


Although PWscf does not currently support a z-matrix or internal coordinate form for the atomic positions, it is possible to impose constraints that are defined in terms of internal coordinate parameters.  To carry out a constrained relaxation, we set up a relaxation with `ion\_dynamics=‘damp’` and add an additional `CONSTRAINTS` namelist to the end of the input file after `K\_POINTS`:


    ```CONSTRAINTS```


The first line of this namelist should include the number of constraints you wish to apply and the tolerance on achieving those constraints:


    ```<num\_constraints> <tolerance>```


The remaining lines are where you define the constraints in terms of the atom number of each atom in the constraint as defined by its order in your `ATOMIC\_POSITIONS` input:


    ```<constr\_type>, <at #s comma delimited>, <constraint value>```


 


More specifically, for each constraint, line 2 and onwards can be defined with any combination of the following:


 


distance:    `‘distance’, <#at1>, <#at2>, <tgt distance>` 


                                                                **(in bohrs!)**


angle:       `‘planar\_angle’, <#at1>,<#at2>,<#at3>, <tgt angle>` 


                                       ijk angle with 2=j vertex      **(in degrees!)**


dihedral:    `‘torsional\_angle’,<at#1>,<at#2>,<at#3>,<at#4>,<tgt dihed>`


                                       ijkl/1234 order with 2&3 central   **(in degrees!)**


 


Some additional constraints on other quantities such as coordination number are also available, and I encourage you to read the INPUT\_PW file that is in the Doc folder of your Quantum-ESPRESSO installation root for more details.


 


I hope that this quick tip has helped you to better understand how to make the most of your structural relaxations in [PWscf](http://www.pwscf.org/ "http://www.pwscf.org").  Please [email me](mailto:hjkulikATmitDOTedu?subject=Questions%20about%20constraints%20quick%20tip "mailto:hjkulikATmitDOTedu?subject=Questions about constraints quick tip") if you have any additional questions not answered here!


