---
title: "Troubleshooting common problems with DFT+U"
subtitle:
aliases: /content/troubleshooting-common-problems-dftu
 

# Summary for listings and search engines
summary: 

# Link this post with a project
projects: []

# Date published
date: 2011-09-13

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
  placement: 1
  preview_only: false

authors:
- admin

tags:

categories:
- tutorials

---
Thus far, I have introduced how to calculate U from linear-response for both [single-site](../2011-05-31-calculating-hubbard-u "Calculating the Hubbard U") and [multiple-site](../2011-06-28-hubbard-u-multiple-sites "Hubbard U for multiple sites") systems.  However, there are a few practical issues you may run into when using DFT+U to study your system.  Here is an overview of the most common difficulties and some solutions.


 


**1. “Pseudopotential not yet inserted”: The atom you set for your Hubbard atom is not recognized as being valid by the code.**

First, is the element a conventional element for adding a Hubbard term? Most transition metals (first row: Ti-Zn, second row: Zr-Cd, and third row: Hf-Hg) are included in the latest version of PWscf by default as well as rare earths and the first-row elements H, C, N, O.  If your element is not listed above, you will need to add it to the list of allowed elements and specify the angular momentum of the Hubbard manifold in `set_hubbard_l.f90` and the approximate occupation of the manifold in `tabd.f90`. You may also want to consider whether a standard DFT+U approach is right for you if you don’t see the element of your Hubbard atom listed above. 


Next, if you think your element should be already included in the list above, but the code is still complaining, check your pseudopotential `PP_HEADER` for the line that specifies the ‘element’.  This line is how the code determines which element you are using in `set_hubbard_l`.  Make sure that the element is properly specified here.


Finally, check that the `Hubbard_U(n)` you have assigned corresponds to the  correct species listed under the `ATOMIC_SPECIES` namelist (i.e. the nth line there).  This is where the atom type ordering is set, not in the ordering of atoms in `ATOMIC_POSITIONS`.


 


**2. The occupation matrix looks wrong. Occupations are more than one, less than expected, or extremely unusual (e.g. NaN).**

Your maximum occupation should be one and the occupation matrix should reflect the electronic structure you expect your underlying system to have. You can test the occupations of a given pseudopotential by calculating the energy and occupation matrix of a single atom (you may want to turn off symmetry).  Occupations are by default calculated from projection onto the atomic orbital basis of the element encoded in the pseudopotential.  It is possible that the orbitals encoded in the pseudopotential would lead to non-normalized occupations.  The effect could be subtle (max occupations around 1.03) or quite noticeable (max occupations around 2.5); the former case may still yield reasonable results while the latter case will certainly give meaningless results if you try to do DFT+U calculations.


In order to fix occupations, you should change `U_projection_type` to `norm_atomic`.  Note that in this case you will not get forces or stresses (though there is a quick and dirty fix to get out meaningful forces as well), but you can use the norm_atomic results to compare against your results without normalization to see if there is a significant difference.  


