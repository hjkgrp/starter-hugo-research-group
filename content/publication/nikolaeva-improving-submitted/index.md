---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Improving Molecular Dynamics of Aqueous Electrolytes through Data-Driven Sensitivity-Guided GFN2-xTB Reparameterization'
subtitle: ''
summary: ''
authors:
- tatiana
- admin
- Christopher J. Stein

tags: []
categories: []
date: '2026-10-21'
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
abstract: 'Semiempirical tight-binding methods such as GFN2-xTB enable efficient molecular dynamics (MD) simulations, but their performance is strongly system dependent. The default GFN2-xTB parameterization overestimates equilibrium densities of liquid water and aqueous NaCl, and it underestimates the bond length for Na+–water pairs in the radial distribution function. To correct these deficiencies, we develop a sensitivity-guided stepwise approach to reparameterize GFN2-xTB against cluster-based and periodic revPBE0-D3 data. We find that the GFN2-xTB fitting problem is ill-conditioned, with many compensating parameter changes that reduce fitted errors but yield unphysical densities in MD simulations. Fisher information matrix (FIM) analysis reveals that only a few parameter combinations dominate the sensitivity of fitted observables, suggesting a reduction of the parameter space for efficient optimization. Optimizing those FIM-selected parameter subsets first for H/O and then for Na improves the equilibrium densities and shifts Na+ hydration distances into the experimental ranges without compromising the remaining properties. We achieve these improvements without directly fitting densities or hydration distances. While the best agreement with experiment for densities is achieved by optimizations on periodic datasets that include virials in the objective function, inclusion of targeted scans of essential geometric degrees of freedom in either a periodic or cluster dataset also improves optimization. Our results identify cluster data as a practical route to correct ion-solvation structure via inexpensive reference calculations, while periodic virials provide complementary control over bulk properties. These findings demonstrate that sensitivity-guided parameter selection, combined with carefully selected reference data describing the relevant interactions, enables GFN2-xTB reparameterizations whose improvements in the static fit translate to bulk MD and provides a general strategy for improving dynamical properties from low-cost electronic structure methods.'
publication: '*submitted*'
#doi: 10.1021/jacs.2c11858
links:
- name: ChemRxiv
  url: https://chemrxiv.org/doi/full/10.26434/chemrxiv.15010774/v1
---
