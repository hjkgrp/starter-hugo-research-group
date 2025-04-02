---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Assessing UFF and DFT-Tuned Force Fields for Predicting Experimental Isotherms of MOFs
subtitle: ''
summary: ''
authors:
- yscho
- jakob205
- admin
tags: []
categories: []
date: '2025-03-18'
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
abstract: 'Metal–organic frameworks (MOFs) are promising materials for gas storage and separation applications due to their high tunability and porosity. The rational design of MOFs relies on accurate computational modeling, with grand canonical Monte Carlo (GCMC) simulations frequently employed to model gas uptake. However, GCMC predictions often deviate from experimental observations, limiting their utility in MOF screening. These discrepancies primarily arise from three factors: inaccuracies in the force field, neglect of atomic motions, and neglect of structural imperfections in MOFs. In this study, we systematically evaluate the impact of the first factor on the predictive accuracy of the GCMC simulations. We evaluate the widely used Universal Force Field (UFF) by comparing its predictions with experimental isotherms for four representative adsorbates, H₂, CO₂, C₂H₄, and C₂H₆, across 379 isotherms from 142 MOFs. The results show that UFF consistently overestimates the gas uptake in GCMC simulations. To isolate the contribution of force field inaccuracies to errors in GCMC, we developed a practical scheme for fitting force field parameters to DFT-calculated energies for a large set of MOFs. While the refined force field improves the accuracy of interatomic interaction energies, its reduction of repulsion, combined with UFF’s tendency to overestimate gas uptake, ultimately amplifies the overestimation of experimental gas uptake meaurement. Our analysis suggests that improving the agreement of gas adsorption prediction with experiments requires addressing atomic motion and structural defects in MOFs alongside force field refinements.'
publication: '*J. Chem. Inf. Model.*, **in press**'
doi: 10.1021/acs.jcim.4c02044
#url_pdf: https://pubs.aip.org/aip/jcp/article-pdf/doi/10.1063/5.0201934/19883122/154101_1_5.0201934.pdf
links:
- name: ChemRxiv
  url: https://doi.org/10.26434/chemrxiv-2024-wh9m4
---
