---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Machine Learning Prediction of the Experimental Transition Temperature of Fe(II) Spin-Crossover Complexes'
subtitle: ''
summary: ''
authors:
- vyshnavi
- Irem B. Kilic
- gterrone
- crduan
- admin
tags: []
categories: []
date: '2023-12-26'
lastmod: 2023-06-08T13:54:08-04:00
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
publishDate: '2023-06-08T17:54:08.046005Z'
publication_types:
- '2'
abstract: 'Spin-crossover (SCO) complexes are materials that exhibit changes in the spin state in response to external stimuli, with potential applications in molecular electronics. It is challenging to know a priori how to design ligands to achieve the delicate balance of entropic and enthalpic contributions needed to tailor a transition temperature close to room temperature. We leverage the SCO complexes from the previously curated SCO-95 data set [Vennelakanti et al. *J. Chem. Phys.* **159**, 024120 (2023)] to train three machine learning (ML) models for transition temperature (T<sub>1/2</sub>) prediction using graph-based revised autocorrelations as features. We perform feature selection using random forest-ranked recursive feature addition (RF-RFA) to identify the features essential to model transferability. Of the ML models considered, the full feature set RF and recursive feature addition RF models perform best, achieving moderate correlation to experimental T<sub>1/2</sub> values. We then compare ML T<sub>1/2</sub> predictions to those from three previously identified best-performing density functional approximations (DFAs) which accurately predict SCO behavior across SCO-95, finding that the ML models predict T<sub>1/2</sub> more accurately than the best-performing DFAs. In addition, we study ML model predictions for a set of 18 SCO complexes for which only estimated T<sub>1/2</sub> values are available. Upon excluding outliers from this set, the RF-RFA RF model shows a strong correlation to estimated T<sub>1/2</sub> values with a Pearson’s r of 0.82. In contrast, DFA-predicted T<sub>1/2</sub> values have large errors and show no correlation to estimated T<sub>1/2</sub> values over the same set of complexes. Overall, our study demonstrates slightly superior performance of ML models in comparison with some of the best-performing DFAs, and we expect ML models to improve further as larger data sets of SCO complexes are curated and become available for model training.'
publication: '*J. Phys. Chem. A*, **in press**'
doi: 10.1021/acs.jpca.3c07104
url_pdf: https://pubs.acs.org/doi/epdf/10.1021/acs.jpca.3c07104
links:
- name: ChemRxiv
  url: https://doi.org/10.26434/chemrxiv-2023-mhb4c
---
