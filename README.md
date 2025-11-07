
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
# Table of crystal systems

<img width="828" height="795" alt="Screenshot 2025-09-08 at 17 57 03" src="https://github.com/user-attachments/assets/8849335b-e8f2-45f8-8f61-83dec84a30aa" />


---

<table>
  <tr>
    <td width="160" align="center" valign="top">
      <img src="https://github.com/user-attachments/assets/7e77bd5a-42d6-45db-b8e6-2c82cac81b9d" width="140" style="border-radius: 50%;"/>
    </td>
    <td valign="top">
      <b>For any inquiries or assistance, feel free to contact Mr. CAO Bin at:</b><br>
      📧 Email: <a href="mailto:bcao686@connect.hkust-gz.edu.cn">bcao686@connect.hkust-gz.edu.cn</a><br><br>
      Cao Bin is a PhD candidate at the <b>Hong Kong University of Science and Technology (Guangzhou)</b>, 
      under the supervision of Professor <a href="https://gbaaa.org.hk/en-us/article/67">Zhang Tong-Yi</a>. His research focuses on 
      <b>AI for science</b>, especially intelligent crystal-structure analysis and discovery. 
      Learn more about his work on his 
      <a href="https://www.caobin.asia/">homepage</a>.
    </td>
  </tr>
</table>
