---
title: "Nudged elastic band"
subtitle:
aliases: /content/nudged-elastic-band
 

# Summary for listings and search engines
summary: 

# Link this post with a project
projects: []

# Date published
date: 2011-07-26

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
The nudged elastic band approach for identifying transition-states is implemented in [Quantum-ESPRESSO](http://quantum-espresso.org/ "http://quantum-espresso.org") and in version, [4.3.1](http://qe-forge.org/frs/?group_id=10 "http://qe-forge.org/frs/?group_id=10"), it can be driven by electronic structure results from either CP or [PWscf](http://www.pwscf.org/ "http://www.pwscf.org").  A basic example of how to use this approach is provided in #17 of the [examples](http://qe-forge.org/frs/?group_id=10 "http://qe-forge.org/frs/?group_id=10") that are distributed with the code.


 


This approach is useful both for identifying reaction pathways in the solid-state for things like vacancy migration or adatom hops, but it also is very useful for isolated systems to identify transition states in molecules.  Nevertheless, there are some pitfalls to the current implementation of NEB in [Quantum-ESPRESSO](http://www.quantum-espresso.org/ "http://www.quantum-espresso.org") that require careful consideration, particularly for quantum chemistry applications.


 


The first drawback has been [previously noted](../2011-07-12-quick-tip-constraining-molecular-coordinates "Constraining molecular coordinates") in the constraining molecular coordinates quick tip: rotations and translations must be frozen out to avoid incorporating these into your reaction pathway for isolated systems. You should also be careful to avoid introducing any translations or rotations between the different starting coordinates you provide.


 


An second concern is that the listing of atomic positions must be ordered in exactly the same way for the first and last image (a.k.a. reactant and product) and any specified intermediate images.  The interpolating code assumes that the atoms are ordered exactly the same way in all images, and if the order changes, the net effect is that spurious paths are interpolated.  The easiest way to check that you have the correct ordering between atoms in the first and last image is to pass your NEB input to [XCrysDen](http://www.xcrysden.org/ "http://www.xcrysden.org"):


                                   ```xcrysden --pwi <inputfile>```


You can then view the different interpolated starting images of your path using the animation control center in [XCrysDen](http://www.xcrysden.org/ "http://www.xcrysden.org").  If you see any atoms move significantly more than you expected or even the molecule breaking apart and reforming, that is a sign that the atoms in your images are not correctly ordered. If you are using a builder that relies on a z-matrix formalism for building structures, such as [molden](http://www.cmbi.ru.nl/molden/ "http://www.cmbi.ru.nl/molden/"), it is likely that the atoms will get reordered between different structures.  


 


Finally, it is important to note, especially for molecules, that the interpolation scheme is purely linear and does not take into account what is a sensible distance between different atoms.  In order to obtain a good initial guess, it is highly advisable that you generate a transition state guess or maybe even a few additional approximate images.  You can use the initial guess shown in [XCrysDen](http://www.xcrysden.org/ "http://www.xcrysden.org") as a guide for any improvements. 


 


I hope that this **feature review** has helped you to better understand how to make the most of transition state determination in [Quantum-ESPRESSO](http://www.quantum-espresso.org/ "http://www.quantum-espresso.org") and [PWscf](http://www.pwscf.org/ "http://www.pwscf.org"). Please [email me](mailto:hjkulikATmitDOTedu?subject=Questions%20about%20nudged%20elastic%20band%20review "mailto:hjkulikATmitDOTedu?subject=Questions about nudged elastic band review") if you have any additional questions not answered here!


