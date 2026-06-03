---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'pyEF: A Python Framework for QM and QM/MM Atom-Wise Electric Field Analysis' 
subtitle: ''
summary: ''
authors:
- manets12
- kastner
- Yuriy Román-Leshkov
- admin
tags: []
categories: []
date: '2026-05-26'
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
abstract: 'We introduce pyEF, a software package for computing molecular electric fields, electrostatic interaction energies, and electrostatic potentials from quantum mechanical (QM) atom-centered multipole expansions with atom-wise decomposable contributions. We demonstrate the computational efficiency and accuracy of this QM-derived electric field evaluation tool through several tests. To assess the influence of the underlying QM method and charge partitioning scheme on these electrostatic quantities, we analyze over 250 configurations of an acetone solute molecule in five solvents of variable polarity. We find that electric field calculations are highly sensitive to the choice of charge partitioning method. Even among real-space charge schemes, acetone Stark tuning rates differ by up to a factor of 2. Benchmarking computed solvent dipole moments against experimental bulk values, we conclude that the CM5, ADCH, and Hirshfeld-I charge schemes most reliably capture solvent electrostatics and therefore provide a more faithful foundation for computing electric fields. When constructed from these real-space charges, electric fields are nearly insensitive to basis set size and monotonically increase in magnitude with higher Fock exchange. We also demonstrate efficient convergence of QM electrostatics when more distant molecules are represented solely by MM point charges, reducing computational overhead. Leveraging these findings, we demonstrate the use of pyEF to deduce environmental effects on a transition metal complex from a Ga4L612– nanocage and quantify the dominant role of organic linkers in orchestrating electrostatic preorganization.'
publication: '*J. Chem. Theory. Comput.*, **22**, 4982--4994 (2026)'
doi: 10.1021/acs.jctc.6c00065
url_pdf: https://pubs.acs.org/doi/pdf/10.1021/acs.jctc.6c00065?ref=article_openPDF
links:
- name: ChemRxiv
  url: https://doi.org/10.26434/chemrxiv-2026-3cbg4
---
