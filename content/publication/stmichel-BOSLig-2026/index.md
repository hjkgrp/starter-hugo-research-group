---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'The BOS-Lig Data Set: Accurate Ligand Charges from a Consensus Approach for 66,810 Experimentally Synthesized Ligands'
subtitle: ''
summary: ''
authors:
- rolan701
- Ryan J. Jang
- aarongar
- iliak
- admin

tags: []
categories: []
date: '2026-07-26'
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
abstract: "Understanding ligand properties is essential for computational high-throughput screening of transition metal complexes. However, ligand properties such as net charge and other information such as their application area are often absent or inconsistently recorded in crystallographic data sets. Here, we construct a ligand data set from 126,985 mononuclear transition metal complexes curated from the Cambridge Structural Database. Using an iterative charge-balancing workflow that combines complex charges, metal oxidation states, and consensus across crystallographic observations, we confidently assign net charges to 66,810 ligands among 94,581 identified unique ligand structures to curate the Boston Open-Shell Ligand (BOS-Lig) data set. The workflow assigns ligand charges in homoleptic complexes first and then iteratively propagates these assignments across heteroleptic environments, allowing charges to be inferred even when direct charge information is unavailable. We analyze cases where simple heuristics such as the octet rule would have failed and introduce a purity metric to identify when our charge assignments may be incorrect. Each ligand is also classified in terms of its metal-coordinating atoms and whether there are multiple variants (i.e., hemilability). We then link complexes to their associated journal abstracts and apply a topic-modeling workflow to link 25,146 ligands with functional application areas spanning reactivity, redox chemistry, biological chemistry, and photophysical chemistry. Together, we provide an experimentally grounded data set of ligand chemical space that connects charge and functional application as a foundation for computational screening and data-driven ligand design."
publication: '*J. Chem. Inf. Model.*, **66**, 8336–8348 (2026)'
doi: 10.1021/acs.jcim.6c01063
url_pdf: https://pubs.acs.org/jcisd8/article-pdf/65885825/acs.jcim.6c01063.pdf
links:
- name: arXiv
  url: https://doi.org/10.48550/arXiv.2604.06043
---
