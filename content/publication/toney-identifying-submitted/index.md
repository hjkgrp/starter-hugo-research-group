---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Identifying Dynamic Metal–Ligand Coordination Modes with Ensemble Learning'
subtitle: ''
summary: ''
authors:
- jwt
- rolan701
- aarongar
- iliak
- admin

tags: []
categories: []
date: '2025-08-20'
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
abstract: 'Knowledge of how a ligand coordinates a metal is essential for mechanistic and data-driven studies of transition metal complexes (TMCs), but most analyses assume a single binding interaction for a given metal–ligand pair. This assumption neglects hemilabile ligands defined by dynamic coordination and highly relevant in catalysis. In this work, we curate datasets of hemilabile and nonhemilabile ligands from experimentally characterized structures in the Cambridge Structural Database, analyze trends in observed coordination modes, and introduce four new exhaustive and mutually exclusive classes of hemilability. Using these labeled datasets, we train graph neural networks to classify hemilabile ligands with high accuracy, precision, and recall and develop an ensemble algorithm which predicts primary and alternative chemically plausible coordination modes from SMILES strings in an end-to-end fashion. We demonstrate the utility of our algorithm by generating novel TMCs in predicted coordination modes and calculating the corresponding energy difference due to changes in coordination (i.e., ΔE_c) with density functional theory. Validating our novel TMCs against a ΔE_c benchmark of experimentally observed TMCs reveals strong agreement. We anticipate our open-source workflows will accelerate automated TMC screening by proposing realistic metal–ligand coordination outcomes of synthesized organometallic compounds.'
publication: '*submitted*'
#doi: 10.1021/jacs.2c11858
links:
- name: ChemRxiv
  url: https://doi.org/10.26434/chemrxiv-2025-7t9st
---
