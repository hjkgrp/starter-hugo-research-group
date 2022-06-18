---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Semi-supervised Machine Learning Enables the Robust Detection of Multireference
  Character at Low Cost
subtitle: ''
summary: ''
authors:
- crduan
- Fang Liu
- nandy
- admin
tags: []
categories: []
date: '2020-08-01'
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
publishDate: '2021-06-21T01:48:13.839941Z'
publication_types:
- '2'
abstract: Multireference (MR) diagnostics are common tools for identifying strongly
  correlated electronic structure that makes single-reference (SR) methods (e.g.,
  density functional theory or DFT) insufficient for accurate property prediction.
  However, MR diagnostics typically require computationally demanding correlated wave
  function theory (WFT) calculations, and diagnostics often disagree or fail to predict
  MR effects on properties. To overcome these challenges, we introduce a semi-supervised
  machine learning (ML) approach with virtual adversarial training (VAT) of an MR
  classifier using 15 WFT and DFT MR diagnostics as inputs. In semi-supervised learning,
  only the most extreme SR or MR points are labeled, and the remaining point labels
  are learned. The resulting VAT model outperforms the alternatives, as quantified
  by the distinct property distributions of SR- and MR-classified molecules. To reduce
  the cost of generating inputs to the VAT model, we leverage the VAT model’s robustness
  to noisy inputs by replacing WFT MR diagnostics with regression predictions in an
  MR decision engine workflow that preserves excellent performance. We demonstrate
  the transferability of our approach to larger molecules and those with distinct
  chemical composition from the training set. This MR decision engine demonstrates
  promise as a low-cost, high-accuracy approach to the automatic detection of strong
  correlation for predictive high-throughput screening.
publication: '*J. Phys. Chem. Lett.*, **11**, 6640-6648 (2020)'
url_pdf: https://doi.org/10.1021/acs.jpclett.0c02018
doi: 10.1021/acs.jpclett.0c02018
---
