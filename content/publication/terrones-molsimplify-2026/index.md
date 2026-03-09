---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'molSimplify 2.0: Improved Structure Generation for Automating Discovery in Inorganic Molecular and Reticular Chemistry'
subtitle: ''
summary: ''
authors:
- gterrone
- rolan701
- jwt
- akash98
- yw580
- aarongar
- nandy
- rameyer
- fe2o3
- ohch
- Sebastian G. Pujet
- dbkchu
- davutm
- admin

tags: []
categories: []
date: '2026-02-03'
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
abstract: 'We provide an overview of core molSimplify code functionality and recent updates that enhance its capabilities for automated molecular and materials modeling. We describe the mol3D and atom3D classes, which store atomic and bonding information for a wide range of functions, including reading, modifying, and characterizing molecular geometries from common file formats. Enhancements to decoration and substructure addition functions enable the systematic derivatization of template molecules. We introduce a new mol2D class that enables graph-based uniqueness checks and substructure identification. Most importantly, we introduce improvements to transition metal complex (TMC) generation that eliminate steric clashes and enable structure building with ligands of higher denticity. Integration with machine learning models that predict coordinating atom identities enables truly high-throughput, de novo TMC generation. We describe applications of molSimplify outside of isolated TMCs, including extensions to periodic systems (e.g., metal–organic frameworks) and to metalloenzymes through the protein3D class. We demonstrate our improved combined structure prediction and generation workflow by generating structures of a database of experimentally characterized Ir complexes from only the SMILES strings of their respective ligands. We envision that recent enhancements will make the code easily extendable to other periodic materials, such as covalent organic frameworks and zeolites, or to multimetallic TMCs.'
publication: '*J. Chem. Inf. Model*, **in press**'
doi: 10.1021/acs.jcim.5c02733
url_pdf: https://pubs.acs.org/doi/pdf/10.1021/acs.jcim.5c02733?ref=article_openPDF
links:
- name: ChemRxiv
  url: https://doi.org/10.26434/chemrxiv-2025-h8gff-v2
---
