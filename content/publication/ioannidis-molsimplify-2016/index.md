---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'molSimplify: A toolkit for automating discovery in inorganic chemistry'
subtitle: ''
summary: ''
authors:
- Efthymios I. Ioannidis
- Terry Z. H. Gani
- admin
tags:
- '"high-throughput screening"'
- '"chemical discovery"'
- '"first-principles simulation"'
- '"python"'
- '"structure generation"'
categories: []
date: '2016-01-01'
lastmod: 2021-06-20T14:45:49-04:00
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
publishDate: '2021-06-21T01:48:25.970048Z'
publication_types:
- '2'
abstract: We present an automated, open source toolkit for the first-principles screening
  and discovery of new inorganic molecules and intermolecular complexes. Challenges
  remain in the automatic generation of candidate inorganic molecule structures due
  to the high variability in coordination and bonding, which we overcome through a
  divide-and-conquer tactic that flexibly combines force-field preoptimization of
  organic fragments with alignment to first-principles-trained metal-ligand distances.
  Exploration of chemical space is enabled through random generation of ligands and
  intermolecular complexes from large chemical databases. We validate the generated
  structures with the root mean squared (RMS) gradients evaluated from density functional
  theory (DFT), which are around 0.02 Ha/au across a large 150 molecule test set.
  Comparison of molSimplify results to full optimization with the universal force
  field reveals that RMS DFT gradients are improved by 40%. Seamless generation of
  input files, preparation and execution of electronic structure calculations, and
  post-processing for each generated structure aids interpretation of underlying chemical
  and energetic trends. © 2016 Wiley Periodicals, Inc.
publication: '*J. Comput. Chem.*, **37**, 2106-2117 (2016)'
url_pdf: https://onlinelibrary.wiley.com/doi/abs/10.1002/jcc.24437
doi: 10.1002/jcc.24437
---
