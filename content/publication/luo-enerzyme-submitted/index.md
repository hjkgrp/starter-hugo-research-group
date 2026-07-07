---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Enerzyme: A Framework for Efficient Training of Reactive Neural Network Potentials for Enzyme Catalysis with Application to Methyltransferases'
subtitle: ''
summary: ''
authors:
- weiliang
- admin

tags: []
categories: []
date: '2026-06-30'
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
- '3'
abstract: 'Quantum mechanical (QM) cluster models provide an effective framework for mechanistic studies of enzymatic reactions but remain computationally demanding. Neural network potentials (NNPs) offer a promising route to reduce this cost, but enzymes present challenges beyond small molecules, including large system sizes, implicit-solvent environments, substantial polarization, and charge transfer. Here, we present an integrated software framework for efficient NNP training for mechanistic studies of enzymes, demonstrated on QM cluster models of S-adenosyl-L-methionine-dependent methyltransferases (MTases). Our Enerzyme code introduces modular electrostatics-aware NNP architectures and combines automated QM-cluster construction with reactive dataset generation. The Enerzymette subpackage automates reaction pathway exploration at both NNP and DFT levels. We show that iterative flexible scans and nudged elastic band calculations impose stricter requirements on NNPs than conventional dataset metrics. Nevertheless, NNPs trained on fewer than 1,000 system-specific datapoints reproduce reaction energetics and transition-state structures for MTase clusters containing up to 545 atoms with near-chemical accuracy. Direct supervision of atomic charges and consistent dielectric screening substantially improve simulation stability and accuracy, while multitask-learned atomic charges capture charge transfer and polarization trends and provide chemically meaningful descriptors of reactivity. Finally, transferability across chemically diverse catechol O-methyltransferase substrates indicates that NNPs learn generalizable reactivity patterns as training data expand across multiple enzymes. Together, these results establish a foundation for accelerating enzyme mechanistic studies and guide future NNP development for biomolecular reactivity.'
publication: '*submitted*'
#doi: 10.1021/jacs.2c11858
links:
- name: arXiv
  url: https://arxiv.org/abs/2607.01362
---
