
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
# Table of space groups in 3 dimensions

| №       | Crystal system (count) | Int'l | Schön. | Orbifold | Cox. | Ord. | Space groups (short symbol) |
|---------|-------------------------|-------|--------|----------|------|------|-----------------------------|
| 1       | Triclinic (2)<br><img src="Triclinic.svg" width="50"> | 1 | C<sub>1</sub> | 11 | [&nbsp;]<sup>+</sup> | 1 | P1 |
| 2       | '' '' | $\bar{1}$ | C<sub>i</sub> | 1× | [2<sup>+</sup>,2<sup>+</sup>] | 2 | P$\bar{1}$ |
| 3–5     | Monoclinic (13)<br><img src="Monoclinic.svg" width="40"><img src="Base-centered monoclinic.svg" width="40"> | 2 | C<sub>2</sub> | 22 | [2]<sup>+</sup> | 2 | P2, P2<sub>1</sub><br>C2 |
| 6–9     | '' '' | m | C<sub>s</sub> | *11 | [&nbsp;] | 2 | Pm, Pc<br>Cm, Cc |
| 10–15   | '' '' | 2/m | C<sub>2h</sub> | 2* | [2,2<sup>+</sup>] | 4 | P2/m, P2<sub>1</sub>/m<br>C2/m, P2/c, P2<sub>1</sub>/c<br>C2/c |
| 16–24   | Orthorhombic (59)<br><img src="Orthorhombic.svg" width="40"><img src="Orthorhombic-body-centered.svg" width="40"><br><img src="Orthorhombic-base-centered.svg" width="40"><img src="Orthorhombic-face-centered.svg" width="40"> | 222 | D<sub>2</sub> | 222 | [2,2]<sup>+</sup> | 4 | P222, P222<sub>1</sub>, P2<sub>1</sub>2<sub>1</sub>2, P2<sub>1</sub>2<sub>1</sub>2<sub>1</sub><br>C222<sub>1</sub>, C222<br>F222<br>I222, I2<sub>1</sub>2<sub>1</sub>2<sub>1</sub> |
| 25–46   | '' '' | mm2 | C<sub>2v</sub> | *22 | [2] | 4 | Pmm2, Pmc2<sub>1</sub>, Pcc2, Pma2, Pca2<sub>1</sub>, Pnc2, Pmn2<sub>1</sub>, Pba2, Pna2<sub>1</sub>, Pnn2<br>Cmm2, Cmc2<sub>1</sub>, Ccc2, Amm2, Aem2, Ama2, Aea2<br>Fmm2, Fdd2<br>Imm2, Iba2, Ima2 |
| 47–74   | '' '' | mmm | D<sub>2h</sub> | *222 | [2,2] | 8 | Pmmm, Pnnn, Pccm, Pban, Pmma, Pnna, Pmna, Pcca, Pbam, Pccn, Pbcm, Pnnm, Pmmn, Pbcn, Pbca, Pnma<br>Cmcm, Cmce, Cmmm, Cccm, Cmme, Ccce<br>Fmmm, Fddd<br>Immm, Ibam, Ibca, Imma |
| 75–80   | Tetragonal (68)<br><img src="Tetragonal.svg" width="45"><img src="Tetragonal-body-centered.svg" width="45"> | 4 | C<sub>4</sub> | 44 | [4]<sup>+</sup> | 4 | P4, P4<sub>1</sub>, P4<sub>2</sub>, P4<sub>3</sub>, I4, I4<sub>1</sub> |
| 81–82   | '' '' | $\bar{4}$ | S<sub>4</sub> | 2× | [2<sup>+</sup>,4<sup>+</sup>] | 4 | P$\bar{4}$, I$\bar{4}$ |
| 83–88   | '' '' | 4/m | C<sub>4h</sub> | 4* | [2,4<sup>+</sup>] | 8 | P4/m, P4<sub>2</sub>/m, P4/n, P4<sub>2</sub>/n<br>I4/m, I4<sub>1</sub>/a |
| 89–98   | '' '' | 422 | D<sub>4</sub> | 224 | [2,4]<sup>+</sup> | 8 | P422, P42<sub>1</sub>2, P4<sub>1</sub>22, P4<sub>1</sub>2<sub>1</sub>2, P4<sub>2</sub>22, P4<sub>2</sub>2<sub>1</sub>2, P4<sub>3</sub>22, P4<sub>3</sub>2<sub>1</sub>2<br>I422, I4<sub>1</sub>22 |
| 99–110  | '' '' | 4mm | C<sub>4v</sub> | *44 | [4] | 8 | P4mm, P4bm, P4<sub>2</sub>cm, P4<sub>2</sub>nm, P4cc, P4nc, P4<sub>2</sub>mc, P4<sub>2</sub>bc<br>I4mm, I4cm, I4<sub>1</sub>md, I4<sub>1</sub>cd |
| 111–122 | '' '' | $\bar{4}$2m | D<sub>2d</sub> | 2*2 | [2<sup>+</sup>,4] | 8 | P$\bar{4}$2m, P$\bar{4}$2c, P$\bar{4}$2<sub>1</sub>m, P$\bar{4}$2<sub>1</sub>c, P$\bar{4}$m2, P$\bar{4}$c2, P$\bar{4}$b2, P$\bar{4}$n2<br>I$\bar{4}$m2, I$\bar{4}$c2, I$\bar{4}$2m, I$\bar{4}$2d |
| 123–142 | '' '' | 4/mmm | D<sub>4h</sub> | *224 | [2,4] | 16 | P4/mmm, P4/mcc, P4/nbm, P4/nnc, P4/mbm, P4/mnc, P4/nmm, P4/ncc, P4<sub>2</sub>/mmc, P4<sub>2</sub>/mcm, P4<sub>2</sub>/nbc, P4<sub>2</sub>/nnm, P4<sub>2</sub>/mbc, P4<sub>2</sub>/mnm, P4<sub>2</sub>/nmc, P4<sub>2</sub>/ncm<br>I4/mmm, I4/mcm, I4<sub>1</sub>/amd, I4<sub>1</sub>/acd |
| 143–146 | Trigonal (25)<br><img src="Hexagonal latticeR.svg" width="60"><img src="Hexagonal latticeFRONT.svg" width="60"> | 3 | C<sub>3</sub> | 33 | [3]<sup>+</sup> | 3 | P3, P3<sub>1</sub>, P3<sub>2</sub><br>R3 |
| 147–148 | '' '' | $\bar{3}$ | S<sub>6</sub> | 3× | [2<sup>+</sup>,6<sup>+</sup>] | 6 | P$\bar{3}$, R$\bar{3}$ |
| 149–155 | '' '' | 32 | D<sub>3</sub> | 223 | [2,3]<sup>+</sup> | 6 | P312, P321, P3<sub>1</sub>12, P3<sub>1</sub>21, P3<sub>2</sub>12, P3<sub>2</sub>21<br>R32 |
| 156–161 | '' '' | 3m | C<sub>3v</sub> | *33 | [3] | 6 | P3m1, P31m, P3c1, P31c<br>R3m, R3c |
| 162–167 | '' '' | $\bar{3}$m | D<sub>3d</sub> | 2*3 | [2<sup>+</sup>,6] | 12 | P$\bar{3}$1m, P$\bar{3}$1c, P$\bar{3}$m1, P$\bar{3}$c1<br>R$\bar{3}$m, R$\bar{3}$c |
| 168–173 | Hexagonal (27)<br><img src="Hexagonal latticeFRONT.svg" width="60"> | 6 | C<sub>6</sub> | 66 | [6]<sup>+</sup> | 6 | P6, P6<sub>1</sub>, P6<sub>5</sub>, P6<sub>2</sub>, P6<sub>4</sub>, P6<sub>3</sub> |
| 174     | '' '' | $\bar{6}$ | C<sub>3h</sub> | 3* | [2,3<sup>+</sup>] | 6 | P$\bar{6}$ |
| 175–176 | '' '' | 6/m | C<sub>6h</sub> | 6* | [2,6<sup>+</sup>] | 12 | P6/m, P6<sub>3</sub>/m |
| 177–182 | '' '' | 622 | D<sub>6</sub> | 226 | [2,6]<sup>+</sup> | 12 | P622, P6<sub>1</sub>22, P6<sub>5</sub>22, P6<sub>2</sub>22, P6<sub>4</sub>22, P6<sub>3</sub>22 |
| 183–186 | '' '' | 6mm | C<sub>6v</sub> | *66 | [6] | 12 | P6mm, P6cc, P6<sub>3</sub>cm, P6<sub>3</sub>mc |
| 187–190 | '' '' | $\bar{6}$m2 | D<sub>3h</sub> | *223 | [2,3] | 12 | P$\bar{6}$m2, P$\bar{6}$c2, P$\bar{6}$2m, P$\bar{6}$2c |
| 191–194 | '' '' | 6/mmm | D<sub>6h</sub> | *226 | [2,6] | 24 | P6/mmm, P6/mcc, P6<sub>3</sub>/mcm, P6<sub>3</sub>/mmc |
| 195–199 | Cubic (36)<br><img src="Cubic.svg" width="60"><img src="Cubic-body-centered.svg" width="60"><img src="Cubic-face-centered.svg" width="60"> | 23 | T | 332 | [3,3]<sup>+</sup> | 12 | P23, F23, I23<br>P2<sub>1</sub>3, I2<sub>1</sub>3 |
| 200–206 | '' '' | m$\bar{3}$ | T<sub>h</sub> | 3*2 | [3<sup>+</sup>,4] | 24 | Pm$\bar{3}$, Pn$\bar{3}$, Fm$\bar{3}$, Fd$\bar{3}$, Im$\bar{3}$, Pa$\bar{3}$, Ia$\bar{3}$ |
| 207–214 | '' '' | 432 | O | 432 | [3,4]<sup>+</sup> | 24 | P432, P4<sub>2</sub>32<br>F432, F4<sub>1</sub>32<br>I432<br>P4<sub>3</sub>32, P4<sub>1</sub>32, I4<sub>1</sub>32 |
| 215–220 | '' '' | $\bar{4}$3m | T<sub>d</sub> | *332 | [3,3] | 24 | P$\bar{4}$3m, F$\bar{4}$3m, I$\bar{4}$3m<br>P$\bar{4}$3n, F$\bar{4}$3c, I$\bar{4}$3d |
| 221–230 | '' '' | m$\bar{3}$m | O<sub>h</sub> | *432 | [3,4] | 48 | Pm$\bar{3}$m, Pn$\bar{3}$n, Pm$\bar{3}$n, Pn$\bar{3}$m<br>Fm$\bar{3}$m, Fm$\bar{3}$c, Fd$\bar{3}$m, Fd$\bar{3}$c<br>Im$\bar{3}$m, Ia$\bar{3}$d |
