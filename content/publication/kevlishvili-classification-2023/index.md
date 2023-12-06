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
date: '2023-10-18'
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
- '3'
abstract: Discovery of hemilabile ligands that optimally balance reactivity and stability is important for identifying novel catalyst structures. We design a workflow for identifying ligands in the Cambridge Structural Database (CSD) that have been crystalized with distinct denticities and are thus identifiable as hemilabile ligands. To overcome the difficulty of identifying negative example, non-hemilabile ligands in our data set, we implement a semi-supervised learning approach using a label-spreading algorithm together with a set of heuristic rules based on ligand frequency of appearance. We show that a heuristic based on coordinating atom identity alone is not sufficient to identify whether a ligand is hemilabile and our trained machine-learning classification models are instead needed to predict whether a bi-, tri-, or tetradentate ligand is hemilabile with high accuracy and precision. We gain deeper insight into the factors that govern ligand hemilability by conducting feature importance analysis on our models, finding that the second, third, and fourth coordination spheres all play an important role in ligand hemilability.
publication: '*submitted*'
#doi: 10.1021/acscatal.2c06241
#url_pdf: https://doi.org/10.1021/acscatal.2c06241
links:
- name: ChemRxiv
  url: https://doi.org/10.26434/chemrxiv-2023-66jqr-v2
---
