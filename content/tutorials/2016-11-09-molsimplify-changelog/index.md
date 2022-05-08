---
title: "molSimplify changelog"
subtitle: 

# Summary for listings and search engines
summary: 

# Link this post with a project
projects: []

# Date published
date: 2016-11-09

# Date updated
lastmod: 

# Is this an unpublished draft?
draft: false

# Show this page in the Featured widget?
featured: false

# Featured image
# Place an image named `featured.jpg/png` in this page's folder and customize its options here.
image:
  caption: 
  focal_point: ""
  placement: 2
  preview_only: false

authors:
- admin

tags:

categories:
- tutorials

---
This is a placeholder document for updates, small and large, that get committed to Github. New features will eventually get their own tutorials and will be linked from here.


9/5/18, NY: Transition state generation has been replaced with a rule-based tool and a new tutorial was added.


11/17/2017, TG: Tetradentate ligand alignment now attempts to minimize RMSD between the connecting atoms and the template. This procedure is more robust for nonplanar ligands but now requires that the connecting atoms be specified in a clockwise manner. The existing ligand dictionary has been updated


11/16/2017, TG: Minor bugfixes for conformer search, same conformer should be used for multiple copies of the same ligand in a complex. Slight tweaks to structgen(); subdirectories of bad complexes are now renamed instead of moved. Fixed bug with bbcombsdict that was preventing multiple structures from being generated in the same run. For multidentate smiles ligands, multiple conformers can now be generated in a single run by including -nconfs (number). 


11/15/2017, TG: Fixed Kabsch algorithm for RMSD, distance geometry routine now uses analytic gradients for the distance error function, tests now call the kabsch algorithm before computing RMSDs


11/13/2017, TG: A distance geometry conformer search routine has been implemented, and is the default for multidentate SMILES ligands. Ligands with predefined geometries that are stored as mol or xyz files in our database are not affected. Bidentate custom core replacement should now preserve atom ordering.


11/11/2017, TG: Added doxygen documentation.


11/9/2017, TG: mol3D.getBondedAtomsOct() now accepts a user-specified coordination number (previously defaulted to 6). Tweaked FF metal masking routine to account for intruding carbon atoms in tightly bound complexes.