In very rare cases, if you see very odd results for your occupation matrix, such as NaN results, it is likely you have a problem with your compiler or mkl library versions.  You should check the [PW\_forum archives](http://qe-forge.org/pipermail/pw_forum/ "PW_forum") for similar problems or consider using an older compiler if the compiler you are using is very new and relatively untested.


 


**3. The U from linear-response or self-consistent linear-response looks weird: Calculating U at slightly different geometries gives wildly different results, the calculated U looks too large or is the wrong sign.**

First, you’ll want to check that the linear-response and self-consistent U procedure was carried out with meaningful results.  We rely on starting from the density of a converged zero-alpha calculation and reconverge more tightly subsequent non-zero alpha calculations as outlined here.  If the code has trouble finding the original density files, the self-consistency on the first bare iteration is poor, or the total convergence thresholds and diagonalization thresholds are too loose, you may be introducing errors into your calculation.  The finite difference/linear regression step for U calculation are one step where you should be able to check the quality of your data. The data should be essentially perfectly linear.  



In cases with nearly full (e.g. d10, high spin d5) or nearly empty (e.g. d0) manifolds, the physics and chemistry of your system might mean that a DFT+U approach is not particularly meaningful.  Rigid shifts of the localized manifold in this case would yield very small values for reorganization in the occupations and the resulting inverse needed for DFT+U calculations would be subject to numerical noise[1].    



The easiest way to identify this behavior is to vary your geometry slightly and recalculate U and look at the scatter between U values.  If the variation is smooth, then the data are likely meaningful, but if the variation shows a lot of scatter then   



 


**4. The geometry changes a lot after adding the +U term and re-optimizing a structure with DFT+U.**

While DFT+U tends to fix hybridization problems due to overly-delocalized orbitals, it is possible for DFT+U, especially with large values of U, to over-elongate bonds in a way that causes DFT+U structures to look significantly different from DFT structures.  There are a few possible fixes:


A structurally-consistent U procedure involves calculating U at the DFT level, relaxing the structure with that DFT+U value, recomputing U on the DFT+U structure, and so on until a consistent result is achieved[2].  This approach can reduce problems with bond over-elongation significantly.


For systems with significant covalency - e.g. metal oxides or semiconductors - DFT+U theory alone is fundamentally incomplete, and an additional intersite or “+V” term is recommended with DFT+U+V[3].  In the case of MO2 triatomics (M=Mn, Fe, Co) pictured above, I showed that DFT+U structures were always linear, while the preferred experimental structure should be bent and this corresponded to the transition from a double well potential to a single well potential.  By constraining M-O bond lengths to DFT values, I recovered the angular dependence with DFT+U[4].  It was also possible to achieve the same effect through DFT+U+V[4].  MO2 is a key example where there is a strong mix between covalent bonding and localized 3d electrons.   


 


**5. The electronic state of large U DFT+U is different from low/no U DFT+U and the large U DFT+U is believed to be WRONG/RIGHT.**

Open shell systems often have multiple low-lying solutions and convergence for DFT (or DFT+U) to a given solution does not guarantee it is the lowest energy solution locally at a given geometry or globally.  It is possible that different solutions will converge most easily for different values of U.  Check out the [previous tutorial](../2011-08-09-low-lying-electronic-states "Low-lying electronic states") for more in-depth discussion of [low-lying electronic states](../2011-08-09-low-lying-electronic-states "Low-lying electronic states").  Importantly, one can take a solution converged at a high or a low value of U and use the converged density as a starting guess for a new calculation at a different value of U.  The main point to DFT+U is to improve the estimate of ground state electronic structure, but unfortunately this does not always guarantee that the state you first self-consistently converge to at high value U is the lowest energy state at that value of U.  



 


**6. I’d like to compare total energies of structures obtained at different values of U but the results cannot be compared.**

Fundamentally, standard implementations of DFT+U require that different structures be compared at some average value of U.  Shifts in the total energy at different values of U make it difficult to compare the total energies directly.  The direct incorporation of variation of U with position is most useful for systems that undergo a large geometric rearrangement.  Differences between applied U and self-consistent U on the order of 1-2 eV on average yield energy errors under 0.01-0.1 eV so the averaging of U values becomes most significant in outlying cases with large variations in U[5]. My recent research has focused on directly incorporating the variation in U with structure, and if you’re interested, [feel free to contact me](mailto:hjkulikATmitDOTedu?subject=Questions%20about%20DFT+U(R) "mailto:hjkulikATmitDOTedu?subject=Questions about DFT+U(R)") about my paper on DFT+U(R)[6].


 


I hope that this [tutorial](Tutorials "Tutorials") has helped you to better understand how to carry out DFT+U calculations smoothly and easily in [Quantum-ESPRESSO](http://www.quantum-espresso.org/ "http://www.quantum-espresso.org") and [PWscf](http://www.pwscf.org/ "http://www.pwscf.org").  Remember, a lot of the challenges you may associate with DFT+U may also simply be due to the fundamental challenges in correctly describing the electronic structure of open shell species. Please [email me](mailto:hjkulikATmitDOTedu?subject=Questions%20about%20low-lying%20electronic%20states%20tutorial "mailto:hjkulikATmitDOTedu?subject=Questions about low-lying electronic states tutorial") if you have any additional questions not answered here!


 


References:


[1] H. J. Kulik and N. Marzari. J. Chem. Phys. **133**, 114103 (2010).


[[2](http://prb.aps.org/abstract/PRB/v79/i12/e125124 "http://prb.aps.org/abstract/PRB/v79/i12/e125124")] H. Hsu, K. Umemoto, M. Cococcioni, and R. Wentzcovitch. Phys. Rev. B **79**, 125124 (2009). 


[[3](http://iopscience.iop.org/0953-8984/22/5/055602 "http://iopscience.iop.org/0953-8984/22/5/055602")] V. L. Campo Jr. and M. Cococcioni. J. Phys. Cond. Matt. **22**, 055602 (2010).  



[4] H. J. Kulik and N. Marzari. J. Chem. Phys. **134**, 094103 (2011).


[5] H. J. Kulik and N. Marzari. Chapter 14 in Fuel Cell Science: Theory, Fundamentals, and Bio-Catalysis eds. Jens Norskov and Andrzej Wiezcowski (2010).


[6] H. J. Kulik and N. Marzari “Accurate potential energy surfaces with a DFT+U(R) approach” J. Chem. Phys. **135**, 194105 (2011).


