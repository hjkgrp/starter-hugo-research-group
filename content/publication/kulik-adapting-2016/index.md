---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Adapting DFT+U for the Chemically Motivated Correction of Minimal Basis Set
  Incompleteness
subtitle: ''
summary: ''
authors:
- admin
- Natasha Seelam
- Brendan D. Mar
- Todd J. Martínez
tags: []
categories: []
date: '2016-07-01'
lastmod: 2021-06-20T14:45:50-04:00
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
publishDate: '2021-06-21T01:48:26.623392Z'
publication_types:
- '2'
abstract: Recent algorithmic and hardware advances have enabled the application of
  electronic structure methods to the study of large-scale systems such as proteins
  with O(103) atoms. Most such methods benefit greatly from the use of reduced basis
  sets to further enhance their speed, but truly minimal basis sets are well-known
  to suffer from incompleteness error that gives rise to incorrect descriptions of
  chemical bonding, preventing minimal basis set use in production calculations. We
  present a strategy for improving these well-known shortcomings in minimal basis
  sets by selectively tuning the energetics and bonding of nitrogen and oxygen atoms
  within proteins and small molecules to reproduce polarized double-ζ basis set geometries
  at minimal basis set cost. We borrow the well-known +U correction from the density
  functional theory community normally employed for self-interaction errors and demonstrate
  its power in the context of correcting basis set incompleteness within a formally
  self-interaction-free Hartree–Fock framework. We tune the Hubbard U parameters for
  nitrogen and oxygen atoms on small-molecule tautomers (e.g., cytosine), demonstrate
  the applicability of the approach on a number of amide-containing molecules (e.g.,
  formamide, alanine tripeptide), and test our strategy on a 10 protein test set where
  anomalous proton transfer events are reduced by 90% from RHF/STO-3G to RHF/STO-3G+U,
  bringing the latter into quantitative agreement with RHF/6-31G* results. Although
  developed with the study of biological molecules in mind, this empirically tuned
  U approach shows promise as an alternative strategy for correction of basis set
  incompleteness errors.
publication: '*J. Phys. Chem. A*, **120**, 5939-5949 (2016)'
url_pdf: https://doi.org/10.1021/acs.jpca.6b04527
doi: 10.1021/acs.jpca.6b04527
---
