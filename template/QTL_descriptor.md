# QTL data-set name

Dataset description. Should be one or multiple sentences.

## Contact

The lead analysts of the data and also the persons responsible for maintaining this document.

- Contact Name : Name
- Contact Email : Email
- Contact Affiliation : contact affilitation or institution
- Contact Role : contact role, one of principal investigator, submitter, primary contact

## Study Overview

**NOTE: the "study" here describes the QTL analysis**

- Study name : (i.e. XXX QTL)
- Study Description : (i.e. XXX QTL analysis using the FGC xQTL pipeline)

## Analysis Details

### Sample size tracking through the analysis workflow

|Step |Sample Size|Phenotype (for example gene) Count|
|-----|-----------|------------|
|Raw data|#|#|
|QC step 1|#|#|
|QC step 2|#|#|
|...|...|...|
|Data after pre-processing|#|#|


### QC and Normalization Details for Phenotype Data

Discribe the critera of phenotype QC and nomalization methods.

### Genotype parameters

(Default of our pipeline, please edit accordingly)

- Kinship coefficient for related individuals: 0.0625
- Minor allele count cutoff for single variant analysis: 5
- Variant level missingness threshold: 0.1
- Sample level missingness threshold: 0.1

### Covariate parameters

(Default of our pipeline, please edit accordingly)

PCA analysis:
- MAF for PCA: 0.01
- LD pruning via PLINK for PCA analysis: window 50, shift 10, r2 0.1
- Tolerance of missingness in covariates: 0.3
- number of pc that captured more than 70% PVE were kept

PEER analysis (Default values from PEER software):
- The number of max iteration: 1000
- Prior parameter Alpha_a: 0.001
- Prior parameter Alpha_b: 0.1
- Prior parameter Eps_a: 0.1
- Prior parameter Eps_b: 10.0
- Tolarance parameter tol: 0.001
- Tolarance parameter var_tol: 0.00001
- minimum variance explained criteria to drop factors while training r2_tol: False
- Convergence mode: "fast"

