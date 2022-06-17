---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Accelerating Chemical Discovery with Machine Learning: Simulated Evolution
  of Spin Crossover Complexes with an Artificial Neural Network'
subtitle: ''
summary: ''
authors:
- Jon Paul Janet
- Lydia Chan
- admin
tags: []
categories: []
date: '2018-03-01'
lastmod: 2021-06-20T14:45:46-04:00
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
publishDate: '2021-06-21T01:48:20.932316Z'
publication_types:
- '2'
abstract: Machine learning (ML) has emerged as a powerful complement to simulation
  for materials discovery by reducing time for evaluation of energies and properties
  at accuracy competitive with first-principles methods. We use genetic algorithm
  (GA) optimization to discover unconventional spin-crossover complexes in combination
  with efficient scoring from an artificial neural network (ANN) that predicts spin-state
  splitting of inorganic complexes. We explore a compound space of over 5600 candidate
  materials derived from eight metal/oxidation state combinations and a 32-ligand
  pool. We introduce a strategy for error-aware ML-driven discovery by limiting how
  far the GA travels away from the nearest ANN training points while maximizing property
  (i.e., spin-splitting) fitness, leading to discovery of 80% of the leads from full
  chemical space enumeration. Over a 51-complex subset, average unsigned errors (4.5
  kcal/mol) are close to the ANN’s baseline 3 kcal/mol error. By obtaining leads from
  the trained ANN within seconds rather than days from a DFT-driven GA, this strategy
  demonstrates the power of ML for accelerating inorganic material discovery.
publication: '*J. Phys. Chem. Lett.*, **9**, 1064-1071 (2018)'
url_pdf: https://doi.org/10.1021/acs.jpclett.8b00170
doi: 10.1021/acs.jpclett.8b00170
---
