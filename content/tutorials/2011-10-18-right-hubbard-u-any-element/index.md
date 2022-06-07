---
title: "The right Hubbard U for any element"
subtitle:
aliases: /content/right-hubbard-u-any-element
 

# Summary for listings and search engines
summary: 

# Link this post with a project
projects: []

# Date published
date: 2011-10-18

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
Thus far, I’ve told you about how to calculate the Hubbard U for [single](../2011-05-31-calculating-hubbard-u "Calculating the Hubbard U") [sites](calculating-hubbard-u "Calculating the Hubbard U")or [multiple sites](../2011-06-28-hubbard-u-multiple-sites "Hubbard U for multiple sites") and how to [troubleshoot common problems with DFT+U](../2011-09-13-troubleshooting-common-problems-dftu "Troubleshooting common problems with DFT+U"). In fact, calculating U is nearly as easy as carrying out a single point calculation.  It is also a powerful tool that gives you information about the electronic structure of your system that can’t be achieved by using functionals that have been fit to a data set.



However, one of the most common myths is that the U is a parameter that must be set based on each element. In [Quantum-ESPRESSO](http://www.quantum-espresso.org/ "http://www.quantum-espresso.org"), the Hubbard U that you calculate is highly sensitive to the environment around the metal and the oxidation state of the metal. There is no single “Hubbard U” for iron or for any other metal, but the values of U that you calculate in the code can be comparable for iron-containing complexes with similar bonding patterns.


 


Another myth is that there are only a few elements for which DFT+U is appropriate.  In fact, we have shown that it can be useful for elements with nearly empty 3d manifolds - such as Scandium or Vanadium - in addition to other elements.


 


I hope that this quick tip has helped you to better understand the importance and ease of calculating U in [Quantum-ESPRESSO](http://www.quantum-espresso.org/ "http://www.quantum-espresso.org") and [PWscf](http://www.pwscf.org/ "http://www.pwscf.org"). Please [email me](mailto:hjkulik@mit.edu?subject=Questions%20about%20Hubbard%20U%20for%20any%20element "mailto:hjkulik@mit.edu?subject=Questions about Hubbard U for any element") if you have any additional questions not answered here!


