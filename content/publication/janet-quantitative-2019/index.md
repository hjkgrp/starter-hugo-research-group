---
# Documentation: https://wowchemy.com/docs/managing-content/

title: A quantitative uncertainty metric controls error in neural network-driven chemical
  discovery
subtitle: ''
summary: ''
authors:
- Jon Paul Janet
- crduan
- Tzuhsiung Yang
- nandy
- admin
tags: []
categories: []
date: '2019-01-01'
lastmod: 2021-06-20T14:45:44-04:00
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
publishDate: '2021-06-21T01:48:19.018721Z'
publication_types:
- '2'
abstract: Machine learning (ML) models, such as artificial neural networks, have emerged
  as a complement to high-throughput screening, enabling characterization of new compounds
  in seconds instead of hours. The promise of ML models to enable large-scale chemical
  space exploration can only be realized if it is straightforward to identify when
  molecules and materials are outside the model's domain of applicability. Established
  uncertainty metrics for neural network models are either costly to obtain (e.g.,
  ensemble models) or rely on feature engineering (e.g., feature space distances),
  and each has limitations in estimating prediction errors for chemical space exploration.
  We introduce the distance to available data in the latent space of a neural network
  ML model as a low-cost, quantitative uncertainty metric that works for both inorganic
  and organic chemistry. The calibrated performance of this approach exceeds widely
  used uncertainty metrics and is readily applied to models of increasing complexity
  at no additional cost. Tightening latent distance cutoffs systematically drives
  down predicted model errors below training errors, thus enabling predictive error
  control in chemical discovery or identification of useful data points for active
  learning.
publication: '*Chem. Sci.*, **10**, 7913-7922 (2019)'
url_pdf: https://pubs.rsc.org/en/content/articlelanding/2019/sc/c9sc02298h
doi: 10.1039/C9SC02298H
---
