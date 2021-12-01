---
title: "All about the tutorials"
subtitle: 

# Summary for listings and search engines
summary: 

# Link this post with a project
projects: []

# Date published
date: 2011-05-24

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
Welcome to a new [tutorial series](../Tutorials "../Tutorials") that I have put together about using [Quantum-ESPRESSO](http://quantum-espresso.org/ "http://quantum-espresso.org") for quantum chemistry applications.  These [tutorials](../Tutorials "../Tutorials") will be focused primarily on [using PWscf](http://www.quantum-espresso.org/users-manual/ "http://www.quantum-espresso.org/users-manual/") for applications near and dear to my heart - transition-metal complexes.  However, some of the tutorials will also directly cover applications in the condensed phase or be easily extendable to such systems.


 


The form of the tutorials will begin with a written explanation of the background and purpose of each exercise. The job scripts are written in [python](http://www.python.org/ "http://www.python.org") or, alternatively, [Bash](http://en.wikipedia.org/wiki/Bash_(Unix_shell) "http://en.wikipedia.org/wiki/Bash_(Unix_shell)"), and their contents are explained both in the tutorial body and in a README file.  In order to maximize backwards compatibility, the python scripts will be written to be compatible with Python[v 2.4](http://www.python.org/download/releases/2.4.3/ "http://www.python.org/download/releases/2.4.3/") or [later](http://www.python.org/download/releases/2.7.1/ "http://www.python.org/download/releases/2.7.1/") unless otherwise noted.  A [scipy](http://www.scipy.org/ "http://www.scipy.org") installation is not required, but it is helpful.


 


Whether you are new to [Quantum-ESPRESSO](http://quantum-espresso.org/ "http://quantum-espresso.org") or a veteran of the code, you may have noticed that the input deck has a tendency to evolve from version to version.  With that in mind, all scripts were originally written to generate input files compatible with the most recent version of the code, which, at the start of the tutorials was [v4.3.1](http://qe-forge.org/gf/project/q-e/ "http://qe-forge.org/gf/project/q-e/").  However, where it is possible to provide backwards and forwards compatibility, alternative lines of code that can be toggled on and off are provided in the main job scripts to provide backwards and forwards compatibility to [v3.0](http://www.pwscf.org/download.php#previous "http://www.pwscf.org/download.php#previous") of [Quantum-ESPRESSO](http://quantum-espresso.org/ "http://quantum-espresso.org") and up to v5.x (as of Summer 2013 port of tutorials to new site).


 


I recommend [VMD](http://www.ks.uiuc.edu/Research/vmd/ "http://www.ks.uiuc.edu/Research/vmd/"), [XCrysDen](http://www.xcrysden.org/ "http://www.xcrysden.org/"), and [pymol](http://www.pymol.org/ "http://www.pymol.org/") for visualization of molecules and associated properties, [Molden](http://www.cmbi.ru.nl/molden/howtoget.html "http://www.cmbi.ru.nl/molden/howtoget.html") for building molecules, and [xmgrace](http://plasma-gate.weizmann.ac.il/Grace/ "http://plasma-gate.weizmann.ac.il/Grace/") or [matplotlib](http://matplotlib.sourceforge.net/ "http://matplotlib.sourceforge.net/") for making graphs, but the tutorials are written as generally as possible to minimize version and specific software dependency.


 


Any questions or requests about these tutorials is welcome! (Feel free to [email me](mailto:hjkulikATmitDOTedu?subject=QC%20with%20Q-E%20Tutorials "mailto:hjkulikATmitDOTedu?subject=QC with Q-E Tutorials") or read more [about me](../about-heather "..//about-heather") and my work [here](../Research "../Research")).  More general questions about the [Quantum-ESPRESSO](http://quantum-espresso.org/ "http://quantum-espresso.org") code can be typically answered by consulting the [online manual](http://www.quantum-espresso.org/wp-content/uploads/Doc/user_guide.pdf "http://www.quantum-espresso.org/wp-content/uploads/Doc/user_guide.pdf"), reading [mailing list archives](http://qe-forge.org/pipermail/pw_forum/ "http://qe-forge.org/pipermail/pw_forum/"), or [subscribing to the mailing list](http://pwscf.org/mailman/listinfo/pw_forum "http://pwscf.org/mailman/listinfo/pw_forum") and emailing directly.


 


I hope you enjoy these tutorials as I aim to simplify some of the challenges associated with using Quantum-ESPRESSO for quantum chemistry applications!


