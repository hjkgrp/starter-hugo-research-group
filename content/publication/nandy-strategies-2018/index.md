---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Strategies and Software for Machine Learning Accelerated Discovery in Transition
  Metal Chemistry
subtitle: ''
summary: ''
authors:
- nandy
- crduan
- Jon Paul Janet
- Stefan Gugler
- admin
tags: []
categories: []
date: '2018-10-01'
lastmod: 2021-06-20T14:45:45-04:00
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
publishDate: '2021-06-21T01:48:20.136919Z'
publication_types:
- '2'
abstract: Machine learning the electronic structure of open shell transition metal
  complexes presents unique challenges, including robust and automated data set generation.
  Here, we introduce tools that simplify data acquisition from density functional
  theory (DFT) and validation of trained machine learning models using the molSimplify
  automatic design (mAD) workflow. We demonstrate this workflow by training and comparing
  the performance of LASSO, kernel ridge regression (KRR), and artificial neural network
  (ANN) models using heuristic, topological revised autocorrelation (RAC) descriptors
  we have recently introduced for machine learning inorganic chemistry. On a series
  of open shell transition metal complexes, we evaluate set aside test errors of these
  models for predicting the HOMO level and HOMO–LUMO gap. The best performing models
  are ANNs, which show 0.15 and 0.25 eV test set mean absolute errors on the HOMO
  level and HOMO–LUMO gap, respectively. Poor performing KRR models using the full
  153-feature RAC set are improved to nearly the same performance as the ANNs when
  trained on down-selected subsets of 20–30 features. Analysis of the essential descriptors
  for HOMO level and HOMO–LUMO gap prediction as well as comparison to subsets previously
  obtained for other properties reveal the paramount importance of nonlocal, steric
  properties in determining frontier molecular orbital energetics. We demonstrate
  our model performance on diverse complexes and in the discovery of molecules with
  target HOMO–LUMO gaps from a large 15,000 molecule design space in minutes rather
  than days that full DFT evaluation would require.
publication: '*Ind. Eng. Chem. Res.*, **57**, 13973-13986 (2018)'
url_pdf: https://doi.org/10.1021/acs.iecr.8b04015
doi: 10.1021/acs.iecr.8b04015
---
