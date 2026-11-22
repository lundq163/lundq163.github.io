---
title: "Automated Loes Scoring"
date: 2025-03-05
context: "CDNI · Project lead"
description: "Deep-learning Loes scoring of brain MRI for cerebral adrenoleukodystrophy (ALD)."
summary: "CDNI · Project lead"
cover:
    image: "cover.jpg"
    alt: "Scatter plot of actual versus predicted Loes scores"
---

##### Links

- [Code (loes-scoring-2 on GitHub)](https://github.com/DCAN-Labs/loes-scoring-2)

---

##### Overview

A deep-learning system that predicts the Loes score, a 0–35 MRI severity scale for cerebral adrenoleukodystrophy (ALD), a rare pediatric disease. Scans are normalized, skull-stripped, and registered before a 3D CNN regressor (MONAI) predicts the score, which supports tracking disease progression across sessions. I led the project, managing a senior developer and four neuroradiologists. This code supported the research behind our poster on automated MRI severity scoring, which won the Best Poster Award at the University of Minnesota's Rare Disease Day 2026.
