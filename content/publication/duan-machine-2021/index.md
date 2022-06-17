---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Machine learning to tame divergent density functional approximations a new
  path to consensus materials design principles
subtitle: ''
summary: ''
authors:
- crduan
- Shuxin Chen
- Michael G. Taylor
- Fang Liu
- admin
tags: []
categories: []
date: '2021-01-01'
lastmod: 2022-05-08T21:33:22-04:00
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
publishDate: '2022-05-09T01:33:22.597404Z'
publication_types:
- '2'
abstract: Virtual high-throughput screening (VHTS) with density functional theory
  (DFT) and machine-learning (ML)-acceleration is essential in rapid materials discovery.
  By necessity, efficient DFT-based workflows are carried out with a single density
  functional approximation (DFA). Nevertheless, properties evaluated with different
  DFAs can be expected to disagree for cases with challenging electronic structure
  (e.g., open-shell transition-metal complexes, TMCs) for which rapid screening is
  most needed and accurate benchmarks are often unavailable. To quantify the effect
  of DFA bias, we introduce an approach to rapidly obtain property predictions from
  23 representative DFAs spanning multiple families, “rungs” (e.g., semi-local to
  double hybrid) and basis sets on over 2000 TMCs. Although computed property values
  (e.g., spin state splitting and frontier orbital gap) differ by DFA, high linear
  correlations persist across all DFAs. We train independent ML models for each DFA
  and observe convergent trends in feature importance, providing DFA-invariant, universal
  design rules. We devise a strategy to train artificial neural network (ANN) models
  informed by all 23 DFAs and use them to predict properties (e.g., spin-splitting
  energy) of over 187k TMCs. By requiring consensus of the ANN-predicted DFA properties,
  we improve correspondence of computational lead compounds with literature-mined,
  experimental compounds over the typically employed single-DFA approach.
publication: '*Chem. Sci.*, **12**, 13021-13036 (2021)'
doi: 10.1039/D1SC03701C
url_pdf: https://pubs.rsc.org/en/Content/ArticleLanding/2021/SC/D1SC03701C
---
