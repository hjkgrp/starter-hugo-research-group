---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Insights into the deviation from piecewise linearity in transition metal complexes from supervised machine learning models
subtitle: ''
summary: ''
authors:
- yaelc
- nandy
- crduan
- admin
tags: []
categories: []
date: submitted-01-01
lastmod: 2023-01-13T14:39:46-04:00
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
publishDate: '2023-01-13T18:39:46.489202Z'
publication_types:
- '2'
abstract: 'Virtual high-throughput screening (VHTS) and machine learning (ML) with density functional theory (DFT) suffer from inaccuracies from the underlying density functional approximation (DFA). Many of these inaccuracies can be traced to the lack of derivative discontinuity that leads to a curvature in the energy with electron addition or removal. Over a dataset of nearly one thousand transition metal complexes typical of VHTS applications, we computed and analyzed the average curvature (i.e., deviation from piecewise linearity) for 23 density functional approximations spanning multiple rungs of "Jacobs ladder". While we observe the expected dependence of the curvatures on HF exchange, we note limited correlation of curvature values between different rungs of "Jacobs ladder". We train ML models (i.e., artificial neural networks or ANNs) to predict the curvature and the associated frontier orbital energies for each of these 23 functionals and then interpret differences in curvature among the different DFAs through analysis of the ML models. Notably, we observe spin to play a much more important role in determining the curvature of range-separated and double hybrids in comparison to semi-local functionals, explaining why curvature values are weakly correlated between these and other families of functionals. Over a space of 187.2k hypothetical compounds, we use our ANNs to pinpoint DFAs for which representative transition metal complexes have near-zero curvature with low uncertainty, demonstrating an approach to accelerate screening of complexes with targeted optical gaps.'
publication: '*Physc. Chem. Chem. Phys.*, in press'
---
