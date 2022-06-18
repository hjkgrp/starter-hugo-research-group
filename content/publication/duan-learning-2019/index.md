---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Learning from Failure: Predicting Electronic Structure Calculation Outcomes
  with Machine Learning Models'
subtitle: ''
summary: ''
authors:
- crduan
- Jon Paul Janet
- Fang Liu
- nandy
- admin
tags: []
categories: []
date: '2019-04-01'
lastmod: 2021-06-20T14:45:44-04:00
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
publishDate: '2021-06-21T01:48:18.378325Z'
publication_types:
- '2'
abstract: High-throughput computational screening for chemical discovery mandates
  the automated and unsupervised simulation of thousands of new molecules and materials.
  In challenging materials spaces, such as open shell transition metal chemistry,
  characterization requires time-consuming first-principles simulation that often
  necessitates human intervention. These calculations can frequently lead to a null
  result, e.g., the calculation does not converge or the molecule does not stay intact
  during a geometry optimization. To overcome this challenge toward realizing fully
  automated chemical discovery in transition metal chemistry, we have developed the
  first machine learning models that predict the likelihood of successful simulation
  outcomes. We train support vector machine and artificial neural network classifiers
  to predict simulation outcomes (i.e., geometry optimization result and degree of
  ⟨S2⟩ deviation) for a chosen electronic structure method based on chemical composition.
  For these static models, we achieve an area under the curve of at least 0.95, minimizing
  computational time spent on nonproductive simulations and therefore enabling efficient
  chemical space exploration. We introduce a metric of model uncertainty based on
  the distribution of points in the latent space to systematically improve model prediction
  confidence. In a complementary approach, we train a convolutional neural network
  classification model on simulation output electronic and geometric structure time
  series data. This dynamic model generalizes more readily than the static classifier
  by becoming more predictive as input simulation length increases. Finally, we describe
  approaches for using these models to enable autonomous job control in transition
  metal complex discovery.
publication: '*J. Chem. Theory Comput.*, **15**, 2331-2345 (2019)'
url_pdf: https://doi.org/10.1021/acs.jctc.9b00057
doi: 10.1021/acs.jctc.9b00057
---
