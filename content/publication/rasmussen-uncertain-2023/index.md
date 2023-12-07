---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Uncertain of uncertainties? A comparison of uncertainty quantification metrics for chemical data sets'
subtitle: ''
summary: ''
authors:
- Maria H. Rasmussen
- crduan
- admin
- Jan Halborg Jensen
tags: []
categories: []
date: '2023-11-28'
lastmod: 2023-06-08T13:54:08-04:00
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
publishDate: '2023-06-08T17:54:08.046005Z'
publication_types:
- '2'
abstract: With the increasingly more important role of machine learning (ML) models in chemical research, the need for putting a level of confidence to the model predictions naturally arises. Several methods for obtaining uncertainty estimates have been proposed in recent years but consensus on the evaluation of these have yet to be established and different studies on uncertainties generally uses different metrics to evaluate them. We compare three of the most popular validation metrics (Spearman’s rank correlation coefficient, the negative log likelihood (NLL) and the miscalibration area) to the error-based calibration introduced by Levi et al. (Sensors 2022, 22, 5540). Importantly, metrics such as the negative log likelihood (NLL) and Spearman’s rank correlation coefficient bear little information in themselves. We therefore introduce reference values obtained through errors simulated directly from the uncertainty distribution. The different metrics target different properties and we show how to interpret them, but we generally find the best overall validation to be done based on the error-based calibration plot introduced by Levi et al. Finally, we illustrate the sensitivity of ranking-based methods (e.g. Spearman’s rank correlation coefficient) towards test set design by using the same toy model on two different test sets and obtaining vastly different metrics (0.05 vs. 0.65).
publication: '*J. Cheminform.*, **in press**'
#doi: 10.1021/jacs.2c11858
links:
- name: ChemRxiv
  url: https://doi.org/10.26434/chemrxiv-2023-w93dm
---
