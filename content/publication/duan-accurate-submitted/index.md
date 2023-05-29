---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Accurate transition state generation with an object-aware equivariant elementary reaction diffusion model'
subtitle: ''
summary: ''
authors:
- crduan
- Yuanqi Du
- haojun
- admin
tags: []
categories: []
date: '2023-04-17'
lastmod: 2023-04-17T14:39:46-04:00
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
publishDate: '2023-04-17T18:39:46.489202Z'
publication_types:
- '3'
abstract: 'Transition state (TS) search is key in chemistry for elucidating reaction mechanisms and exploring reaction networks. The search for accurate 3D TS structures, however, requires numerous computationally intensive quantum chemistry calculations due to the complexity of potential energy surfaces. Here, we developed an object-aware SE(3) equivariant diffusion model that satisfies all physical symmetries and constraints for generating sets of structures - reactant, TS, and product - in an elementary reaction. Provided reactant and product, this model generates a TS structure in seconds instead of hours required when performing quantum chemistry-based optimizations. The generated TS structures achieve a median of 0.08 Å root mean square deviation compared to the true TS. With a confidence scoring model for uncertainty quantification, we approach an accuracy required for reaction rate estimation (2.6 kcal/mol) by only performing quantum chemistry-based optimizations on 14 percent of the most challenging reactions. We envision the proposed approach useful in constructing large reaction networks with unknown mechanisms.'
publication: '*submitted*'
links:
- name: arXiv
  url: https://arxiv.org/abs/2304.06174
---
