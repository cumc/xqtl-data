# MiGA multi-brain region gene expression

A genetic and transcriptomic resource comprised of 255 primary human microglia samples isolated ex vivo from four different brain regions of 100 human subjects with neurodegenerative, neurological, or neuropsychiatric disorders, as well as unaffected controls.

The human post-mortem brain samples were obtained from the Netherlands Brain Bank (NBB) and the Neuropathology Brain Bank and Research CoRE at Mount Sinai Hospital. The permission to collect human brain material was obtained from the Ethical Committee of the VU University Medical Center, Amsterdam, The Netherlands, and the Mount Sinai Institutional Review Board. For the Netherlands Brain bank, informed consent for autopsy, the use of brain tissue and accompanied clinical information for research purposes was obtained per donor ante-mortem.

## Contact

Travyse Edwards

## Study Overview

- Study information: `descriptor/study_info/MiGA.md`.
- Website&Logo : https://dss.niagads.org/sample-sets/snd10022/

## Dataset Description

### Raw data

- https://dss.niagads.org/datasets/ng00105/
- https://dss.niagads.org/studies/sa000018/


### Molecular phenotype matrices

We have gene expression data for four brain regions: medial frontal gyrus (GFM), superior temporal gyrus (GTS), thalamus (THA), and subventricular zone (SVZ). I have included information about the TPM matrices below for each brain region. The columns are sample names and the rows are gene ids. 

- GFM
  - Path: `/sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/rnaseq/GFM/sample-gfm.trimmed.clean.rnaseqc.low_expression_filtered.outlier_removed.tpm.gct.gz`
  - Columns: 75, Rows: 45814
- GTS
  - Path: `/sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/rnaseq/GTS/sample-gts.trimmed.clean.rnaseqc.low_expression_filtered.outlier_removed.tpm.gct.gz`
  - Columns: 63, Rows: 45472
- THA
  - Path: `/sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/rnaseq/THA/sample-tha.trimmed.clean.rnaseqc.low_expression_filtered.outlier_removed.tpm.gct.gz`
  - Columns: 61, Rows: 45461
- SVZ
  - Path: `/sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/rnaseq/SVZ/sample-svz.trimmed.clean.rnaseqc.low_expression_filtered.outlier_removed.tpm.gct.gz`
  - Columns: 53, Rows: 42086

File Sizes:
```
$ ls -lh
-rw-r--r-- 1 edwart10 LOAD  11M Sep 28 12:16 sample-gfm.trimmed.clean.rnaseqc.low_expression_filtered.outlier_removed.tpm.gct.gz
-rw-r--r-- 1 edwart10 LOAD  8.8M Sep 28 13:17 sample-gts.trimmed.clean.rnaseqc.low_expression_filtered.outlier_removed.tpm.gct.gz
-rw-r--r-- 1 edwart10 LOAD  8.6M Sep 28 13:17 sample-tha.trimmed.clean.rnaseqc.low_expression_filtered.outlier_removed.tpm.gct.gz
-rw-r--r-- 1 edwart10 LOAD 6.8M Sep 28 13:18 sample-svz.trimmed.clean.rnaseqc.low_expression_filtered.outlier_removed.tpm.gct.gz
```

### Other Key Files

TBD


## Links to omics data analysis notebooks

1. EDA: https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Marcora_MSSM/MiGA/data_overview.ipynb
2. [Molecular Phenotype Calling](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Marcora_MSSM/MiGA/molecular-phenotype-calling.ipynb)
3. [Genotype Preprocessing](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Marcora_MSSM/MiGA/genotype-preprocessing.ipynb)
4. [Phenotype Preprocessing](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Marcora_MSSM/MiGA/phenotype-preprocessing.ipynb)
5. [Covariate Preprocessing](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Marcora_MSSM/MiGA/covariate-preprocessing-age_sex.ipynb)
6. [Association Scan](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Marcora_MSSM/MiGA/association-scan-preprocessing-template-age_sex.ipynb)
