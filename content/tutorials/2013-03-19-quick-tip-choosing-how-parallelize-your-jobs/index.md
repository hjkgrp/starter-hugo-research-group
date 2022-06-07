---
title: "Quick tip: Choosing how to parallelize your jobs"
subtitle:
aliases: /content/quick-tip-choosing-how-parallelize-your-jobs
 

# Summary for listings and search engines
summary: 

# Link this post with a project
projects: []

# Date published
date: 2013-03-19

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
In today’s quick tip, we’ll go over why and how you may want to parallelize the jobs that you run.  There are a number of reasons why you may want to parallelize the jobs that you are running.  


 


**Why to parallelize:** Namely, if your job is large enough, it may simply not fit on a single computer or processor.  Additionally, you may not want to wait as long as it will take for the job to run in serial.  It’s particularly beneficial to parallelize if you’re able to divide up your calculation and minimize communication. We’ll get into that shortly. Finally, some supercomputing resources give a bonus priority to large jobs. You may wish to parallelize in that case just to get your job to run faster.


 


**Why not parallelize?:** In some cases, you’re only trying to do many small calculations. This in effect is a form of parallelization to send out all these small jobs, but you are effectively only using a single processor to do a single calculation.  Additionally, you may not have a parallel copy of your code, the communication between nodes on your cluster may be slow, or if you are thinking of using another code besides Quantum-ESPRESSO, you may lack a parallel license for the code in question.


 


**How to parallelize in Quantum-ESPRESSO:**


The main issue in choosing a parallelization scheme is to identify whether you can parallelize your job in a way that minimizes communication.


 


1. NEB/string images: each image in a path-based method is a single point energy. The downside of parallelizing across images is that images close to the transition state often take considerably longer than images near the endpoints.  Generally, you don’t want to parallelize a pool for each image, maybe put two images on each pool. e.g. for 8 images, `neb.x -nimages 4`.

 


2. k points: Generally, communication required between different pools of processors for different kpoints is minimal.  You should take advantage of any k-point parallelization you can obtain for your system. Keep in mind that if you specify, e.g. a 4x4x4 mesh, you would expect to have 64 kpoints. However, through symmetry that total number of kpoints will be reduced.  If you’re not sure how many unique k points will be found for your simulation, try running your calculation just for a few seconds and check out the header to see what symmetry is found in your simulation. For instance, 64 kpoints might be 27 unique kpoints with symmetry. To run, try breaking that into 3 pools for kpoints: `pw.x -npool 3 < input > output`. It’s important to have at least 1 kpoint per pool.

 

3. r+g parallelization: Within a single k-point or if you are running a gamma point calculation, you can straightforwardly parallelize over the total number of FFT planes in your calculation. This is determined in part by the size of your cell and the cutoff you are using for your calculation. You can find out how many smooth planes are needed for your calculation at the start under the header “Parallelization info”.  Run for a few seconds and you should find this info.  Be sure to not run with more processors than you have smooth planes in your calculation!  The only way around this is to try out using task groups.  The full command, imagining above that you have 27 kpoints, parallelizing over 3 pools, and you have 64 smooth planes, then you can use a total of 64x3 = 192 processors with a command like:`mpirun -np 192 pw.x -npool 3 < input > output`.

 


4. further parallelization: task groups can be used to divide up processors for massive parallelization in cases where you want to use more processors than you have smooth planes (`-ntg`) or you can split up how diagonalization is carried out (`-ndiag`).

 


I hope you found this parallelization quick tip helpful. If you have any questions, please [email me](mailto:hjkulik@mit.edu?subject=Questions%20about%20parallelization%20quick%20tip "mailto:hjkulik@mit.edu?subject=Questions about parallelization quick tip")!


