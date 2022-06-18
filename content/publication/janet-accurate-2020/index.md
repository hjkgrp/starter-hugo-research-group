---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Accurate Multiobjective Design in a Space of Millions of Transition Metal Complexes
  with Neural-Network-Driven Efficient Global Optimization
subtitle: ''
summary: ''
authors:
- Jon Paul Janet
- Sahasrajit Ramesh
- crduan
- admin
tags: []
categories: []
date: '2020-04-01'
lastmod: 2021-06-20T14:45:41-04:00
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
publishDate: '2021-06-21T01:48:15.037248Z'
publication_types:
- '2'
abstract: The accelerated discovery of materials for real world applications requires
  the achievement of multiple design objectives. The multidimensional nature of the
  search necessitates exploration of multimillion compound libraries over which even
  density functional theory (DFT) screening is intractable. Machine learning (e.g.,
  artificial neural network, ANN, or Gaussian process, GP) models for this task are
  limited by training data availability and predictive uncertainty quantification
  (UQ). We overcome such limitations by using efficient global optimization (EGO)
  with the multidimensional expected improvement (EI) criterion. EGO balances exploitation
  of a trained model with acquisition of new DFT data at the Pareto front, the region
  of chemical space that contains the optimal trade-off between multiple design criteria.
  We demonstrate this approach for the simultaneous optimization of redox potential
  and solubility in candidate M(II)/M(III) redox couples for redox flow batteries
  from a space of 2.8 M transition metal complexes designed for stability in practical
  redox flow battery (RFB) applications. We show that a multitask ANN with latent-distance-based
  UQ surpasses the generalization performance of a GP in this space. With this approach,
  ANN prediction and EI scoring of the full space are achieved in minutes. Starting
  from ca. 100 representative points, EGO improves both properties by over 3 standard
  deviations in only five generations. Analysis of lookahead errors confirms rapid
  ANN model improvement during the EGO process, achieving suitable accuracy for predictive
  design in the space of transition metal complexes. The ANN-driven EI approach achieves
  at least 500-fold acceleration over random search, identifying a Pareto-optimal
  design in around 5 weeks instead of 50 years.
publication: '*ACS Cent. Sci.*, **6**, 513-524 (2020)'
url_pdf: https://doi.org/10.1021/acscentsci.0c00026
doi: 10.1021/acscentsci.0c00026
---
