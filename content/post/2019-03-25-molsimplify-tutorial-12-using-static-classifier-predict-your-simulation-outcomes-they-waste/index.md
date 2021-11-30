
---
title: molSimplify Tutorial 12: Using the static classifier to predict your simulation outcomes before they waste your time
subtitle: 

# Summary for listings and search engines
summary: 

# Link this post with a project
projects: []

# Date published
date: 2019-03-25

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
 


Geometry optimization with density functional theory (DFT), a general procedure to obtain the ground state structures of a complex, is computationally demanding in terms of time and can also easily fail. Two main failure modes are 1) the expected geometry cannot maintain stability during the DFT simulation (e.g., ligand dissociation) and 2) the electronic structure of the optimized geometry is bad, which indicates the system of study is out of the domain of applicability of DFT. Either case can only be identified after a simulation completes, leading to a massive waste of the computational resources (and your time!).


To address this challenge, we built machine learning models to classify the simulation outcomes and readily achieved a good performance on the out-of-sample test data. With carrying out simulations that were predicted as "successful" by the static classifier, which were around half of the total simulations of interests, we covered 90 percent of valid design space. To increase the applicability of the static classifier, we further developed a model confidence metric based on the distribution of data points in the latent space, thus called latent space entropy (LSE). LSE performs similarly as model confidence metrics such as prediction probability and ensemble variance for out-of-sample test data, but it outperforms the other two metrics for out-of-distribution data, which have different distribution with the training data. By tuning the confidence tolerance of LSE, we showed that the performance of the static classifier can systematically improve even when the baseline performance is poor. More details please see our paper in JCTC (<https://pubs.acs.org/doi/abs/10.1021/acs.jctc.9b00057>).


Both the static classifier and LSE are implemented in molSimplify and are turned on by default when you generate a structure with molSimplify. The prediction probability, predicted class, and the LSE can be found in the report file (your\_structure\_name.report). For the tutorial of structure generation with molSimplify, please refer to <https://hjkgrp.mit.edu/content/molsimplify-tutorial-1-structure-generation>. Currently, two types of static classifiers are implemented, one for the geometry stability and the other for the spin square deviation (<S^2> -S(S+1)), to address two common failure modes mentioned above separately. An example command line input for a six-coordiantion iron water complex with oxidation II and high spin is


molsimplify -coord 6 -core fe -lig water -oxstate 2 -spin 5


We can find the predictions of the static classifiers in "fe\_oct\_2\_water\_6\_s\_5.report" as


sc\_label, 1
sc\_label\_trust, very high
geo\_LSE, 0.056454913968045105
geo\_prob, 0.8308638334274292
sc\_LSE, 0.0010312223992481981
geo\_label\_trust, very high
geo\_label, 1
sc\_prob, 0.7422247529029846
 
In the above output, spin contamination (sc) and geometry (geo) preedictions and confidence are denoted. In this case, both the geometry and electronic structure are predicted as good (label of 1) with very high confidence (LSE close to 0), which is expected. Please make sure that keras and  tensorflow are preinstalled in your conda environment to successfully activate static classifiers and other machine learning models built in molSimplify.
