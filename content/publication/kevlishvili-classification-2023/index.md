---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Classification of Hemilabile Ligands Using Machine Learning
subtitle: ''
summary: ''
authors:
- iliak
- crduan
- admin
tags: []
categories: []
date: '2023-12-05'
lastmod: 2023-02-03T13:35:03-04:00
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
publishDate: '2023-02-03T17:35:02.766661Z'
publication_types:
- '2'
abstract: Hemilabile ligands have the capacity to partially disengage from a metal center, providing a strategy to balance stability and reactivity in catalysis, but they are not straightforward to identify. We identify ligands in the Cambridge Structural Database that have been crystallized with distinct denticities and are thus identifiable as hemilabile ligands. We implement a semi-supervised learning approach using a label-spreading algorithm to augment a small negative set that is supported by heuristic rules of ligand and metal co-occurrence. We show that a heuristic based on coordinating atom identity alone is not sufficient to identify whether a ligand is hemilabile, and our trained machine-learning classification models are instead needed to predict whether a bi-, tri-, or tetradentate ligand is hemilabile with high accuracy and precision. Feature importance analysis of our models shows that the second, third, and fourth coordination spheres all play important roles in ligand hemilability.
publication: '*J. Phys. Chem. Lett.*, **14**, 11100–11109 (2023)'
doi: 10.1021/acs.jpclett.3c02828
url_pdf: https://pubs.acs.org/doi/epdf/10.1021/acs.jpclett.3c02828
links:
- name: ChemRxiv
  url: https://doi.org/10.26434/chemrxiv-2023-66jqr-v2
---
