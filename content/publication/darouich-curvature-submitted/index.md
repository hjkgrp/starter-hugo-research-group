---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Curvature-aware flow matching for molecular structure generation' 
subtitle: ''
summary: ''
authors:
- samirdar
- Juliane Geisler
- jwt
- Tanja Bien
- Johannes Kästner
- admin
- Mathias Niepert


tags: []
categories: []
date: '2026-09-26'
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
abstract: 'Generative models produce three-dimensional molecular structures with high geometric accuracy, yet they are trained on distributions of atomic coordinates without explicit access to the underlying physics. The potential energy surface (PES) describes how the energy changes around a molecular geometry, and the RMSD between a generated structure and its reference captures this local landscape only indirectly. Supervising the PES during training could close this gap, but conformers and transition states (TSs) are stationary points at which the forces vanish, so first-order quantities carry little information about them. What remains is the local curvature, encoded in the Hessian of the PES. Quantum-chemical Hessians are too expensive to be available at the scale required for training, but recently proposed machine-learned predictors make curvature inexpensive enough to supervise directly. We introduce CurvFM, a flow matching (FM) formulation whose training objective constrains the curvature at the generated structure. A frozen Hessian prediction model is evaluated at the generated endpoint and at the reference structure, which removes the need for quantum-chemical Hessians and keeps the residual cheap enough to impose at every training step. Across TS and conformer generation, CurvFM substantially improves physical fidelity at unchanged global structural accuracy, reducing the median deviation in maximum force by 63% on GEOM-QM9 and raising the fraction of valid TSs by up to 10% across three reaction datasets.'
publication: '*submitted*'
#doi: https://doi.org/10.1038/s43588-026-01034-5
#url_pdf: https://www.nature.com/articles/s43588-026-01034-5.pdf
links:
- name: arXiv
  url: https://arxiv.org/abs/2609.34592
---
