---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Optimal transport for generating transition states in chemical reactions'
subtitle: ''
summary: ''
authors:
- Chenru Duan
- Guan-Horng Liu
- Yuanqi Du
- Tianrong Chen
- Qiyuan Zhao
- haojun
- Carla P. Gomes
- Evangelos A. Theodorou
- admin
tags: []
categories: []
date: '2025-04-23'
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
abstract: 'Transition states (TSs) are transient structures that are key to understanding reaction mechanisms and designing catalysts but challenging to capture in experiments. Many optimization algorithms have been developed to search for TSs computationally. Yet, the cost of these algorithms driven by quantum chemistry methods (usually density functional theory) is still high, posing challenges for their applications in building large reaction networks for reaction exploration. Here we developed React-OT, an optimal transport approach for generating unique TS structures from reactants and products. React-OT generates highly accurate TS structures with a median structural root mean square deviation of 0.053 Å and median barrier height error of 1.06 kcal mol−1 requiring only 0.4 s per reaction. The root mean square deviation and barrier height error are further improved by roughly 25% through pretraining React-OT on a large reaction dataset obtained with a lower level of theory, GFN2-xTB. We envision that the remarkable accuracy and rapid inference of React-OT will be highly useful when integrated with the current high-throughput TS search workflow. This integration will facilitate the exploration of chemical reactions with unknown mechanisms.'
publication: '*Nat. Mach. Intell.*, **7**, 615–626 (2025)'
doi: 10.1038/s42256-025-01010-0
url_pdf: https://www.nature.com/articles/s42256-025-01010-0.pdf
links:
- name: arXiv
  url: https://arxiv.org/abs/2404.13430
---
