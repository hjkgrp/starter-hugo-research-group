---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Accurate potential energy surfaces with a DFT+U(R) approach
subtitle: ''
summary: ''
authors:
- admin
- Nicola Marzari
tags: []
categories: []
date: '2011-11-01'
lastmod: 2021-06-20T14:45:52-04:00
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
publishDate: '2021-06-21T01:48:29.704053Z'
publication_types:
- '2'
abstract: We introduce an improvement to the Hubbard U augmented density functional
  approach known as DFT+U that incorporates variations in the value of self-consistently
  calculated, linear-response U with changes in geometry. This approach overcomes
  the one major shortcoming of previous DFT+U studies, i.e., the use of an averaged
  Hubbard U when comparing energies for different points along a potential energy
  surface is no longer required. While DFT+U is quite successful at providing accurate
  descriptions of localized electrons (e.g., d or f) by correcting self-interaction
  errors of standard exchange correlation functionals, we show several diatomic molecule
  examples where this position-dependent DFT+U(R) provides a significant two- to four-fold
  improvement over DFT+U predictions, when compared to accurate correlated quantum
  chemistry and experimental references. DFT+U(R) reduces errors in binding energies,
  frequencies, and equilibrium bond lengths by applying the linear-response, position-dependent
  U(R) at each configuration considered. This extension is most relevant where variations
  in U are large across the points being compared, as is the case with covalent diatomic
  molecules such as transition-metal oxides. We thus provide a tool for deciding whether
  a standard DFT+U approach is sufficient by determining the strength of the dependence
  of U on changes in coordinates. We also apply this approach to larger systems with
  greater degrees of freedom and demonstrate how DFT+U(R) may be applied automatically
  in relaxations, transition-state finding methods, and dynamics.
publication: '*J. Chem. Phys.*, **19**, 194105 (2011)'
url_pdf: https://aip.scitation.org/doi/abs/10.1063/1.3660353
doi: 10.1063/1.3660353
---
