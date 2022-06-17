---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Resolving Transition Metal Chemical Space: Feature Selection for Machine Learning
  and Structure–Property Relationships'
subtitle: ''
summary: ''
authors:
- Jon Paul Janet
- admin
tags: []
categories: []
date: '2017-11-01'
lastmod: 2021-06-20T14:45:47-04:00
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
publishDate: '2021-06-21T01:48:22.442948Z'
publication_types:
- '2'
abstract: Machine learning (ML) of quantum mechanical properties shows promise for
  accelerating chemical discovery. For transition metal chemistry where accurate calculations
  are computationally costly and available training data sets are small, the molecular
  representation becomes a critical ingredient in ML model predictive accuracy. We
  introduce a series of revised autocorrelation functions (RACs) that encode relationships
  of the heuristic atomic properties (e.g., size, connectivity, and electronegativity)
  on a molecular graph. We alter the starting point, scope, and nature of the quantities
  evaluated in standard ACs to make these RACs amenable to inorganic chemistry. On
  an organic molecule set, we first demonstrate superior standard AC performance to
  other presently available topological descriptors for ML model training, with mean
  unsigned errors (MUEs) for atomization energies on set-aside test molecules as low
  as 6 kcal/mol. For inorganic chemistry, our RACs yield 1 kcal/mol ML MUEs on set-aside
  test molecules in spin-state splitting in comparison to 15–20× higher errors for
  feature sets that encode whole-molecule structural information. Systematic feature
  selection methods including univariate filtering, recursive feature elimination,
  and direct optimization (e.g., random forest and LASSO) are compared. Random-forest-
  or LASSO-selected subsets 4–5× smaller than the full RAC set produce sub- to 1 kcal/mol
  spin-splitting MUEs, with good transferability to metal–ligand bond length prediction
  (0.004–5 Å MUE) and redox potential on a smaller data set (0.2–0.3 eV MUE). Evaluation
  of feature selection results across property sets reveals the relative importance
  of local, electronic descriptors (e.g., electronegativity, atomic number) in spin-splitting
  and distal, steric effects in redox potential and bond lengths.
publication: '*J. Phys. Chem. A*, **121**, 8939-8954 (2017)'
url_pdf: https://doi.org/10.1021/acs.jpca.7b08750
doi: 10.1021/acs.jpca.7b08750
---
