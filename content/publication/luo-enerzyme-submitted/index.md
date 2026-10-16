---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Enerzyme: An Efficient Reactive Neural Network Potential Training Framework for Enzyme Cluster Models with Application to Methyltransferases'
subtitle: ''
summary: ''
authors:
- weiliang
- admin

tags: []
categories: []
date: '2026-10-13'
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
abstract: 'Quantum mechanical (QM) cluster models provide an effective framework for mechanistic studies of enzymatic reactions but QM calculations remain computationally demanding. Neural network potentials (NNPs) offer a promising route to reduce their cost, but enzymes introduce new challenges not faced by NNPs for small molecules, including large system sizes, the need for inclusion of solvent environments, substantial polarization, and charge transfer. Here, we demonstrate an integrated software framework for efficient training of NNPs for mechanistic study of enzymes, with demonstrations on QM-cluster models of S-adenosyl-l-methionine-dependent methyltransferases (MTases). Our Enerzyme code introduces modular, electrostatics-aware NNP architectures and combines automated QM-cluster construction with reactive dataset generation. The Enerzymette subpackage also automates reaction pathway exploration at both NNP and DFT levels of theory. We show that iterative flexible scans and nudged elastic band calculations impose stricter requirements on NNPs than conventionally employed dataset metrics. Nevertheless, we develop an approach to train NNPs on fewer than 1,000 system-specific data points to reproduce reaction energetics and transition-state structures on MTase clusters containing up to 545 atoms, approaching chemical accuracy with respect to the reference. We show that direct supervision of atomic charges and alignment of dielectric screening with QM-cluster calculations substantially improve simulation stability and accuracy and that multitask-learned atomic charges predict correct charge transfer and polarization trends and provide chemically meaningful descriptors of reactivity. Furthermore, we demonstrate transferability across chemically diverse catechol O-methyltransferase substrates, indicating NNPs learn generalizable reactivity patterns as training data is expanded across multiple enzymes. Together, these results establish a foundation for accelerating enzyme mechanistic studies and provide insights for future NNP development for biomolecular reactivity.'
publication: '*J. Chem. Theory Comput.*, **in press** '
doi: 10.1021/acs.jctc.6c01330
links:
- name: arXiv
  url: https://arxiv.org/abs/2607.01362
---
