---
# Documentation: https://wowchemy.com/docs/managing-content/

title: A Transferable Recommender Approach for Selecting the Best Density Functional
  Approximations in Chemical Discovery
subtitle: ''
summary: ''
authors:
- crduan
- nandy
- rameyer
- narunach
- admin
tags:
- Computer Science - Machine Learning
- Condensed Matter - Materials Science
- Physics - Chemical Physics
categories: []
date: 2023-01-26
lastmod: 2023-01-26T14:44:25-05:00
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
publishDate: '2023-01-26T19:44:24.480889Z'
publication_types:
- '2'
abstract: Approximate density functional theory (DFT) has become indispensable owing
  to its cost-accuracy trade-off in comparison to more computationally demanding but
  accurate correlated wavefunction theory. To date, however, no single density functional
  approximation (DFA) with universal accuracy has been identified, leading to uncertainty
  in the quality of data generated from DFT. With electron density fitting and transfer
  learning, we build a DFA recommender that selects the DFA with the lowest expected
  error with respect to gold standard but cost-prohibitive coupled cluster theory
  in a system-specific manner. We demonstrate this recommender approach on vertical
  spin-splitting energy evaluation for challenging transition metal complexes. Our
  recommender predicts top-performing DFAs and yields excellent accuracy (ca. 2 kcal/mol)
  for chemical discovery, outperforming both individual transfer learning models and
  the single best functional in a set of 48 DFAs. We demonstrate the transferability
  of the DFA recommender to experimentally synthesized compounds with distinct chemistry.
publication: '*Nat. Comput. Sci.*, **3**, 38-47 (2023)'
doi: 10.1038/s43588-022-00384-0
url_pdf: https://doi.org/10.1038/s43588-022-00384-0
links:
- name: arXiv
  url: https://arxiv.org/abs/2207.10747
---
