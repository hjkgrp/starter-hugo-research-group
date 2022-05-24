---
title: "Quick tips: More about U"
subtitle:
aliases: /content/quick-tips-more-about-u
 

# Summary for listings and search engines
summary: 

# Link this post with a project
projects: []

# Date published
date: 2013-11-30

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
This month marked both the AIChE national meeting in San Francisco's special symposium that I co-organized called "Applications of DFT+X in catalysis" as well as my first month as an assistant professor.  The tutorials are likely to be archived and remain online but will no longer be updated as frequently. In Fall 2014, I will teach an elective in simulations at MIT, and some of this material may make its way to the tutorial page here. Here are a couple of quick tips related to questions that came up during the session and beyond:


1. Electron delocalization: if metallic character in a solid occurs upon vacancy formation in an oxide...this may be a common issue that is alleviated with a U, leading to differences in electronic states. 


2. Using "ramping: For users of DFT+U with CP2K, "ramping" is encouraged.  This is where low U values are used at first to ensure convergence to a specific electronic state. Note, using the potential from a previous SCF calculation is a useful tool for converging the same electronic state at a different value of U or with a different functional.


3. Unphysical values of "U": When a manifold is nearly empty or nearly full, response functions from the linear-response calculation of U become small. Inverting the bare and converged numbers may result in two large numbers that, when subtracted, will give a non-zero number that has little meaning.  


4. Solid state vs. single site vs. slabs: In the solid state, a U calculation should be done in a matrix formalism, with each unique site getting its own U calculation (you can fill in the rest through symmetry).  Single site calculations, we simply invert a number and subtract. For slab calculations (both pristine and decorated), it's worthwhile to note that under-coordinated species often have different values of U than those in the bulk. 


5. Self-consistent U is most useful when the DFT(LDA/GGA) ground state is distinct from the state observed at non-zero U.  This is particularly important for cases where the two states cannot both be self-consistently achieved. For qualitatively equivalent electronic states, a linear-response U is often sufficient.  A more complete tutorial for calculating the self-consistent U will be provided next month.


Hope you found these quick tips helpful. Stay tuned while tutorials shift gears and possibly go more back to basics while I address the needs of our new research group.


