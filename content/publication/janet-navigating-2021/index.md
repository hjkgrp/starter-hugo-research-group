---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Navigating Transition-Metal Chemical Space: Artificial Intelligence for First-Principles
  Design'
subtitle: ''
summary: ''
authors:
- Jon Paul Janet
- crduan
- nandy
- Fang Liu
- admin
tags: []
categories: []
date: '2021-02-01'
lastmod: 2021-06-20T14:45:39-04:00
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
publishDate: '2021-06-21T01:48:11.957447Z'
publication_types:
- '2'
abstract: ConspectusThe variability of chemical bonding in open-shell transition-metal
  complexes not only motivates their study as functional materials and catalysts but
  also challenges conventional computational modeling tools. Here, tailoring ligand
  chemistry can alter preferred spin or oxidation states as well as electronic structure
  properties and reactivity, creating vast regions of chemical space to explore when
  designing new materials atom by atom. Although first-principles density functional
  theory (DFT) remains the workhorse of computational chemistry in mechanism deduction
  and property prediction, it is of limited use here. DFT is both far too computationally
  costly for widespread exploration of transition-metal chemical space and also prone
  to inaccuracies that limit its predictive performance for localized d electrons
  in transition-metal complexes. These challenges starkly contrast with the well-trodden
  regions of small-organic-molecule chemical space, where the analytical forms of
  molecular mechanics force fields and semiempirical theories have for decades accelerated
  the discovery of new molecules, accurate DFT functional performance has been demonstrated,
  and gold-standard methods from correlated wavefunction theory can predict experimental
  results to chemical accuracy.The combined promise of transition-metal chemical space
  exploration and lack of established tools has mandated a distinct approach. In this
  Account, we outline the path we charted in exploration of transition-metal chemical
  space starting from the first machine learning (ML) models (i.e., artificial neural
  network and kernel ridge regression) and representations for the prediction of open-shell
  transition-metal complex properties. The distinct importance of the immediate coordination
  environment of the metal center as well as the lack of low-level methods to accurately
  predict structural properties in this coordination environment first motivated and
  then benefited from these ML models and representations. Once developed, the recipe
  for prediction of geometric, spin state, and redox potential properties was straightforwardly
  extended to a diverse range of other properties, including in catalysis, computational
  “feasibility”, and the gas separation properties of periodic metal–organic frameworks.
  Interpretation of selected features most important for model prediction revealed
  new ways to encapsulate design rules and confirmed that models were robustly mapping
  essential structure–property relationships. Encountering the special challenge of
  ensuring that good model performance could generalize to new discovery targets motivated
  investigation of how to best carry out model uncertainty quantification. Distance-based
  approaches, whether in model latent space or in carefully engineered feature space,
  provided intuitive measures of the domain of applicability. With all of these pieces
  together, ML can be harnessed as an engine to tackle the large-scale exploration
  of transition-metal chemical space needed to satisfy multiple objectives using efficient
  global optimization methods. In practical terms, bringing these artificial intelligence
  tools to bear on the problems of transition-metal chemical space exploration has
  resulted in ML-model assessments of large, multimillion compound spaces in minutes
  and validated new design leads in weeks instead of decades.
publication: '*Acc. Chem. Res.*, **54**, 532-545 (2021)'
url_pdf: https://doi.org/10.1021/acs.accounts.0c00686
doi: 10.1021/acs.accounts.0c00686
---
