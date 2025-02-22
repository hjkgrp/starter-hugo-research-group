---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Many-body expansion based machine learning models for octahedral transition metal complexes
subtitle: ''
summary: ''
authors:
- rameyer
- dbkchu
- admin

tags: []
categories: []
date: '2025-01-06'
lastmod: 
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
publishDate: 
publication_types:
- '2'
abstract: 'Graph-based machine learning (ML) models for material properties show great potential to accelerate virtual high-throughput screening of large chemical spaces. However, in their simplest forms, graph-based models do not include any 3D information and are unable to distinguish stereoisomers such as those arising from different orderings of ligands around a metal center in coordination complexes. In this work we present a modification to revised autocorrelation descriptors, a molecular graph featurization method, for predicting spin state dependent properties of octahedral transition metal complexes (TMCs). Inspired by analytical semi-empirical models for TMCs, the new modeling strategy is based on the many-body expansion (MBE) and allows one to tune the captured stereoisomer information by changing the truncation order of the MBE. We present the necessary modifications to include this approach in two commonly used ML methods, kernel ridge regression and feed-forward neural networks. On a test set composed of all possible isomers of binary TMCs, the best MBE models achieve mean absolute errors (MAEs) of 2.75 kcal mol<sup>−1</sup> on spin-splitting energies and 0.26 eV on frontier orbital energy gaps, a 30%–40% reduction in error compared to models based on our previous approach. We also observe improved generalization to previously unseen ligands where the best-performing models exhibit MAEs of 4.00 kcal mol<sup>−1</sup> (i.e. a 0.73 kcal mol<sup>−1</sup> reduction) on the spin-splitting energies and 0.53 eV (i.e. a 0.10 eV reduction) on the frontier orbital energy gaps. Because the new approach incorporates insights from electronic structure theory, such as ligand additivity relationships, these models exhibit systematic generalization from homoleptic to heteroleptic complexes, allowing for efficient screening of TMC search spaces.'
publication: '*Mach. Learn.: Sci. Technol.*, **5**, 045080 (2024)'
doi: 10.1088/2632-2153/ad9f22
url_pdf: https://iopscience.iop.org/article/10.1088/2632-2153/ad9f22/pdf
links:
- name: arXiv
  url: https://arxiv.org/abs/2410.09659
---
