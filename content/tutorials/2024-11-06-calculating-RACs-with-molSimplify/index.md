---
title: "Calculating RACs with molSimplify"
subtitle:
aliases: /content/calculating-RACs
 

# Summary for listings and search engines
summary: This tutorial shows how the set of RACs can be calculated given a molecule file

# Link this post with a project
projects: []

# Date published
date: 2024-11-06

# Date updated
lastmod: 

# Is this an unpublished draft?
draft: true

# Show this page in the Featured widget?
featured: false

# Featured image
# Place an image named `featured.jpg/png` in this page's folder and customize its options here.
image:
  caption: 
  focal_point: ""
  placement: 1
  preview_only: false

authors:
#- admin

tags:
- molsimplify

categories:
- molsimplify-tutorials
- tutorials

---
The following code can be used to calculate the full set of RAC descriptors for an input molecule with molSimplify. The code can be downloaded at the `.ipynb` link at the bottom of the page.
```
# import mol3D from molSimplify
from molSimplify.Classes.mol3D import mol3D
from molSimplify.Informatics.autocorrelation import generate_full_complex_autocorrelations, generate_metal_autocorrelations, generate_metal_deltametrics, generate_atomonly_autocorrelations, generate_atomonly_deltametrics
from molSimplify.Informatics.lacRACAssemble import get_descriptor_vector
```
```
xyz_file_path = 'ZOMHUG.xyz'
mol = mol3D()
mol.readfromxyz(xyz_file_path)
mol.convert2OBMol()
mol.graph = mol.populateBOMatrix(bonddict=True)
total_racs_feature_set = get_descriptor_vector(mol)
```
```
total_racs_feature_set
```
misc-dent-ax   |     0      |\n|   1 | misc-charge-ax |     0      |\n|   2 | misc-dent-eq   |     0      |\n|   3 | misc-charge-eq |     0      |\n|   4 | f-chi-0-all    |   467.793  |\n|   5 | f-chi-1-all    |  1029.69   |\n|   6 | f-chi-2-all    |  1735.91   |\n|   7 | f-chi-3-all    |  2051.5    |\n|   8 | f-Z-0-all      |  3065      |\n|   9 | f-Z-1-all      |  4934      |\n|  10 | f-Z-2-all      |  8524      |\n|  11 | f-Z-3-all      | 10066      |\n|  12 | f-I-0-all      |    82      |\n|  13 | f-I-1-all      |   170      |\n|  14 | f-I-2-all      |   300      |\n|  15 | f-I-3-all      |   348      |\n|  16 | f-T-0-all      |   470      |\n|  17 | f-T-1-all      |  1160      |\n|  18 | f-T-2-all      |  1696      |\n|  19 | f-T-3-all      |  2192      |\n|  20 | f-S-0-all      |    30.6677 |\n|  21 | f-S-1-all      |    77.5876 |\n|  22 | f-S-2-all      |   122.922  |\n|  23 | f-S-3-all      |   152.373  |\n|  24 | f-chi-0-ax     |     1.7689 |\n|  25 | f-chi-1-ax     |    10.8262 |\n|  26 | f-chi-2-ax     |    25.5759 |\n|  27 | f-chi-3-ax     |    35.91   |\n|  28 | f-Z-0-ax       |  1600      |\n|  29 | f-Z-1-ax       |   760      |\n|  30 | f-Z-2-ax       |  1800      |\n|  31 | f-Z-3-ax       |  2040      |\n|  32 | f-I-0-ax       |     1      |\n|  33 | f-I-1-ax       |     3      |\n|  34 | f-I-2-ax       |     7      |\n|  35 | f-I-3-ax       |    11      |\n|  36 | f-T-0-ax       |     9      |\n|  37 | f-T-1-ax       |    30      |\n|  38 | f-T-2-ax       |    60      |\n|  39 | f-T-3-ax       |    90      |\n|  40 | f-S-0-ax       |     2.3716 |\n|  41 | f-S-1-ax       |     3.5266 |\n|  42 | f-S-2-ax       |     8.2082 |\n|  43 | f-S-3-ax       |    11.1958 |\n|  44 | f-chi-0-eq     |     0      |\n|  45 | f-chi-1-eq     |    -4.15   |\n|  46 | f-chi-2-eq     |    -9.92   |\n|  47 | f-chi-3-eq     |   -12.37   |\n|  48 | f-Z-0-eq       |     0      |\n|  49 | f-Z-1-eq       |   101      |\n|  50 | f-Z-2-eq       |   235      |\n|  51 | f-Z-3-eq       |   389      |\n|  52 | f-I-0-eq       |     0      |\n|  53 | f-I-1-eq       |     0      |\n|  54 | f-I-2-eq       |     0      |\n|  55 | f-I-3-eq       |     0      |\n|  56 | f-T-0-eq       |     0      |\n|  57 | f-T-1-eq       |    -1      |\n|  58 | f-T-2-eq       |     1      |\n|  59 | f-T-3-eq       |     3      |\n|  60 | f-S-0-eq       |     0      |\n|  61 | f-S-1-eq       |     2.33   |\n|  62 | f-S-2-eq       |     5.45   |\n|  63 | f-S-3-eq       |     9.67   |\n|  64 | lc-chi-0-ax    |            |\n|  65 | lc-chi-1-ax    |            |\n|  66 | lc-chi-2-ax    |            |\n|  67 | lc-chi-3-ax    |            |\n|  68 | lc-Z-0-ax      |            |\n|  69 | lc-Z-1-ax      |            |\n|  70 | lc-Z-2-ax      |            |\n|  71 | lc-Z-3-ax      |            |\n|  72 | lc-I-0-ax      |            |\n|  73 | lc-I-1-ax      |            |\n|  74 | lc-I-2-ax      |            |\n|  75 | lc-I-3-ax      |            |\n|  76 | lc-T-0-ax      |            |\n|  77 | lc-T-1-ax      |            |\n|  78 | lc-T-2-ax      |            |\n|  79 | lc-T-3-ax      |            |\n|  80 | lc-S-0-ax      |            |\n|  81 | lc-S-1-ax      |            |\n|  82 | lc-S-2-ax      |            |\n|  83 | lc-S-3-ax      |            |\n|  84 | lc-chi-0-eq    |            |\n|  85 | lc-chi-1-eq    |            |\n|  86 | lc-chi-2-eq    |            |\n|  87 | lc-chi-3-eq    |            |\n|  88 | lc-Z-0-eq      |            |\n|  89 | lc-Z-1-eq      |            |\n|  90 | lc-Z-2-eq      |            |\n|  91 | lc-Z-3-eq      |            |\n|  92 | lc-I-0-eq      |            |\n|  93 | lc-I-1-eq      |            |\n|  94 | lc-I-2-eq      |            |\n|  95 | lc-I-3-eq      |            |\n|  96 | lc-T-0-eq      |            |\n|  97 | lc-T-1-eq      |            |\n|  98 | lc-T-2-eq      |            |\n|  99 | lc-T-3-eq      |            |\n| 100 | lc-S-0-eq      |            |\n| 101 | lc-S-1-eq      |            |\n| 102 | lc-S-2-eq      |            |\n| 103 | lc-S-3-eq      |            |\n| 104 | D_lc-chi-0-ax  |            |\n| 105 | D_lc-chi-1-ax  |            |\n| 106 | D_lc-chi-2-ax  |            |\n| 107 | D_lc-chi-3-ax  |            |\n| 108 | D_lc-Z-0-ax    |            |\n| 109 | D_lc-Z-1-ax    |            |\n| 110 | D_lc-Z-2-ax    |            |\n| 111 | D_lc-Z-3-ax    |            |\n| 112 | D_lc-I-0-ax    |            |\n| 113 | D_lc-I-1-ax    |            |\n| 114 | D_lc-I-2-ax    |            |\n| 115 | D_lc-I-3-ax    |            |\n| 116 | D_lc-T-0-ax    |            |\n| 117 | D_lc-T-1-ax    |            |\n| 118 | D_lc-T-2-ax    |            |\n| 119 | D_lc-T-3-ax    |            |\n| 120 | D_lc-S-0-ax    |            |\n| 121 | D_lc-S-1-ax    |            |\n| 122 | D_lc-S-2-ax    |            |\n| 123 | D_lc-S-3-ax    |            |\n| 124 | D_lc-chi-0-eq  |            |\n| 125 | D_lc-chi-1-eq  |            |\n| 126 | D_lc-chi-2-eq  |            |\n| 127 | D_lc-chi-3-eq  |            |\n| 128 | D_lc-Z-0-eq    |            |\n| 129 | D_lc-Z-1-eq    |            |\n| 130 | D_lc-Z-2-eq    |            |\n| 131 | D_lc-Z-3-eq    |            |\n| 132 | D_lc-I-0-eq    |            |\n| 133 | D_lc-I-1-eq    |            |\n| 134 | D_lc-I-2-eq    |            |\n| 135 | D_lc-I-3-eq    |            |\n| 136 | D_lc-T-0-eq    |            |\n| 137 | D_lc-T-1-eq    |            |\n| 138 | D_lc-T-2-eq    |            |\n| 139 | D_lc-T-3-eq    |            |\n| 140 | D_lc-S-0-eq    |            |\n| 141 | D_lc-S-1-eq    |            |\n| 142 | D_lc-S-2-eq    |            |\n| 143 | D_lc-S-3-eq    |            |\n| 144 | mc-chi-0-all   |            |\n| 145 | mc-chi-1-all   |            |\n| 146 | mc-chi-2-all   |            |\n| 147 | mc-chi-3-all   |            |\n| 148 | mc-Z-0-all     |            |\n| 149 | mc-Z-1-all     |            |\n| 150 | mc-Z-2-all     |            |\n| 151 | mc-Z-3-all     |            |\n| 152 | mc-I-0-all     |            |\n| 153 | mc-I-1-all     |            |\n| 154 | mc-I-2-all     |            |\n| 155 | mc-I-3-all     |            |\n| 156 | mc-T-0-all     |            |\n| 157 | mc-T-1-all     |            |\n| 158 | mc-T-2-all     |            |\n| 159 | mc-T-3-all     |            |\n| 160 | mc-S-0-all     |            |\n| 161 | mc-S-1-all     |            |\n| 162 | mc-S-2-all     |            |\n| 163 | mc-S-3-all     |            |\n| 164 | D_mc-chi-0-all |            |\n| 165 | D_mc-chi-1-all |            |\n| 166 | D_mc-chi-2-all |            |\n| 167 | D_mc-chi-3-all |            |\n| 168 | D_mc-Z-0-all   |            |\n| 169 | D_mc-Z-1-all   |            |\n| 170 | D_mc-Z-2-all   |            |\n| 171 | D_mc-Z-3-all   |            |\n| 172 | D_mc-I-0-all   |            |\n| 173 | D_mc-I-1-all   |            |\n| 174 | D_mc-I-2-all   |            |\n| 175 | D_mc-I-3-all   |            |\n| 176 | D_mc-T-0-all   |            |\n| 177 | D_mc-T-1-all   |            |\n| 178 | D_mc-T-2-all   |            |\n| 179 | D_mc-T-3-all   |            |\n| 180 | D_mc-S-0-all   |            |\n| 181 | D_mc-S-1-all   |            |\n| 182 | D_mc-S-2-all   |            |\n| 183 | D_mc-S-3-all   |            |
```
(['misc-dent-ax',
  'misc-charge-ax',
  'misc-dent-eq',
  'misc-charge-eq',
  'f-chi-0-all',
  'f-chi-1-all',
  'f-chi-2-all',
  'f-chi-3-all',
  'f-Z-0-all',
  'f-Z-1-all',
  'f-Z-2-all',
  'f-Z-3-all',
  'f-I-0-all',
  'f-I-1-all',
  'f-I-2-all',
  'f-I-3-all',
  'f-T-0-all',
  'f-T-1-all',
  'f-T-2-all',
  'f-T-3-all',
  'f-S-0-all',
  'f-S-1-all',
  'f-S-2-all',
  'f-S-3-all',
  'f-chi-0-ax',
  'f-chi-1-ax',
  'f-chi-2-ax',
  'f-chi-3-ax',
  'f-Z-0-ax',
  'f-Z-1-ax',
  'f-Z-2-ax',
  'f-Z-3-ax',
  'f-I-0-ax',
  'f-I-1-ax',
  'f-I-2-ax',
  'f-I-3-ax',
  'f-T-0-ax',
  'f-T-1-ax',
  'f-T-2-ax',
  'f-T-3-ax',
  'f-S-0-ax',
  'f-S-1-ax',
  'f-S-2-ax',
  'f-S-3-ax',
  'f-chi-0-eq',
  'f-chi-1-eq',
  'f-chi-2-eq',
  'f-chi-3-eq',
  'f-Z-0-eq',
  'f-Z-1-eq',
  'f-Z-2-eq',
  'f-Z-3-eq',
  'f-I-0-eq',
  'f-I-1-eq',
  'f-I-2-eq',
  'f-I-3-eq',
  'f-T-0-eq',
  'f-T-1-eq',
  'f-T-2-eq',
  'f-T-3-eq',
  'f-S-0-eq',
  'f-S-1-eq',
  'f-S-2-eq',
  'f-S-3-eq',
  'lc-chi-0-ax',
  'lc-chi-1-ax',
  'lc-chi-2-ax',
  'lc-chi-3-ax',
  'lc-Z-0-ax',
  'lc-Z-1-ax',
  'lc-Z-2-ax',
  'lc-Z-3-ax',
  'lc-I-0-ax',
  'lc-I-1-ax',
  'lc-I-2-ax',
  'lc-I-3-ax',
  'lc-T-0-ax',
  'lc-T-1-ax',
  'lc-T-2-ax',
  'lc-T-3-ax',
  'lc-S-0-ax',
  'lc-S-1-ax',
  'lc-S-2-ax',
  'lc-S-3-ax',
  'lc-chi-0-eq',
  'lc-chi-1-eq',
  'lc-chi-2-eq',
  'lc-chi-3-eq',
  'lc-Z-0-eq',
  'lc-Z-1-eq',
  'lc-Z-2-eq',
  'lc-Z-3-eq',
  'lc-I-0-eq',
  'lc-I-1-eq',
  'lc-I-2-eq',
  'lc-I-3-eq',
  'lc-T-0-eq',
  'lc-T-1-eq',
  'lc-T-2-eq',
  'lc-T-3-eq',
  'lc-S-0-eq',
  'lc-S-1-eq',
  'lc-S-2-eq',
  'lc-S-3-eq',
  'D_lc-chi-0-ax',
  'D_lc-chi-1-ax',
  'D_lc-chi-2-ax',
  'D_lc-chi-3-ax',
  'D_lc-Z-0-ax',
  'D_lc-Z-1-ax',
  'D_lc-Z-2-ax',
  'D_lc-Z-3-ax',
  'D_lc-I-0-ax',
  'D_lc-I-1-ax',
  'D_lc-I-2-ax',
  'D_lc-I-3-ax',
  'D_lc-T-0-ax',
  'D_lc-T-1-ax',
  'D_lc-T-2-ax',
  'D_lc-T-3-ax',
  'D_lc-S-0-ax',
  'D_lc-S-1-ax',
  'D_lc-S-2-ax',
  'D_lc-S-3-ax',
  'D_lc-chi-0-eq',
  'D_lc-chi-1-eq',
  'D_lc-chi-2-eq',
  'D_lc-chi-3-eq',
  'D_lc-Z-0-eq',
  'D_lc-Z-1-eq',
  'D_lc-Z-2-eq',
  'D_lc-Z-3-eq',
  'D_lc-I-0-eq',
  'D_lc-I-1-eq',
  'D_lc-I-2-eq',
  'D_lc-I-3-eq',
  'D_lc-T-0-eq',
  'D_lc-T-1-eq',
  'D_lc-T-2-eq',
  'D_lc-T-3-eq',
  'D_lc-S-0-eq',
  'D_lc-S-1-eq',
  'D_lc-S-2-eq',
  'D_lc-S-3-eq',
  'mc-chi-0-all',
  'mc-chi-1-all',
  'mc-chi-2-all',
  'mc-chi-3-all',
  'mc-Z-0-all',
  'mc-Z-1-all',
  'mc-Z-2-all',
  'mc-Z-3-all',
  'mc-I-0-all',
  'mc-I-1-all',
  'mc-I-2-all',
  'mc-I-3-all',
  'mc-T-0-all',
  'mc-T-1-all',
  'mc-T-2-all',
  'mc-T-3-all',
  'mc-S-0-all',
  'mc-S-1-all',
  'mc-S-2-all',
  'mc-S-3-all',
  'D_mc-chi-0-all',
  'D_mc-chi-1-all',
  'D_mc-chi-2-all',
  'D_mc-chi-3-all',
  'D_mc-Z-0-all',
  'D_mc-Z-1-all',
  'D_mc-Z-2-all',
  'D_mc-Z-3-all',
  'D_mc-I-0-all',
  'D_mc-I-1-all',
  'D_mc-I-2-all',
  'D_mc-I-3-all',
  'D_mc-T-0-all',
  'D_mc-T-1-all',
  'D_mc-T-2-all',
  'D_mc-T-3-all',
  'D_mc-S-0-all',
  'D_mc-S-1-all',
  'D_mc-S-2-all',
  'D_mc-S-3-all'],
 [False,
  False,
  False,
  False,
  467.7931999999995,
  1029.6938000000002,
  1735.9089999999992,
  2051.5000000000014,
  3065.0,
  4934.0,
  8524.0,
  10066.0,
  82.0,
  170.0,
  300.0,
  348.0,
  470.0,
  1160.0,
  1696.0,
  2192.0,
  30.667700000000032,
  77.58759999999997,
  122.92180000000006,
  152.37300000000005,
  1.7689000000000001,
  10.8262,
  25.575900000000004,
  35.910000000000004,
  1600.0,
  760.0,
  1800.0,
  2040.0,
  1.0,
  3.0,
  7.0,
  11.0,
  9.0,
  30.0,
  60.0,
  90.0,
  2.3716,
  3.5265999999999997,
  8.208200000000001,
  11.195800000000004,
  0.0,
  -4.1499999999999995,
  -9.919999999999998,
  -12.369999999999997,
  0.0,
  101.0,
  235.0,
  389.0,
  0.0,
  0.0,
  0.0,
  0.0,
  0.0,
  -1.0,
  1.0,
  3.0,
  0.0,
  2.33,
  5.449999999999999,
  9.669999999999998])
```
### Scripts and Files:

[RACS_tutorial_full_complex.ipynb](RACS_tutorial_full_complex.ipynb)