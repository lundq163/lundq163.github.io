---
title: "XCP-D: A robust pipeline for the post-processing of fMRI data"
date: 2024-08-13
author: ["Mehta K", "Salo T", "Madison TJ", "…", "Lundquist JT", "…", "Satterthwaite TD"]
description: "XCP-D: A robust pipeline for the post-processing of fMRI data. Imaging Neuroscience 2 (2024)."
summary: "Imaging Neuroscience 2 (2024)"
doi: "10.1162/imag_a_00257"
venue: imaging-neuroscience
---

##### Links

- [Article (open access)](https://doi.org/10.1162/imag_a_00257)
- [Code (XCP-D on GitHub)](https://github.com/PennLINC/xcp_d)

---

##### Abstract

Functional neuroimaging is an essential tool for neuroscience research. Pre-processing pipelines produce standardized, minimally pre-processed data to support a range of potential analyses. However, post-processing is not similarly standardized. While several options for post-processing exist, they may not support output from different pre-processing pipelines, may have limited documentation, and may not follow generally accepted data organization standards (e.g., Brain Imaging Data Structure (BIDS)). In response, we present XCP-D: a collaborative effort between PennLINC at the University of Pennsylvania and the DCAN lab at the University of Minnesota. XCP-D uses an open development model on GitHub and incorporates continuous integration testing; it is distributed as a Docker container or Apptainer image. XCP-D generates denoised BOLD images and functional derivatives from resting-state data in either NIfTI or CIFTI files following pre-processing with fMRIPrep, HCP, or ABCD-BIDS pipelines. Even prior to its official release, XCP-D has been downloaded >5,000 times from DockerHub. Together, XCP-D facilitates robust, scalable, and reproducible post-processing of fMRI data.

<small>Abstract reproduced from the publisher under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).</small>

