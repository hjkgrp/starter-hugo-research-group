---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Quantum Chemistry for Solvated Molecules on Graphical Processing Units Using
  Polarizable Continuum Models
subtitle: ''
summary: ''
authors:
- Fang Liu
- Nathan Luehr
- admin
- Todd J. Martínez
tags: []
categories: []
date: '2015-07-01'
lastmod: 2021-06-20T14:45:51-04:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2021-06-21T01:48:27.756130Z'
publication_types:
- '2'
abstract: 'The conductor-like polarization model (C-PCM) with switching/Gaussian smooth
  discretization is a widely used implicit solvation model in chemical simulations.
  However, its application in quantum mechanical calculations of large-scale biomolecular
  systems can be limited by computational expense of both the gas phase electronic
  structure and the solvation interaction. We have previously used graphical processing
  units (GPUs) to accelerate the first of these steps. Here, we extend the use of
  GPUs to accelerate electronic structure calculations including C-PCM solvation.
  Implementation on the GPU leads to significant acceleration of the generation of
  the required integrals for C-PCM. We further propose two strategies to improve the
  solution of the required linear equations: a dynamic convergence threshold and a
  randomized block-Jacobi preconditioner. These strategies are not specific to GPUs
  and are expected to be beneficial for both CPU and GPU implementations. We benchmark
  the performance of the new implementation using over 20 small proteins in solvent
  environment. Using a single GPU, our method evaluates the C-PCM related integrals
  and their derivatives more than 10× faster than that with a conventional CPU-based
  implementation. Our improvements to the linear solver provide a further 3× acceleration.
  The overall calculations including C-PCM solvation require, typically, 20–40% more
  effort than that for their gas phase counterparts for a moderate basis set and molecule
  surface discretization level. The relative cost of the C-PCM solvation correction
  decreases as the basis sets and/or cavity radii increase. Therefore, description
  of solvation with this model should be routine. We also discuss applications to
  the study of the conformational landscape of an amyloid fibril.'
publication: '*J. Chem. Theory Comput.*, **11**, 3131-3144 (2015)'
url_pdf: https://doi.org/10.1021/acs.jctc.5b00370
doi: 10.1021/acs.jctc.5b00370
---
