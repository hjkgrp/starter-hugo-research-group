---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Detection of multi-reference character imbalances enables a transfer learning
  approach for chemical discovery with coupled cluster accuracy at DFT cost
subtitle: ''
summary: ''
authors:
- crduan
- dbkchu
- nandy
- admin
tags: []
categories: []
date: '2022-01-01'
lastmod: 2022-05-09T10:11:43-04:00
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
publishDate: '2022-05-09T14:11:43.445826Z'
publication_types:
- '2'
abstract: Appropriately identifying and treating molecules and materials with significant
  multi-reference (MR) character is crucial for achieving high data fidelity in virtual
  high-throughput screening (VHTS). Despite development of numerous MR diagnostics,
  the extent to which a single value of such a diagnostic indicates the MR effect
  on a chemical property prediction is not well established. We evaluate MR diagnostics
  for over 10 000 transition-metal complexes (TMCs) and compare to those for organic
  molecules. We observe that only some MR diagnostics are transferable from one chemical
  space to another. By studying the influence of MR character on chemical properties
  (i.e., MR effect) that involve multiple potential energy surfaces (i.e., adiabatic
  spin splitting, ΔEH–L, and ionization potential, IP), we show that differences in
  MR character are more important than the cumulative degree of MR character in predicting
  the magnitude of an MR effect. Motivated by this observation, we build transfer
  learning models to predict CCSD(T)-level adiabatic ΔEH–L and IP from lower levels
  of theory. By combining these models with uncertainty quantification and multi-level
  modeling, we introduce a multi-pronged strategy that accelerates data acquisition
  by at least a factor of three while achieving coupled cluster accuracy (i.e., to
  within 1 kcal mol−1 MAE) for robust VHTS.
publication: '*Chem. Sci.*, **13**, 4962-4971 (2022)'
doi: 10.1039/D2SC00393G
url_pdf: https://pubs.rsc.org/en/Content/ArticleLanding/2022/SC/D2SC00393G
---
