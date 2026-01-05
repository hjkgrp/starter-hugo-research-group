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
date: '2025-12-31'
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
abstract: 'Knowledge of how a ligand coordinates a metal is essential for mechanistic and data-driven studies of transition metal complexes (TMCs), but most analyses assume a single binding interaction for a given metal–ligand pair. In catalysis, many ligands engage in dynamic, hemilabile coordination modes, challenging this assumption. In this work, we curate data sets of hemilabile and nonhemilabile ligands from experimentally characterized structures in the Cambridge Structural Database, analyze trends in observed coordination modes, and introduce four exhaustive and mutually exclusive types of hemilability. Using these labeled data sets, we train graph neural networks to carry out classification of hemilabile ligands with high accuracy, precision, and recall and develop an ensemble algorithm that predicts primary and alternative chemically plausible coordination modes from SMILES strings in an end-to-end fashion. We demonstrate the utility of our algorithm by generating novel TMCs in predicted coordination modes and calculating the corresponding energy difference due to changes in coordination (i.e., ΔEc) with density functional theory. Comparing our novel TMCs in multiple poses against an energetic criterion from experimentally observed TMCs confirms the plausibility of our alternative poses. We anticipate that our open-source workflows will accelerate organometallic discovery in experimental and virtual screening campaigns by proposing realistic metal–ligand coordination.'
publication: '*J. Am. Chem. Soc*, **147**, 48218–48234 (2025)'
doi: 10.1021/jacs.5c17169
url_pdf: https://pubs.acs.org/doi/10.1021/jacs.5c17169#
links:
- name: ChemRxiv
  url: https://doi.org/10.26434/chemrxiv-2025-7t9st
---
