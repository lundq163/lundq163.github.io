---
title: "Automated MRI QC"
date: 2026-08-13
context: "MIDB · Jupyter Notebook, Python, Shell"
description: "Automated motion quality control for infant MRI: a 3D ResNet regressor that predicts a motion score from each scan."
summary: "MIDB · Jupyter Notebook, Python, Shell"
cover:
    image: "resnet_architecture.png"
    alt: "Diagram of the automated QC model's 3D ResNet architecture"
---

##### Links

- [Code (automated-qc on GitHub)](https://github.com/DCAN-Labs/automated-qc)

---

##### Overview

An automated motion-QC system for infant brain MRI, built for the HEALthy Brain and Child Development (HBCD) study. A 3D ResNet regressor (MONAI, PyTorch) takes a T1- or T2-weighted scan and predicts its motion score, replacing most of the manual review each scan used to need. Training uses cross-validation, with TensorBoard monitoring on the university's HPC cluster.
