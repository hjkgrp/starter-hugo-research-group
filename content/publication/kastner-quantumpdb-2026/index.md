---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'QuantumPDB: A Workflow for High-Throughput Quantum Cluster Model Generation from Protein Structures' 
subtitle: ''
summary: ''
authors:
- kastner
- weiliang
- wilson
- clorice
- allikeys
- admin

tags: []
categories: []
date: '2026-05-25'
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
abstract: 'Computational modeling of enzymes provides molecular-level insight into catalysis, but the preparation of quantum mechanical (QM) calculations starting from experimental structures is a significant bottleneck for high-throughput studies. Automated tools developed to accelerate this process may fail to generalize across distinct active site chemistries and geometries. To overcome these limitations, we present QuantumPDB, a Python package that automates the generation of hierarchical coordination/interaction spheres around an active center to create QM cluster models directly from raw protein structures. The workflow integrates structure cleaning, protonation state assignment, and QM calculation setup. It uses chemically meaningful models constructed from contact-based interaction spheres derived from Voronoi tessellation, enabling accurate representation of complex active site geometries. We provide an overview of our modular code and describe how it may be employed to automate high-throughput protein screening. To demonstrate its utility, we curated a data set of 989 holo-enzymes from the PDB and performed QM calculations on 1,673 enzyme cluster models of 842 of these enzymes. Analysis of computed properties suggests that enzyme environments simulated with density functional theory consistently modulate substrate charge toward neutrality and reduce the substrate dipole moment. This phenomenon appears to be general, even in cases where the active site consists predominantly of neutral residues. By automating and standardizing multisphere QM model construction, QuantumPDB provides a robust platform for large-scale, data-driven investigations of proteins.'
publication: '*J. Chem. Inf. Model.*, **66**, 6011--6026 (2026)'
doi: 10.1021/acs.jcim.5c03064
url_pdf: https://pubs.acs.org/doi/pdf/10.1021/acs.jcim.5c03064?ref=article_openPDF
links:
- name: ChemRxiv
  url: https://doi.org/10.26434/chemrxiv-2026-w5x1d
---
