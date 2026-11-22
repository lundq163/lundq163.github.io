---
title: "Automated MRI QC"
date: 2026-08-13
context: "CDNI · Lead developer"
description: "Automated motion quality control for infant MRI: a 3D ResNet regressor that predicts a motion score from each scan."
summary: "CDNI · Lead developer"
cover:
    image: "cover.jpg"
    alt: "Diagram of the 3D ResNet layers used in the automated QC model"
---

##### Links

- [Code (automated-qc on GitHub)](https://github.com/DCAN-Labs/automated-qc)

---

##### Overview

An automated motion-QC system for infant brain MRI, built for the HEALthy Brain and Child Development (HBCD) study. A 3D ResNet regressor (MONAI, PyTorch) takes a T1- or T2-weighted scan and predicts its motion score, replacing most of the manual review each scan used to need. I started the project, designed the model, and wrote most of the code, including cross-validated training and TensorBoard monitoring on the university's HPC cluster.
