---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Non-empirical, low-cost recovery of exact conditions with model-Hamiltonian
  inspired expressions in jmDFT
subtitle: ''
summary: ''
authors:
- Akash Bajaj
- Fang Liu
- admin
tags: []
categories: []
date: '2019-04-01'
lastmod: 2021-06-20T14:45:43-04:00
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
publishDate: '2021-06-21T01:48:17.465295Z'
publication_types:
- '2'
abstract: Density functional theory (DFT) is widely applied to both molecules and
  materials, but well known energetic delocalization and static correlation errors
  in practical exchange-correlation approximations limit quantitative accuracy. Common
  methods that correct energetic delocalization errors, such as the Hubbard U correction
  in DFT+U or Hartree-Fock exchange in global hybrids, do so at the cost of worsening
  static correlation errors. We recently introduced an alternate approach [Bajaj et
  al., J. Chem. Phys. 147, 191101 (2017)] known as judiciously modified DFT (jmDFT),
  wherein the deviation from exact behavior of semilocal functionals over both fractional
  spin and charge, i.e., the so-called flat plane, was used to motivate functional
  forms of second order analytic corrections. In this work, we introduce fully nonempirical
  expressions for all four coefficients in a DFT+U+J-inspired form of jmDFT, where
  all coefficients are obtained only from energies and eigenvalues of the integer-electron
  systems. We show good agreement for U and J coefficients obtained nonempirically
  as compared with the results of numerical fitting in a jmDFT U+J/J′ correction.
  Incorporating the fully nonempirical jmDFT correction reduces and even eliminates
  the fractional spin error at the same time as eliminating the energetic delocalization
  error. We show that this approach extends beyond s-electron systems to higher angular
  momentum cases including p- and d-electrons. Finally, we diagnose some shortcomings
  of the current jmDFT approach that limit its ability to improve upon DFT results
  for cases such as weakly bound anions due to poor underlying semilocal functional
  behavior.
publication: '*J. Chem. Phys.*, **150**, 154115 (2019)'
url_pdf: https://aip.scitation.org/doi/abs/10.1063/1.5091563
doi: 10.1063/1.5091563
---
