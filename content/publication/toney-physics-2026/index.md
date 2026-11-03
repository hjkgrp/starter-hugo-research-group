---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Physics-based molecular fingerprints from spectral graph theory provide efficient geometry-aware measures of chemical similarity' 
subtitle: ''
summary: ''
authors:
- jwt
- ayleenf
- samirdar
- admin 
tags: []
categories: []
date: '2026-10-15'
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
abstract: 'Molecular representations are essential for the evaluation of molecular similarity and the development of structure–property relationships. Despite the known importance of three-dimensional (3D) structure to determine chemical and physical properties, the most widely used molecular fingerprints encode only two-dimensional connectivity. Such representations fail to distinguish similar but distinct stereoisomers and conformers. Alternative 3D methods are typically defined pairwise, making their application to large chemical spaces prohibitive, while deep learning embeddings are expressive but uninterpretable and limited by their training data diversity. Here, we introduce novel physics-inspired molecular fingerprints based on principles from spectral graph theory. We represent a molecule as a complete graph in 3D space, with edge weights encoding heuristic physical interactions. Eigenvalue decomposition of the resulting graph Laplacian matrix results in a computationally efficient fixed-length chemical fingerprint that encodes 3D structure while obeying necessary physical symmetries of permutation and E(3) invariance. Spectral fingerprints differentiate between unique molecular structures with identical 2D connectivity, overcoming a limitation of 2D descriptors, while maintaining the low computational cost needed for efficient screening of vast chemical spaces. We evaluate our fingerprints with community detection algorithms and observe strong performance against representative baselines across datasets from organic, inorganic, biological, reticular, and reaction chemistry. Nearest-neighbor property estimation and applicability domain analyses reveal the utility of our molecular representation in machine learning and cheminformatics. We anticipate that spectral fingerprints will serve as interpretable and efficient measures of chemical similarity that incorporate 3D information at minimal cost and generalize well across diverse chemical domains.'
publication: '*Chem. Sci.*, **in press**'
doi: 10.1039/d6sc06309h
url_pdf: https://pubs.rsc.org/sc/article-pdf/doi/10.1039/d6sc06309h/14942099/d6sc06309h.pdf
links:
- name: arXiv
  url: https://doi.org/10.48550/arXiv.2608.05336
---
