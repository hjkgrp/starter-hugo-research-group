---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Robust Generative Transition State Models for Unseen Chemistry' 
subtitle: ''
summary: ''
authors:
- samirdar
- jwt
- weiliang
- Johannes Kästner
- Mathias Niepert
- admin

tags: []
categories: []
date: '2026-08-12'
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
abstract: 'Transition states (TSs) govern the rates and outcomes of chemical reactions, making their accurate prediction a central challenge in computational chemistry. Although recent machine learning models achieve near-chemical accuracy in the prediction of TS structures and the associated reaction barriers for small organic reactions, their ability to generalize beyond the training domain remains largely unexplored. Here we introduce targeted benchmarks to probe chemical and structural novelty in generative TS prediction. Building on Transition1x, a large-scale dataset of reactions involving small organic molecules, we curate extensions incorporating controlled elemental substitutions and diverse transition metal complexes (TMCs), which reveal fundamental limitations of generative models in the generalization to previously unseen elements. To address this challenge, we introduce a self-supervised pretraining strategy based on equilibrium conformers that exposes generative TS models to novel chemical environments before targeted fine-tuning. Across the proposed benchmarks, self-supervised pretraining substantially improves TS prediction for previously unseen systems, lowering the median root-mean-square deviation of TS geometries on Transition1x-TMC reactions and reducing fine-tuning data requirements, enabling reliable performance even in low-data regimes.'
publication: '*Nat. Comput. Sci.*, **in press**'
doi: https://doi.org/10.1038/s43588-026-01034-5
url_pdf: https://www.nature.com/articles/s43588-026-01034-5.pdf
links:
- name: arXiv
  url: https://arxiv.org/abs/2601.16469
---
