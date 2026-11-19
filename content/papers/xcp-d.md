---
title: "XCP-D: A robust pipeline for the post-processing of fMRI data"
date: 2024-08-13
author: ["Mehta K", "Salo T", "Madison TJ", "…", "Lundquist JT", "…", "Satterthwaite TD"]
description: "XCP-D: A robust pipeline for the post-processing of fMRI data. Imaging Neuroscience 2 (2024)."
summary: "Imaging Neuroscience 2 (2024)"
editPost:
    URL: "https://doi.org/10.1162/imag_a_00257"
    Text: "Imaging Neuroscience"
---

##### Links

- [Article (open access)](https://doi.org/10.1162/imag_a_00257)
- [Code (XCP-D on GitHub)](https://github.com/PennLINC/xcp_d)

---

##### Abstract

Functional neuroimaging is an essential tool for neuroscience research. Pre-processing pipelines produce standardized, minimally pre-processed data to support a range of potential analyses. However, post-processing is not similarly standardized. While several options for post-processing exist, they may not support output from different pre-processing pipelines, may have limited documentation, and may not follow generally accepted data organization standards (e.g., Brain Imaging Data Structure (BIDS)). In response, we present XCP-D: a collaborative effort between PennLINC at the University of Pennsylvania and the DCAN lab at the University of Minnesota. XCP-D uses an open development model on GitHub and incorporates continuous integration testing; it is distributed as a Docker container or Apptainer image. XCP-D generates denoised BOLD images and functional derivatives from resting-state data in either NIfTI or CIFTI files following pre-processing with fMRIPrep, HCP, or ABCD-BIDS pipelines. Even prior to its official release, XCP-D has been downloaded >5,000 times from DockerHub. Together, XCP-D facilitates robust, scalable, and reproducible post-processing of fMRI data.

<small>Abstract reproduced from the publisher under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).</small>

---

##### Citation

Mehta K, Salo T, Madison TJ, Adebimpe A, Bassett DS, Bertolero M, Cieslak M, Covitz S, Houghton A, Keller AS, **Lundquist JT**, Luo A, Miranda-Dominguez O, Nelson SM, Shafiei G, Shanmugan S, Shinohara RT, Smyser CD, Sydnor VJ, Weldon KB, Feczko E, Fair DA, Satterthwaite TD. 2024. “XCP-D: A robust pipeline for the post-processing of fMRI data.” *Imaging Neuroscience* 2. [https://doi.org/10.1162/imag_a_00257](https://doi.org/10.1162/imag_a_00257)

```bibtex
@article{Mehta_2024,
  title = {XCP-D: A robust pipeline for the post-processing of fMRI data},
  volume = {2},
  ISSN = {2837-6056},
  url = {http://dx.doi.org/10.1162/imag_a_00257},
  DOI = {10.1162/imag_a_00257},
  journal = {Imaging Neuroscience},
  publisher = {MIT Press},
  author = {Mehta, Kahini and Salo, Taylor and Madison, Thomas J. and Adebimpe, Azeez and Bassett, Danielle S. and Bertolero, Max and Cieslak, Matthew and Covitz, Sydney and Houghton, Audrey and Keller, Arielle S. and Lundquist, Jacob T. and Luo, Audrey and Miranda-Dominguez, Oscar and Nelson, Steve M. and Shafiei, Golia and Shanmugan, Sheila and Shinohara, Russell T. and Smyser, Christopher D. and Sydnor, Valerie J. and Weldon, Kimberly B. and Feczko, Eric and Fair, Damien A. and Satterthwaite, Theodore D.},
  year = {2024}
}
```
