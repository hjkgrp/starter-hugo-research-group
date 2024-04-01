---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Improving Gas Adsorption Modeling for MOFs by Local Calibration of Hubbard U Parameters 
subtitle: ''
summary: ''
authors:
- yscho
- admin
tags: []
categories: []
date: '2024-03-31'
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
abstract: 'While computational screening with density functional theory (DFT) is frequently employed for the screening of metal-organic frameworks (MOFs) for gas separation and storage, commonly applied generalized gradient approximations (GGAs) exhibit self-interaction errors, that hinder predictions of adsorption energies. We investigate the Hubbard U parameter to augment DFT calculations for full periodic MOFs, targeting a more precise modeling of gas molecule–MOF interactions, specifically for N<sub>2</sub>, CO<sub>2</sub>, and O<sub>2</sub>. We introduce a calibration scheme for the U parameter, which is tailored for each MOF, by leveraging higher-level calculations on the secondary building unit (SBU) of the MOF. When applied to the full periodic MOF, the U parameter calibrated against hybrid HSE06 calculations of SBUs successfully reproduces hybrid-quality calculations of the adsorption energy of the periodic MOF. The mean absolute deviation (MAD) of adsorption energies reduces from 0.13 eV for a standard GGA treatment to 0.06 eV with the calibrated U, demonstrating the utility of the calibration procedure when applied to the full MOF structure. Furthermore, attempting to use CCSD(T) calculations of isolated SBUs for this calibration procedure shows varying degrees of success in predicting the experimental heat of adsorption. It improves accuracy for N<sub>2</sub> adsorption for cases of overbinding, whereas its impact on CO<sub>2</sub> is minimal, and ambiguities in spin state assignment hinder consistent improvements of O<sub>2</sub> adsorption. Our findings emphasize the limitations of cluster models and advocate the use of full periodic MOF systems with a calibrated U parameter, providing a more comprehensive understanding of gas adsorption in MOFs.'
publication: '*J. Chem. Phys.*, **in press**'
#doi: 10.1021/jacs.2c11858
links:
- name: ChemRxiv
  url: https://doi.org/10.26434/chemrxiv-2024-pjh9z
---
