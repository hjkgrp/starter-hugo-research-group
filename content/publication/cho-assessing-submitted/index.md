---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Assessing UFF and DFT-tuned Force Fields for Predicting Experimental Isotherms of MOFs
subtitle: ''
summary: ''
authors:
- yscho
- jakob205
- admin
tags: []
categories: []
date: '2025-01-01'
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
abstract: 'Metal-organic frameworks (MOFs) are promising materials for gas storage and separation applications due to their high tunability and porosity. The rational design of MOFs relies on accurate computational modeling, with grand canonical Monte Carlo (GCMC) simulations frequently employed to model gas uptake. In GCMC simulations, interatomic interactions are typically described using force fields, but no single existing force field can fully capture the diverse chemical environments present in MOFs. Refining force field parameters using density functional theory (DFT) provides a more accurate, ab initio-level description of interatomic interactions. In this study, we evaluate the predictive power of the widely used Universal Force Field (UFF) by comparing its predictions with experimental isotherms for four representative adsorbates, H2, CO2, C2H4, and C2H6, across 379 isotherms from 142 MOFs. The results show that UFF consistently overestimates gas uptake in GCMC simulations. To provide a customized force field for each MOF, we present a practical scheme for fitting force field parameters to DFT-calculated energies for a large set of MOFs. The refined force field successfully reproduces the DFT-calculated interaction energy, effectively correcting UFF’s overestimation of interatomic repulsion. However, because UFF overestimates gas uptake, and the refined force field reduces repulsion further, this refinement amplifies the overestimation. Our analysis suggests that structural defects and atomic motion in MOFs, typically neglected in GCMC simulations, should be addressed to improve agreement of gas adsorption prediction with experiments.'
publication: '*submitted*'
#doi: 10.1063/5.0201934
#url_pdf: https://pubs.aip.org/aip/jcp/article-pdf/doi/10.1063/5.0201934/19883122/154101_1_5.0201934.pdf
links:
- name: ChemRxiv
  url: https://doi.org/10.26434/chemrxiv-2024-wh9m4
---
