---
title: "BIBSNet: A deep learning baby image brain segmentation network for MRI scans"
date: 2026-03-09
author: ["Hendrickson TJ", "Reiners P", "Moore LA", "Lundquist JT", "…", "Feczko E"]
description: "BIBSNet: A deep learning baby image brain segmentation network for MRI scans. Developmental Cognitive Neuroscience 79 (2026)."
summary: "Developmental Cognitive Neuroscience 79 (2026)"
editPost:
    URL: "https://doi.org/10.1016/j.dcn.2026.101706"
    Text: "Developmental Cognitive Neuroscience"
---

##### Links

- [Article (open access)](https://doi.org/10.1016/j.dcn.2026.101706)
- [Code (BIBSNet on GitHub)](https://github.com/DCAN-Labs/BIBSnet)

---

##### Abstract

**Objectives.** Brain tissue segmentation of infant magnetic resonance (MR) images is important for studying typical and atypical brain development. The infant brain undergoes rapid changes throughout the first years of postnatal life, making tissue segmentation difficult for most existing algorithms. We introduce a deep neural network BIBSNet (Baby and Infant Brain Segmentation Neural Network), an open-source model for robust and generalizable brain tissue segmentation leveraging data augmentation and a large sample size of manually annotated images.

**Experimental design.** Model training included MR brain images from 90 participants with an age range of 0-8 months (median age 4.6 months). Using manually annotated real images along with synthetic segmentation images produced using SynthSeg, the model was trained using a 10-fold procedure. Model performance was assessed by comparing BIBSNet, and joint label fusion (JLF) inferred segmentations to ground truth segmentations, and an ad-hoc analysis with iBeat inferred segmentation, using Dice Similarity Coefficient (DSC). Additionally, MR data along with the FreeSurfer compatible segmentations were processed with the DCAN labs infant-ABCD-BIDS processing pipeline from ground truth, JLF, and BIBSNet to produce anatomical and resting state functional derivatives to further assess model performance on processed derivatives.

**Principal observations.** BIBSNet outperforms JLF based on DSC comparisons especially with gray matter (BIBSNet = 0.849, JLF = 0.713) and white matter (BIBSNet = 0.862, JLF = 0.791). Additionally, with processed derived metrics, BIBSNet inferred segmentations outperforms JLF inferred segmentations across nearly all anatomical and functional metrics. Ad-hoc analyses of cortical segmentations - iBeat does not perform subcortical segmentations - showed that there is no significant difference between iBeat and BIBSNet segmentation for infants 0-5 months, but iBeat performed significantly better for infants 6-8 months.

**Conclusions.** BIBSNet shows marked improvement over JLF across all age groups analyzed. The BIBSNet model is 600x faster compared to JLF at segmentation inference, produces FreeSurfer-compatible segmentation labels, and can be easily included in other processing pipelines. BIBSNet provides a viable alternative for segmenting the brain in the earliest stages of development.

<small>Abstract reproduced from the publisher under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).</small>

---

##### Citation

Hendrickson TJ, Reiners P, Moore LA, **Lundquist JT**, Fayzullobekova B, Perrone AJ, Lee EG, Moser J, Day TKM, Alexopoulos D, Styner M, Kardan O, Chamberlain TA, Mummaneni A, Caldas HA, Bower B, Stoyell S, Martin T, Sung S, Fair EA, Carter K, Uriarte-Lopez J, Rueter AR, Yacoub E, Rosenberg MD, Smyser CD, Elison JT, Graham A, Fair DA, Feczko E. 2026. “BIBSNet: A deep learning baby image brain segmentation network for MRI scans.” *Developmental Cognitive Neuroscience* 79. [https://doi.org/10.1016/j.dcn.2026.101706](https://doi.org/10.1016/j.dcn.2026.101706)

```bibtex
@article{Hendrickson_2026,
  title = {BIBSNet: A deep learning baby image brain segmentation network for MRI scans},
  volume = {79},
  ISSN = {1878-9293},
  url = {http://dx.doi.org/10.1016/j.dcn.2026.101706},
  DOI = {10.1016/j.dcn.2026.101706},
  journal = {Developmental Cognitive Neuroscience},
  publisher = {Elsevier BV},
  author = {Hendrickson, Timothy J. and Reiners, Paul and Moore, Lucille A. and Lundquist, Jacob T. and Fayzullobekova, Begim and Perrone, Anders J. and Lee, Erik G. and Moser, Julia and Day, Trevor K.M. and Alexopoulos, Dimitrios and Styner, Martin and Kardan, Omid and Chamberlain, Taylor A. and Mummaneni, Anurima and Caldas, Henrique A. and Bower, Brad and Stoyell, Sally and Martin, Tabitha and Sung, Sooyeon and Fair, Ermias A. and Carter, Kenevan and Uriarte-Lopez, Jonathan and Rueter, Amanda R. and Yacoub, Essa and Rosenberg, Monica D. and Smyser, Christopher D. and Elison, Jed T. and Graham, Alice and Fair, Damien A. and Feczko, Eric},
  year = {2026}, month=June,
  pages = {101706}
}
```