Final covariates: Sex, Age at death, PMI, PCs(#), PEER factors(#)

### TensorQTL accociation scan parameters

(Default of our pipeline, please edit accordingly)

- cis window for the up and downstream radius to analyze around the region of interest, in units of bp: 1000000
- Minor allele count cutoff: #
- N: (intersection of geno/cov/pheno)
- Minor allele frequency cutoff: MAC/(2.0*N)

## Links to analysis notebooks (below take pQTL notbooks as example)
See notebooks in:
- https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Wang_Columbia/knight/pqtl

The notebooks in this folder contain the commands and data wrangling codes for analysis of the pQTL data in ROSMAP.

Please list the links to analysis notebooks in the order you executed our pipeline:

### Association data preprocessing
phenotype preprocessing can be run in parallel but covariate preprocessing need to be done last since it requires both phenotype data and PCs from PCA in genotype preprocessing.
1. [Genotype processing](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/knight/pqtl/genotype_preprocessing.ipynb#L4) shows the commands used for genotype processing and preparation steps.
- Includes QC, PCA, and PCA result figures.
2. [Phenotype processing](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/pqtl/phenotype_preprocessing.ipynb) shows the commands used for the phenotype data processing and preparation steps.
- This notebook strated from some already cleaned data and covert them to bed format inputs taken by tensorQTL.
3. [Covariance processing](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/pqtl/covariate_processing.ipynb) shows the commands used for the covariate data processing and preparation steps.

### Association scan using TensorQTL and summary statistics standardization
4. [cis_pQTL_association.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/pqtl/cis_pqtl_association.ipynb) provides information about the TensorQTL cis association scan.
5. [trans_pQTL_association.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/pqtl/trans_pqtl_association.ipynb) provides information about the TensorQTL trans association scan.

### Fine-mapping with SuSiE model
6. [TAD_based_pQTL_finemapping.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/pqtl/pqtl-finemapping.ipynb) provides information about the fine mapping based on TAD region.
-  Includes the coommands for uni_susie.


Alternatively you can also use a somewhat free style as long as it is clear from your write-up where the notebooks are on github and what they are. Check out this section for an example of alternative style: https://github.com/cumc/fungen-xqtl-analysis/blob/main/data/descriptor/qtl/ROSMAP_DLPFC_ChIPSeq_H3K9ac_qtl.md#links-to-qtl-analysis-notebookss
- [processing duplicated ID](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/pqtl/duplicates_processing.ipynb) provides information about processing duplicated ID in pQTL data. 
- [processing missing data](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/pqtl/missForest.ipynb) provides information about processing missing data in pQTL data. 


## Dataset Details

(Edit from NIAGAD's metadata requirement, leave blank if not avaliable)

- Number of cases :
- Number of controls :
- Annotation information : one or more annotation sources specified as resource-version, // separated, e.g., Ensembl-v100//dbSNP-155
- Genotype level imputation : Required for QTL data or any GWAS summary statistics file, Yes/no with how imputation was done
- Imputation Panel : imputation panel used


### Path(s) to genotype matrix

Here please document the exact genotype matrix used for QTL calling. 

- Path(s) to the data on your local cluster where you analyzed the data. For example:
- Zhang Lab, `/restricted/projectnb/casa/skandoi/ROSMAP_DLPFC/genotype_partition/ROSMAP_NIA_WGS_plink_files/`
- NIAGADS FTP, `/ftp_fgc_xqtl/projects/...`
- This section may contain multiple locations in which case you can use bullet points to separate them. 
- If the lead analysts are from different institutes please include all the paths. 

A summary of the genotype data including size. We suggest using `ls -lh` command to show them. For example:

```
$ ls -lh *.{bim,bed,fam}
-rw-rw-r-- 1 gw gw  2.7M Apr  5  2017 ROSMAP_NIA_WGS.###.bed
-rw-rw-r-- 1 gw gw  2.7M Apr  5  2017 ROSMAP_NIA_WGS.###.bim
-rw-rw-r-- 1 gw gw  2.7M Apr  5  2017 ROSMAP_NIA_WGS.###.fam
```

### Path(s) to omics-data matrix

Here please document the exact omics-data matrix used for QTL calling.

- Path(s) to the data on your local cluster where you analyzed the data. For example:
- Zhang Lab, `/restricted/projectnb/casa/skandoi/ROSMAP_DLPFC/phenotype/`
- NIAGADS FTP, `/ftp_fgc_xqtl/projects/...`
- This section may contain multiple locations in which case you can use bullet points to separate them. 
- If the lead analysts are from different institutes please include all the paths. 

A summary of the phenotype data including size. We suggest using `ls -lh` command to show them. For example:

```
$ ls -lh *.tsv
-rw-rw-r-- 1 gw gw  2.7M Apr  5  2017 ROSMAP.###.tsv
```

### Path(s) to covariate data matrix

Here please document the exact covariate matrix used for QTL calling, **including selected covariates from sample attribute file, genotype PC and phenotype hidden counfounding factors computed in your previous analysis**

- Path(s) to the data on your local cluster where you analyzed the data. For example:
- Zhang Lab, `/restricted/projectnb/casa/skandoi/ROSMAP_DLPFC/covariate/`
- NIAGADS FTP, `/ftp_fgc_xqtl/projects/...`
- This section may contain multiple locations in which case you can use bullet points to separate them. 
- If the lead analysts are from different institutes please include all the paths. 

A summary of the phenotype data including size. We suggest using `ls -lh` command to show them. For example:

```
$ ls -lh *.tsv
-rw-rw-r-- 1 gw gw  2.7M Apr  5  2017 ROSMAP.###.tsv
```

### Path(s) to QTL results

### Path(s) to fine-mapping with SuSiE model

### Path(s) to fine-mapping with SuSiE RSS model

### Path(s) to colocalization with SuSiE-coloc
