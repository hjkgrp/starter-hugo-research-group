---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Enhancing materials discovery with valence-constrained design in generative modeling' 
subtitle: ''
summary: ''
authors:
- Mouyang Cheng
- weiliang
- Hao Tang
- Bowen Yu
- Yongqiang Cheng
- Weiwei Xie
- Ju Li
- admin
- Mingda Li

tags: []
categories: []
date: '2026-08-26'
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
abstract: 'Diffusion-based deep generative models have emerged as powerful tools for inverse materials design. Yet many existing approaches overlook essential chemical constraints, such as oxidation-state balance, which can lead to chemically invalid structures. Here we introduce ‘crystal generator with valence-constrained design’ (CrysVCD), a modular framework that integrates chemical rules directly into the generative process. CrysVCD first uses a transformer-based elemental language model to generate valence-balanced compositions, followed by a diffusion model to generate crystal structures. The valence constraint enables orders-of-magnitude more efficient chemical valence checking compared with pure data-driven approaches with post-screening. When fine-tuned on stability metrics, CrysVCD achieves 85% metastability (E<sub>hull</sub> < 0.1 eV per atom) and 68% phonon stability. Moreover, CrysVCD supports conditional generation of functional materials, enabling discovery of candidates such as high thermal conductivity semiconductors and high dielectric constant (high-κ) materials. Designed as a general-purpose plugin, CrysVCD can be integrated into diverse generative pipelines to promote chemical validity, offering a reliable, scientifically grounded path for materials discovery.'
publication: '*Nat. Comput. Sci.*, **in press**'
doi: 10.1038/s43588-026-01037-2
url_pdf: https://www.nature.com/articles/s43588-026-01037-2.pdf
links:
- name: arXiv
  url: https://arxiv.org/abs/2507.19799
---
