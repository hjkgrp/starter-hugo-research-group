---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Systematic Quantum Mechanical Region Determination in QM/MM Simulation
subtitle: ''
summary: ''
authors:
- Maria Karelina
- admin
tags: []
categories: []
date: '2017-02-01'
lastmod: 2021-06-20T14:45:48-04:00
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
publishDate: '2021-06-21T01:48:24.339327Z'
publication_types:
- '2'
abstract: 'Hybrid quantum mechanical-molecular mechanical (QM/MM) simulations are
  widely used in enzyme simulation. Over ten convergence studies of QM/MM methods
  have revealed over the past several years that key energetic and structural properties
  approach asymptotic limits with only very large (ca. 500–1000 atom) QM regions.
  This slow convergence has been observed to be due in part to significant charge
  transfer between the core active site and the surrounding protein environment, which
  cannot be addressed by improvement of MM force fields or the embedding method employed
  within QM/MM. Given this slow convergence, it becomes essential to identify strategies
  for the most atom-economical determination of optimal QM regions and to gain insight
  into the crucial interactions captured only in large QM regions. Here, we extend
  and develop two methods for quantitative determination of QM regions. First, in
  the charge shift analysis (CSA) method, we probe the reorganization of electron
  density when core active site residues are removed completely, as determined by
  large-QM region QM/MM calculations. Second, we introduce the highly parallelizable
  Fukui shift analysis (FSA), which identifies how core/substrate frontier states
  are altered by the presence of an additional QM residue in smaller initial QM regions.
  We demonstrate that the FSA and CSA approaches are complementary and consistent
  on three test case enzymes: catechol O-methyltransferase, cytochrome P450cam, and
  hen eggwhite lysozyme. We also introduce validation strategies and test the sensitivities
  of the two methods to geometric structure, basis set size, and electronic structure
  methodology. Both methods represent promising approaches for the systematic, unbiased
  determination of quantum mechanical effects in enzymes and large systems that necessitate
  multiscale modeling.'
publication: '*J. Chem. Theory Comput.*, **13**, 563-576 (2017)'
url_pdf: https://doi.org/10.1021/acs.jctc.6b01049
doi: 10.1021/acs.jctc.6b01049
---
