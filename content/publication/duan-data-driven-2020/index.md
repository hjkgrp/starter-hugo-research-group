---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Data-Driven Approaches Can Overcome the Cost–Accuracy Trade-Off in Multireference
  Diagnostics
subtitle: ''
summary: ''
authors:
- crduan
- Fang Liu
- nandy
- admin
tags: []
categories: []
date: '2020-07-01'
lastmod: 2021-06-20T14:45:40-04:00
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
publishDate: '2021-06-21T01:48:14.084320Z'
publication_types:
- '2'
abstract: High-throughput computational screening typically employs methods (i.e.,
  density functional theory or DFT) that can fail to describe challenging molecules,
  such as those with strongly correlated electronic structure. In such cases, multireference
  (MR) correlated wavefunction theory (WFT) would be the appropriate choice but remains
  more challenging to carry out and automate than single-reference (SR) WFT or DFT.
  Numerous diagnostics have been proposed for identifying when MR character is likely
  to have an effect on the predictive power of SR calculations, but conflicting conclusions
  about diagnostic performance have been reached on small data sets. We compute 15
  MR diagnostics, ranging from affordable DFT-based to more costly MR-WFT-based diagnostics,
  on a set of 3165 equilibrium and distorted small organic molecules containing up
  to six heavy atoms. Conflicting MR character assignments and low pairwise linear
  correlations among diagnostics are also observed over this set. We evaluate the
  ability of existing diagnostics to predict the percent recovery of the correlation
  energy, %Ecorr. None of the DFT-based diagnostics are nearly as predictive of %Ecorr
  as the best WFT-based diagnostics. To overcome the limitation of this cost–accuracy
  trade-off, we develop machine learning (ML, i.e., kernel ridge regression) models
  to predict WFT-based diagnostics from a combination of DFT-based diagnostics and
  a new, size-independent 3D geometric representation. The ML-predicted diagnostics
  correlate as well with MR effects as their computed (i.e., with WFT) values, significantly
  improving over the DFT-based diagnostics on which the models were trained. These
  ML models thus provide a promising approach to improve upon DFT-based diagnostic
  accuracy while remaining suitably low cost for high-throughput screening.
publication: '*J. Chem. Theory Comput.*, **16**, 4373-4387 (2020)'
url_pdf: https://doi.org/10.1021/acs.jctc.0c00358
doi: 10.1021/acs.jctc.0c00358
---
