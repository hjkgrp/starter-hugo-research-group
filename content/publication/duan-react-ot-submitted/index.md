---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'React-OT: Optimal Transport for Generating Transition State in Chemical Reactions'
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
date: '2024-04-20'
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
- '3'
abstract: 'Transition states (TSs) are transient structures that are key in understanding reaction mechanisms and designing catalysts but challenging to be captured in experiments. Alternatively, many optimization algorithms have been developed to search for TSs computationally. Yet the cost of these algorithms driven by quantum chemistry methods (usually density functional theory) is still high, posing challenges for their applications in building large reaction networks for reaction exploration. Here we developed React-OT, an optimal transport approach for generating unique TS structures from reactants and products. React-OT generates highly accurate TS structures with a median structural root mean square deviation (RMSD) of 0.053Å and median barrier height error of 1.06 kcal/mol requiring only 0.4 second per reaction. The RMSD and barrier height error is further improved by roughly 25% through pretraining React-OT on a large reaction dataset obtained with a lower level of theory, GFN2-xTB. We envision the great accuracy and fast inference of React-OT useful in targeting TSs when exploring chemical reactions with unknown mechanisms.'
publication: '*submitted*'
#doi: 10.1021/jacs.2c11858
links:
- name: arXiv
  url: https://arxiv.org/abs/2404.13430
---
