
<h1 align="center">
  <a href=""><img src="https://github.com/Bin-Cao/TCGPR/assets/86995074/28f69830-4ece-43b3-a887-e78fdb25bcab" alt="WPEM" width="150"></a>
  <br>
  <b>PyWPEM</b>
  <br>
</h1>

<p align="center">
  Python Toolkit for XRD Simulation, Analysis, and Refinement.
</p>

<p align="center">
  <a href="https://pyxplore.netlify.app/">Documentation</a> | <a href="#">Paper (Coming Soon)</a>
</p>

[View package usage statistics / download counts](https://www.pepy.tech/projects/PyXplore)
---

## 📦 Module Overview

```text
PyWPEM/
├── __init__.py
├── WPEM.py
│
├── Amorphous/
│   ├── fitting/
│   │   ├── __init__.py
│   │   └── AmorphousFitting.py
│   └── QuantitativeCalculation/
│       ├── __init__.py
│       └── AmorphousRDF.py
│
├── Background/
│   ├── __init__.py
│   └── BacDeduct.py
│
├── DecomposePlot/
│   ├── __init__.py
│   └── plot.py
│
├── EMBraggOpt/
│   ├── __init__.py
│   ├── EMBraggSolver.py
│   ├── BraggLawDerivation.py
│   └── WPEMFuns/
│       ├── __init__.py
│       └── SolverFuns.py
│
├── Extinction/
│   ├── __init__.py
│   ├── CifReader.py
│   ├── XRDpre.py
│   ├── wyckoff/
│   │   ├── __init__.py
│   │   └── wyckoff_dict.py
│   └── m3gnet/
│
├── GraphStructure/
│   ├── __init__.py
│   └── graph.py
│
├── Plot/
│   ├── __init__.py
│   └── UnitCell.py
│
├── Refinement/
│   ├── __init__.py
│   └── VolumeFractionDertermination.py
│
├── StructureOpt/
│   ├── __init__.py
│   └── SiteOpt.py
│
├── XRDSimulation/
│   ├── __init__.py
│   ├── Simulation.py
│   └── DiffractionGrometry/
│       ├── __init__.py
│       └── atom.py
│
├── WPEMXAS/
│   ├── __init__.py
│   ├── EXAFS.py
│   └── fftdemo.ipynb
│
├── WPEMXPS/
│   ├── __init__.py
│   └── XPSEM.py
│
└── refs/
    ├── International_Union_of_Crystallography.pdf
    └── WPEM_Manual.pdf
```

---

## 📊 Tables & Figures

<p align="center">
  <img src="https://github.com/Bin-Cao/PyWPEM/assets/86995074/4a41f979-ff0c-48d7-8830-d7638811aad2" alt="WPEM Table 1" width="650">
</p>

<p align="center">
  <img src="https://github.com/Bin-Cao/PyWPEM/assets/86995074/a04b60fd-f9b2-4b2d-bc1a-c8227d9dc811" alt="WPEM Table 2" width="650">
</p>

---

## 📚 Citation

If you use this toolkit in your research, please cite:

```bibtex
@misc{cao2025pyxplore,
  author       = {Bin Cao and Tong-Yi Zhang},
  title        = {PyXplore (Revision 56c956f)},
  year         = {2025},
  url          = {https://huggingface.co/datasets/caobin/PyXplore},
  doi          = {10.57967/hf/6055},
  publisher    = {Hugging Face}
}

@article{CAO2024,
  author = "Bin CAO and Tongyi ZHANG",
  title = "{WPEM manual}",
  year = "2024",
  month = "12",
  url = "https://figshare.com/articles/dataset/WPEM_manual/28078985",
  doi = "10.6084/m9.figshare.28078985.v3"
}

@patent{zhang2025em_xrd,
  author       = {Tong-Yi Zhang and Bin Cao and Zhenjie Feng and Qiling Xiao and Zihan Wang and Qian Zhang and Jiahao Wang},
  title        = {A Full Spectrum Line Fitting Method for Powder X-ray Diffraction Patterns Based on Statistical Modeling and Expectation-Maximization Algorithm},
  type         = {Patent},
  number       = {ZL202210408314.X},
  national     = {CN},
  year         = {2025},
  note         = {Authorization No.: CN 114972185 B, Authorized on April 11, 2025},
}
```
==Table of space groups in 3 dimensions==
{{further|List of space groups}}

{| class="wikitable" style="text-align:center;"
|- 
! rowspan=2 width=60  | [[Space group#Notation|{{abbr|№|Space group number}}]]
! rowspan=2 width=100 | [[Crystal system]], <br/>(count), <br/>Bravais lattice
! rowspan=1 colspan=5 | [[Crystallographic point group|Point group]]
! rowspan=2           | Space groups (international short symbol)
|- 
! [[Hermann–Mauguin notation|Int'l]]
! [[Schönflies notation|Schön.]]
! [[Orbifold notation|Orbifold]]
! [[Coxeter notation|Cox.]]
! [[Group order|Ord.]]
|- style="background-color:white;"
! 1
|rowspan=2|[[Triclinic]]<BR>(2)<BR>[[File:Triclinic.svg|50px]]
| 1 || C<sub>1</sub>||11||[&nbsp;]<sup>+</sup>||1
| style="text-align:left;" | P1
|- style="background-color:white;"
! 2
| {{overline|1}}|| C<sub>i</sub>||1×||[2<sup>+</sup>,2<sup>+</sup>]||2
| style="text-align:left;" |P{{overline|1}} 
|-
! 3–5
|rowspan=3|[[Monoclinic]]<BR>(13)<BR>[[File:Monoclinic.svg|40px]][[File:Base-centered monoclinic.svg|40px]]
| 2 || C<sub>2</sub> || 22|| [2]<sup>+</sup> || 2
| style="text-align:left;" |P2, P2<sub>1</sub><BR>C2
|-
! 6–9
| m|| C<sub>s</sub>|| *11|| [&nbsp;]||2
| style="text-align:left;" |Pm, Pc<BR>Cm, Cc 
|-
! 10–15
| 2/m|| C<sub>2h</sub>|| 2*|| [2,2<sup>+</sup>]||4
| style="text-align:left;" |P2/m, P2<sub>1</sub>/m<BR>C2/m,  P2/c, P2<sub>1</sub>/c<BR>C2/c 
|- style="background-color:white;"
! 16–24
|rowspan=3|[[Orthorhombic]]<BR>(59)<BR>[[File:Orthorhombic.svg|40px]][[File:Orthorhombic-body-centered.svg|40px]]<BR>[[File:Orthorhombic-base-centered.svg|40px]][[File:Orthorhombic-face-centered.svg|40px]]
| 222 ||  D<sub>2</sub>|| 222|| [2,2]<sup>+</sup>||4
| style="text-align:left;" |P222, P222<sub>1</sub>, P2<sub>1</sub>2<sub>1</sub>2, P2<sub>1</sub>2<sub>1</sub>2<sub>1</sub><br>C222<sub>1</sub>, C222<br>F222<br>I222, I2<sub>1</sub>2<sub>1</sub>2<sub>1</sub> 
|- style="background-color:white;"
! 25–46
| mm2||  C<sub>2v</sub>|| *22|| [2]||4
| style="text-align:left;" |Pmm2, Pmc<!-- not a PMCID-->2<sub>1</sub>, Pcc2, Pma2, Pca2<sub>1</sub>, Pnc2, Pmn2<sub>1</sub>, Pba2, Pna2<sub>1</sub>, Pnn2<BR>Cmm2, Cmc2<sub>1</sub>, Ccc2, Amm2, Aem2, Ama2, Aea2<BR>Fmm2, Fdd2<BR>Imm2, Iba2, Ima2 
|- style="background-color:white;"
!  47–74
| mmm||  D<sub>2h</sub>|| *222|| [2,2]||8
| style="text-align:left;" |Pmmm, Pnnn, Pccm, Pban, Pmma, Pnna, Pmna, Pcca, Pbam, Pccn, Pbcm, Pnnm, Pmmn, Pbcn, Pbca, Pnma<BR>Cmcm, Cmce, Cmmm, Cccm, Cmme, Ccce<BR>Fmmm, Fddd<BR>Immm, Ibam, Ibca, Imma 
|-
! 75–80
|rowspan=7| [[Tetragonal]]<BR>(68)<BR>[[File:Tetragonal.svg|45px]]<BR>[[File:Tetragonal-body-centered.svg|45px]]
| 4|| C<sub>4</sub>||44||[4]<sup>+</sup>||4
| style="text-align:left;" |P4,  P4<sub>1</sub>, P4<sub>2</sub>, P4<sub>3</sub>, I4, I4<sub>1</sub> 
|-
! 81–82
| {{overline|4}}|| S<sub>4</sub>||2×||[2<sup>+</sup>,4<sup>+</sup>]||4
| style="text-align:left;" |P{{overline|4}}, I{{overline|4}} 
|-
! 83–88
| 4/m|| C<sub>4h</sub>||4*||[2,4<sup>+</sup>]||8
| style="text-align:left;" |P4/m, P4<sub>2</sub>/m, P4/n, P4<sub>2</sub>/n<BR>I4/m, I4<sub>1</sub>/a 
|-
! 89–98
|  422 ||  D<sub>4</sub>||224||[2,4]<sup>+</sup>||8
| style="text-align:left;" |P422, P42<sub>1</sub>2, P4<sub>1</sub>22, P4<sub>1</sub>2<sub>1</sub>2, P4<sub>2</sub>22, P4<sub>2</sub>2<sub>1</sub>2, P4<sub>3</sub>22, P4<sub>3</sub>2<sub>1</sub>2<BR>I422, I4<sub>1</sub>22 
|-
!  99–110
|  4mm||  C<sub>4v</sub>||*44||[4]||8
| style="text-align:left;" |P4mm, P4bm, P4<sub>2</sub>cm, P4<sub>2</sub>nm, P4cc, P4nc, P4<sub>2</sub>mc, P4<sub>2</sub>bc<BR>I4mm, I4cm, I4<sub>1</sub>md, I4<sub>1</sub>cd 
|-
! 111–122
|  {{overline|4}}2m||  D<sub>2d</sub>||2*2||[2<sup>+</sup>,4]||8
| style="text-align:left;" |P{{overline|4}}2m, P{{overline|4}}2c, P{{overline|4}}2<sub>1</sub>m, P{{overline|4}}2<sub>1</sub>c, P{{overline|4}}m2, P{{overline|4}}c2, P{{overline|4}}b2, P{{overline|4}}n2<BR>I{{overline|4}}m2, I{{overline|4}}c2, I{{overline|4}}2m, I{{overline|4}}2d 
|-
!  123–142
|  4/mmm||  D<sub>4h</sub>||*224||[2,4]||16
| style="text-align:left;" |P4/mmm, P4/mcc, P4/nbm, P4/nnc, P4/mbm, P4/mnc, P4/nmm, P4/ncc, P4<sub>2</sub>/mmc, P4<sub>2</sub>/mcm, P4<sub>2</sub>/nbc, P4<sub>2</sub>/nnm, P4<sub>2</sub>/mbc, P4<sub>2</sub>/mnm, P4<sub>2</sub>/nmc, P4<sub>2</sub>/ncm<BR>I4/mmm, I4/mcm, I4<sub>1</sub>/amd, I4<sub>1</sub>/acd
|- bgcolor=#ffffff
! 143–146
| rowspan=5|[[Trigonal]]<BR>(25)<BR>[[File:Hexagonal latticeR.svg|60px]][[File:Hexagonal latticeFRONT.svg|60px]]
| 3|| C<sub>3</sub>||33||[3]<sup>+</sup>||3
| style="text-align:left;" |P3, P3<sub>1</sub>, P3<sub>2</sub><BR>R3 
|- style="background-color:white;"
! 147–148
| {{overline|3}}|| S<sub>6</sub>||3×||[2<sup>+</sup>,6<sup>+</sup>]||6
| style="text-align:left;" |P{{overline|3}}, R{{overline|3}} 
|- style="background-color:white;"
! 149–155
| 32|| D<sub>3</sub>||223||[2,3]<sup>+</sup>||6
| style="text-align:left;" |P312, P321, P3<sub>1</sub>12, P3<sub>1</sub>21, P3<sub>2</sub>12, P3<sub>2</sub>21<BR>R32 
|- style="background-color:white;"
! 156–161
| 3m|| C<sub>3v</sub>||*33||[3]||6
| style="text-align:left;" |P3m1, P31m, P3c1, P31c<BR>R3m, R3c 
|- bgcolor=#ffffff
! 162–167
| {{overline|3}}m|| D<sub>3d</sub>||2*3||[2<sup>+</sup>,6]||12
| style="text-align:left;" |P{{overline|3}}1m, P{{overline|3}}1c, P{{overline|3}}m1, P{{overline|3}}c1<BR>R{{overline|3}}m, R{{overline|3}}c
|-
! 168–173
|rowspan=7| [[Hexagonal crystal system|Hexagonal]]<BR>(27)<BR>[[File:Hexagonal latticeFRONT.svg|60px]]
| 6|| C<sub>6</sub>||66||[6]<sup>+</sup>||6
| style="text-align:left;" |P6, P6<sub>1</sub>, P6<sub>5</sub>, P6<sub>2</sub>, P6<sub>4</sub>, P6<sub>3</sub> 
|-
! 174
| {{overline|6}}|| C<sub>3h</sub>||3*||[2,3<sup>+</sup>]||6
| style="text-align:left;" |P{{overline|6}}
|-
! 175–176
| 6/m|| C<sub>6h</sub>||6*||[2,6<sup>+</sup>]||12
| style="text-align:left;" |P6/m, P6<sub>3</sub>/m 
|-
! 177–182
| 622|| D<sub>6</sub>||226||[2,6]<sup>+</sup>||12
| style="text-align:left;" |P622, P6<sub>1</sub>22, P6<sub>5</sub>22, P6<sub>2</sub>22, P6<sub>4</sub>22, P6<sub>3</sub>22 
|-
! 183–186
| 6mm|| C<sub>6v</sub>||*66||[6]||12
| style="text-align:left;" |P6mm, P6cc, P6<sub>3</sub>cm, P6<sub>3</sub>mc 
|-
! 187–190
| {{overline|6}}m2|| D<sub>3h</sub>||*223||[2,3]||12
| style="text-align:left;" |P{{overline|6}}m2, P{{overline|6}}c2, P{{overline|6}}2m, P{{overline|6}}2c 
|-
! 191–194
| 6/mmm|| D<sub>6h</sub>||*226||[2,6]||24
| style="text-align:left;" |P6/mmm, P6/mcc, P6<sub>3</sub>/mcm, P6<sub>3</sub>/mmc 
|- style="background-color:white;"
! 195–199
| rowspan=5|[[Cubic crystal system|Cubic]]<BR>(36)<BR>[[Image:Cubic.svg|60px]]<BR>[[Image:Cubic-body-centered.svg|60px]]<BR>[[Image:Cubic-face-centered.svg|60px]]

| 23|| T||332||[3,3]<sup>+</sup>||12
| style="text-align:left;" |P23, F23, I23<BR>P2<sub>1</sub>3, I2<sub>1</sub>3
|- style="background-color:white;"
! 200–206
| m{{overline|3}}|| T<sub>h</sub>|| 3*2||[3<sup>+</sup>,4]||24
| style="text-align:left;" |Pm{{overline|3}}, Pn{{overline|3}}, Fm{{overline|3}}, Fd{{overline|3}}, Im{{overline|3}}, Pa{{overline|3}}, Ia{{overline|3}}
|- style="background-color:white;"
! 207–214
| 432|| O||432||[3,4]<sup>+</sup>||24
| style="text-align:left;" |P432, P4<sub>2</sub>32<BR>F432, F4<sub>1</sub>32<BR>I432<BR>P4<sub>3</sub>32, P4<sub>1</sub>32, I4<sub>1</sub>32
|- style="background-color:white;"
! 215–220
| {{overline|4}}3m|| T<sub>d</sub>|| *332||[3,3]||24
| style="text-align:left;" |P{{overline|4}}3m, F{{overline|4}}3m, I{{overline|4}}3m<BR>P{{overline|4}}3n, F{{overline|4}}3c, I{{overline|4}}3d 
|- style="background-color:white;"
! 221–230
| m{{overline|3}}m|| O<sub>h</sub>|| *432||[3,4]||48
| style="text-align:left;" |Pm{{overline|3}}m, Pn{{overline|3}}n, Pm{{overline|3}}n, Pn{{overline|3}}m<BR>Fm{{overline|3}}m, Fm{{overline|3}}c, Fd{{overline|3}}m, Fd{{overline|3}}c<BR>Im{{overline|3}}m, Ia{{overline|3}}d
|}

Note: An ''e'' plane is a double glide plane, one having glides in two different directions. They are found in seven orthorhombic, five tetragonal and five cubic space groups, all with centered lattice. The use of the symbol ''e'' became official with {{harvtxt|Hahn|2002}}.

The lattice system can be found as follows. If the crystal system is not trigonal then the lattice system is of the same type. If the crystal system is trigonal, then the lattice system is hexagonal unless the space group is one of the seven in the [[rhombohedral lattice system]] consisting of the 7 trigonal space groups in the table above whose name begins with R. (The term rhombohedral system is also sometimes used as an alternative name for the whole trigonal system.) The [[hexagonal lattice system]] is larger than the hexagonal crystal system, and consists of the hexagonal crystal system together with the 18 groups of the trigonal crystal system other than the seven whose names begin with R.

The [[Bravais lattice]] of the space group is determined by the lattice system together with the initial letter of its name, which for the non-rhombohedral groups is P, I, F, A or C, standing for the principal, body centered, face centered, A-face centered or C-face centered lattices. There are seven rhombohedral space groups, with initial letter R.

