# ROSMAP DLPFC alternative splicing QTL

Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) DLPFC alternative splicing. 

Please refer to [this document](../study_info/ROSMAP.md) for an overview of the ROSMAP project.

## Contact

Shrishtee Kandoi and Xuanhe Chen (xuanhechenxhc@163.com)

## Study Overview
 
- Study name : ROSMAP DLPFC sQTL
- Study Description : Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) sQTL analysis summary statistics using the FGC xQTL pipeline. 

Samples' phenotype information (sex, age, race etc.) can be found in ROSMAP metadata, see "Other information" section in [this document](../study_info/ROSMAP.md)

## Analysis Status

TransQTL association: Need to be performed.

## Analysis Details

### Sample size tracking through the analysis workflow

|Step |Sample Size|
|-----|-----------|
|Raw data|1141|
|After overlapping with ROSMAP WGS|839|

### QC and Normalization Details for Phenotype Data

In the case of leafcutter data, any features with over 40% missing values across samples were removed. The remaining missing values were replaced with the mean of existing values, and introns with less than 0.005 variation were eliminated. A scaled normalization was performed on each intron cluster (representing a row of leafcutter data), followed by Quantile-Quantile Normalization on each sample (representing a column of leafcutter data). In contrast, psichomics phenotype data underwent a different imputation approach; zero-imputation was performed to retain "no event detected" information, and only scaled normalization was applied to each event (row).

### Genotype parameters

- Kinship coefficient for related individuals: 0.0625
- Minor allele count cutoff for single variant analysis: 5
- Variant level missingness threshold: 0.1
- Sample level missingness threshold: 0.1
- HWE filter: 1e-06

### Covariate parameters

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
- Tolerance  parameter tol: 0.001
- Tolerance parameter var_tol: 0.00001
- minimum variance explained criteria to drop factors while training r2_tol: False
- Convergence mode: "fast"

Final covariates: Sex, Age at death, PMI, PCs(13), PEER factors(60)

### TensorQTL association scan parameters

- cis window for the up and downstream radius to analyze around the region of interest, in units of bp: 1000000
- Minor allele count cutoff: 5
- Minor allele frequency cutoff: 5/(2.0*592) = 0.00422297


## Links to QTL analysis notebooks

See notebooks in: 

- https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Zhang_BU/ROSMAP_DLPFC/

The notebooks in this folder contain the commands and data wrangling codes for analysis of the eQTL and sQTL data in ROSMAP. (data wrangling exist because not all data are processed using the xqtl-pipeline from the beginning and need to be reformatted to fit one intermediate step of the pipeline). Since the sQTL phenotype pre-processing used eQTL STAR alignment output, some of the early stage code are shared.

### Association data preprocessing

phenotype preprocessing and genotype preprocessing can be run in parallel but covariate preprocessing needs to be done last since it requires both phenotype data and PCs from PCA in genotype preprocessing.

- [genotype_qc.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Zhang_BU/ROSMAP_DLPFC/genotype/genotype_qc.ipynb) shows the commands used for genotype processing and preparation steps, including why we decided not to remove any outliers.
  - Also includes QC, PCA, and PCA result figures, some are inside the notebook and some are seperated PDF files. For example [leafcutter_PEER.diag.pdf](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Zhang_BU/ROSMAP_DLPFC/sQTL/leafcutter_PEER.diag.pdf) is the view of PCA result of the sQTL analysis.
- [phenotype_preprocessing_sqtl.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Zhang_BU/ROSMAP_DLPFC/sQTL/phenotype_preprocessing_sQTL.ipynb) shows the commands used for the phenotype data processing and preparation steps.
  - This notebook strated from some eQTL intermidiate output and convert them to bed format inputs taken by tensorQTL.
- [covariate_preprocessing_sQTL.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Zhang_BU/ROSMAP_DLPFC/sQTL/covariate_preprocessing_sQTL.ipynb) shows the commands used for the covariate data processing and preparation steps.
  - This includes PEER factor analysis steps and merging the PEER factors to covariates in raw data and PCA. 
  
### Association scan using TensorQTL and summary statistics standardization

- [association_scan_sQTL.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Zhang_BU/ROSMAP_DLPFC/sQTL/association_scan_sQTL.ipynb) provides information about the TensorQTL cis association scan.

### SuSiE univariate fine mapping

- [fine_mapping.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Zhang_BU/ROSMAP_DLPFC/sQTL/fine_mapping.ipynb) contains the workflow of sQTL univariate fine mapping using filterd psichomics data.


## Dataset Details

- Number of cases : 
- Number of controls :
- Annotation information : 
- Genotype level imputation : 
- Imputation Panel : 

### Path(s) to genotype matrix 

**output of genotype_qc.ipynb**

- BU cluster, `/restricted/projectnb/casa/skandoi/ROSMAP_DLPFC/genotype_partition/ROSMAP_NIA_WGS.leftnorm.filtered.filtered.plink_files_list.txt`
- Wang Lab, `/mnt/mfs/hgrcgrid/homes/zq2209/ROSMAP_NIA_WGS.leftnorm.filtered.filtered.plink_files_list.txt`

```
$ cd /mnt/vast/hpc/csg/molecular_phenotype_calling/genotype_arch/
$ ls -lh *.{bim,bed,fam}
-rw-r--r-- 1 hs3163 hs3163 220M Sep 29 15:09 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.10.bed
-rw-r--r-- 1 hs3163 hs3163  33M Sep 29 15:09 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.10.bim
-rw-r--r-- 1 hs3163 hs3163  23K Sep 29 15:09 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.10.fam
-rw-r--r-- 1 hs3163 hs3163 207M Sep 29 15:09 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.11.bed
-rw-r--r-- 1 hs3163 hs3163  31M Sep 29 15:09 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.11.bim
-rw-r--r-- 1 hs3163 hs3163  23K Sep 29 15:09 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.11.fam
-rw-r--r-- 1 hs3163 hs3163 207M Sep 29 15:10 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.12.bed
-rw-r--r-- 1 hs3163 hs3163  31M Sep 29 15:10 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.12.bim
-rw-r--r-- 1 hs3163 hs3163  23K Sep 29 15:10 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.12.fam
-rw-r--r-- 1 hs3163 hs3163 156M Sep 29 15:09 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.13.bed
-rw-r--r-- 1 hs3163 hs3163  23M Sep 29 15:09 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.13.bim
-rw-r--r-- 1 hs3163 hs3163  23K Sep 29 15:09 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.13.fam
-rw-r--r-- 1 hs3163 hs3163 141M Sep 29 15:07 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.14.bed
-rw-r--r-- 1 hs3163 hs3163  21M Sep 29 15:07 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.14.bim
-rw-r--r-- 1 hs3163 hs3163  23K Sep 29 15:07 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.14.fam
-rw-r--r-- 1 hs3163 hs3163 123M Sep 29 15:09 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.15.bed
-rw-r--r-- 1 hs3163 hs3163  18M Sep 29 15:09 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.15.bim
-rw-r--r-- 1 hs3163 hs3163  23K Sep 29 15:09 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.15.fam
-rw-r--r-- 1 hs3163 hs3163 137M Sep 29 15:10 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.16.bed
-rw-r--r-- 1 hs3163 hs3163  21M Sep 29 15:10 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.16.bim
-rw-r--r-- 1 hs3163 hs3163  23K Sep 29 15:10 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.16.fam
-rw-r--r-- 1 hs3163 hs3163 125M Sep 29 15:10 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.17.bed
-rw-r--r-- 1 hs3163 hs3163  19M Sep 29 15:10 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.17.bim
-rw-r--r-- 1 hs3163 hs3163  23K Sep 29 15:10 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.17.fam
-rw-r--r-- 1 hs3163 hs3163 121M Sep 29 15:11 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.18.bed
-rw-r--r-- 1 hs3163 hs3163  18M Sep 29 15:11 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.18.bim
-rw-r--r-- 1 hs3163 hs3163  23K Sep 29 15:11 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.18.fam
-rw-r--r-- 1 hs3163 hs3163 106M Sep 29 15:10 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.19.bed
-rw-r--r-- 1 hs3163 hs3163  16M Sep 29 15:10 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.19.bim
-rw-r--r-- 1 hs3163 hs3163  23K Sep 29 15:10 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.19.fam
-rw-r--r-- 1 hs3163 hs3163 345M Sep 29 15:08 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.1.bed
-rw-r--r-- 1 hs3163 hs3163  50M Sep 29 15:08 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.1.bim
-rw-r--r-- 1 hs3163 hs3163  23K Sep 29 15:08 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.1.fam
-rw-r--r-- 1 hs3163 hs3163 101M Sep 29 15:11 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.20.bed
-rw-r--r-- 1 hs3163 hs3163  15M Sep 29 15:11 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.20.bim
-rw-r--r-- 1 hs3163 hs3163  23K Sep 29 15:11 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.20.fam
-rw-r--r-- 1 hs3163 hs3163  60M Sep 29 15:11 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.21.bed
-rw-r--r-- 1 hs3163 hs3163 9.1M Sep 29 15:11 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.21.bim
-rw-r--r-- 1 hs3163 hs3163  23K Sep 29 15:11 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.21.fam
-rw-r--r-- 1 hs3163 hs3163  66M Sep 29 15:09 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.22.bed
-rw-r--r-- 1 hs3163 hs3163  11M Sep 29 15:09 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.22.bim
-rw-r--r-- 1 hs3163 hs3163  23K Sep 29 15:09 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.22.fam
-rw-r--r-- 1 hs3163 hs3163 359M Sep 29 15:05 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.2.bed
-rw-r--r-- 1 hs3163 hs3163  52M Sep 29 15:05 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.2.bim
-rw-r--r-- 1 hs3163 hs3163  23K Sep 29 15:05 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.2.fam
-rw-r--r-- 1 hs3163 hs3163 302M Sep 29 15:07 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.3.bed
-rw-r--r-- 1 hs3163 hs3163  42M Sep 29 15:07 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.3.bim
-rw-r--r-- 1 hs3163 hs3163  23K Sep 29 15:07 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.3.fam
-rw-r--r-- 1 hs3163 hs3163 302M Sep 29 15:08 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.4.bed
-rw-r--r-- 1 hs3163 hs3163  43M Sep 29 15:08 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.4.bim
-rw-r--r-- 1 hs3163 hs3163  23K Sep 29 15:08 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.4.fam
-rw-r--r-- 1 hs3163 hs3163 274M Sep 29 15:07 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.5.bed
-rw-r--r-- 1 hs3163 hs3163  39M Sep 29 15:07 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.5.bim
-rw-r--r-- 1 hs3163 hs3163  23K Sep 29 15:07 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.5.fam
-rw-r--r-- 1 hs3163 hs3163 280M Sep 29 15:07 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.6.bed
-rw-r--r-- 1 hs3163 hs3163  40M Sep 29 15:07 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.6.bim
-rw-r--r-- 1 hs3163 hs3163  23K Sep 29 15:07 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.6.fam
-rw-r--r-- 1 hs3163 hs3163 255M Sep 29 15:07 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.7.bed
-rw-r--r-- 1 hs3163 hs3163  37M Sep 29 15:07 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.7.bim
-rw-r--r-- 1 hs3163 hs3163  23K Sep 29 15:07 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.7.fam
-rw-r--r-- 1 hs3163 hs3163 232M Sep 29 15:07 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.8.bed
-rw-r--r-- 1 hs3163 hs3163  33M Sep 29 15:07 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.8.bim
-rw-r--r-- 1 hs3163 hs3163  23K Sep 29 15:07 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.8.fam
-rw-r--r-- 1 hs3163 hs3163 190M Sep 29 15:08 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.9.bed
-rw-r--r-- 1 hs3163 hs3163  27M Sep 29 15:08 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.9.bim
-rw-r--r-- 1 hs3163 hs3163  23K Sep 29 15:08 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.9.fam
-rw-r--r-- 1 hs3163 hs3163 4.2G Sep 28 20:02 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.bed
-rw-r--r-- 1 hs3163 hs3163 619M Sep 28 20:02 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.bim
-rw-r--r-- 1 hs3163 hs3163  23K Sep 28 20:02 ROSMAP_NIA_WGS.leftnorm.filtered.filtered.fam
```


### Path(s) to omics-data matrix 

**output of phenotype_preprocessing_sqtl.ipynb**

leafCutter:

- FTP server: `/ftp_fgc_xqtl/projects/rna-seq/BU/ROSMAP_DLPFC/sQTL/phenotype_preprocessing/`

psichomics:

- Wang Lab, `/mnt/vast/hpc/csg/molecular_phenotype_calling/psichomics_sQTL/pheno`

```
$ ls -lh *.{txt,bed}
-rw-r--r-- 1 xc2610 xc2610 2.7K Apr  3 14:41 ROSMAP_psichomics_bed_recipe.txt
-rw-r--r-- 1 xc2610 xc2610  65M Apr 14 17:00 ROSMAP.psichomics.qqnorm.revised.formated_chr10.bed
-rw-r--r-- 1 xc2610 xc2610 113M Apr 14 17:00 ROSMAP.psichomics.qqnorm.revised.formated_chr11.bed
-rw-r--r-- 1 xc2610 xc2610 102M Apr 14 17:00 ROSMAP.psichomics.qqnorm.revised.formated_chr12.bed
-rw-r--r-- 1 xc2610 xc2610  28M Apr 14 17:01 ROSMAP.psichomics.qqnorm.revised.formated_chr13.bed
-rw-r--r-- 1 xc2610 xc2610  69M Apr 14 17:01 ROSMAP.psichomics.qqnorm.revised.formated_chr14.bed
-rw-r--r-- 1 xc2610 xc2610  58M Apr 14 17:01 ROSMAP.psichomics.qqnorm.revised.formated_chr15.bed
-rw-r--r-- 1 xc2610 xc2610  88M Apr 14 17:01 ROSMAP.psichomics.qqnorm.revised.formated_chr16.bed
-rw-r--r-- 1 xc2610 xc2610 125M Apr 14 17:01 ROSMAP.psichomics.qqnorm.revised.formated_chr17.bed
-rw-r--r-- 1 xc2610 xc2610  26M Apr 14 17:01 ROSMAP.psichomics.qqnorm.revised.formated_chr18.bed
-rw-r--r-- 1 xc2610 xc2610 117M Apr 14 17:01 ROSMAP.psichomics.qqnorm.revised.formated_chr19.bed
-rw-r--r-- 1 xc2610 xc2610 166M Apr  5 14:34 ROSMAP.psichomics.qqnorm.revised.formated_chr1.bed
-rw-r--r-- 1 xc2610 xc2610  52M Apr 14 17:01 ROSMAP.psichomics.qqnorm.revised.formated_chr20.bed
-rw-r--r-- 1 xc2610 xc2610  18M Apr 14 17:01 ROSMAP.psichomics.qqnorm.revised.formated_chr21.bed
-rw-r--r-- 1 xc2610 xc2610  50M Apr 14 17:01 ROSMAP.psichomics.qqnorm.revised.formated_chr22.bed
-rw-r--r-- 1 xc2610 xc2610 122M Apr  5 16:55 ROSMAP.psichomics.qqnorm.revised.formated_chr2.bed
-rw-r--r-- 1 xc2610 xc2610 108M Apr 14 17:00 ROSMAP.psichomics.qqnorm.revised.formated_chr3.bed
-rw-r--r-- 1 xc2610 xc2610  60M Apr 14 17:00 ROSMAP.psichomics.qqnorm.revised.formated_chr4.bed
-rw-r--r-- 1 xc2610 xc2610  75M Apr 14 17:00 ROSMAP.psichomics.qqnorm.revised.formated_chr5.bed
-rw-r--r-- 1 xc2610 xc2610  80M Apr 14 17:00 ROSMAP.psichomics.qqnorm.revised.formated_chr6.bed
-rw-r--r-- 1 xc2610 xc2610  84M Apr 14 17:00 ROSMAP.psichomics.qqnorm.revised.formated_chr7.bed
-rw-r--r-- 1 xc2610 xc2610  62M Apr 14 17:00 ROSMAP.psichomics.qqnorm.revised.formated_chr8.bed
-rw-r--r-- 1 xc2610 xc2610  66M Apr 14 17:00 ROSMAP.psichomics.qqnorm.revised.formated_chr9.bed
-rw-r--r-- 1 xc2610 xc2610 426K Feb 13 01:15 ROSMAP.psichomics.qqnorm.revised.formated_chrMT.bed
-rw-r--r-- 1 xc2610 xc2610  47M Feb 13 01:15 ROSMAP.psichomics.qqnorm.revised.formated_chrX.bed
-rw-r--r-- 1 xc2610 xc2610 529K Feb 13 01:15 ROSMAP.psichomics.qqnorm.revised.formated_chrY.bed
```

### Path(s) to covariate data matrix 

**output of covariate_preprocessing.ipynb**

leafCutter:

- FTP server: `/ftp_fgc_xqtl/projects/rna-seq/BU/ROSMAP_DLPFC/sQTL/covariate_preprocessing/leafcutter.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.gz`
   

psichomics:

- Wang Lab, `/mnt/vast/hpc/csg/molecular_phenotype_calling/psichomics_sQTL/cov`

```
$ ls -lh *.gz
-rw-r--r-- 1 xc2610 xc2610 546K Feb  9 13:06 psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.gz
```

### Path(s) to QTL results 

**output of association_scan_sQTL.ipynb**

leafCutter:

- FTP server: `/ftp_fgc_xqtl/projects/rna-seq/BU/ROSMAP_DLPFC/sQTL/association_scan`
   
psichomics:

- Wang lab: `/mnt/vast/hpc/csg/molecular_phenotype_calling/psichomics_sQTL/output`

```
$ls -lh *.txt
-rw-r--r-- 1 xc2610 xc2610 928K Feb 13 02:34 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.10.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 7.4G Feb 13 01:45 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.10.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 1.6M Feb 13 03:08 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.11.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610  12G Feb 13 01:51 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.11.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 1.5M Feb 13 03:26 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.12.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610  11G Feb 13 01:53 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.12.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 389K Feb 13 02:57 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.13.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 3.2G Feb 13 02:36 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.13.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 973K Feb 13 03:35 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.14.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 7.9G Feb 13 02:44 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.14.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 813K Feb 13 03:24 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.15.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 5.7G Feb 13 02:46 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.15.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 1.2M Feb 13 03:53 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.16.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 9.8G Feb 13 02:50 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.16.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 1.8M Feb 13 04:39 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.17.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610  14G Feb 13 03:01 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.17.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 353K Feb 13 03:18 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.18.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 2.8G Feb 13 03:01 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.18.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 1.6M Feb 13 05:01 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.19.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610  16G Feb 13 03:25 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.19.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 2.3M Feb 13 04:16 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.1.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610  17G Feb 13 02:03 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.1.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 729K Feb 13 03:36 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.20.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 5.7G Feb 13 03:00 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.20.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 254K Feb 13 03:25 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.21.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 2.1G Feb 13 03:12 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.21.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 712K Feb 13 03:58 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.22.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 5.9G Feb 13 03:19 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.22.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 1.7M Feb 13 03:16 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.2.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610  13G Feb 13 01:53 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.2.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 1.5M Feb 13 03:11 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.3.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610  11G Feb 13 01:51 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.3.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 839K Feb 13 02:30 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.4.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 6.7G Feb 13 01:44 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.4.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 1.1M Feb 13 02:37 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.5.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 7.9G Feb 13 01:45 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.5.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 1.1M Feb 13 03:02 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.6.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610  12G Feb 13 01:51 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.6.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 1.2M Feb 13 02:51 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.7.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 9.5G Feb 13 01:49 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.7.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 871K Feb 13 02:31 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.8.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 6.8G Feb 13 01:45 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.8.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 939K Feb 13 02:39 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.9.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 7.5G Feb 13 01:46 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.9.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610  27M Feb 13 05:02 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.emprical.cis_sumstats.txt
```

psichomics (grouped by each gene - event_type pair):

- Wang lab: `/mnt/vast/hpc/csg/molecular_phenotype_calling/psichomics_sQTL/event_sep/output`

```
$ ls -lh *.txt
-rw-r--r-- 1 xc2610 xc2610 229K Apr  3 15:30 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.10.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 1.8G Apr  3 14:49 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.10.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 414K Apr  3 15:53 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.11.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 2.9G Apr  3 14:52 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.11.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 373K Apr  3 16:12 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.12.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 2.7G Apr  3 15:10 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.12.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610  99K Apr  3 15:46 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.13.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 785M Apr  3 15:29 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.13.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 249K Apr  3 16:16 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.14.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 2.0G Apr  3 15:33 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.14.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 213K Apr  3 16:18 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.15.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 1.5G Apr  3 15:47 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.15.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 332K Apr  3 16:30 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.16.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 2.6G Apr  3 15:38 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.16.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 453K Apr  3 17:19 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.17.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 3.4G Apr  3 16:01 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.17.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610  91K Apr  3 16:04 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.18.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 699M Apr  3 15:49 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.18.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 471K Apr  3 17:18 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.19.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 4.3G Apr  3 15:55 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.19.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 617K Apr  3 16:33 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.1.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 4.3G Apr  3 14:55 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.1.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 182K Apr  3 16:05 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.20.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 1.4G Apr  3 15:34 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.20.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610  73K Apr  3 16:06 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.21.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 577M Apr  3 15:55 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.21.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 194K Apr  3 16:30 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.22.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 1.6G Apr  3 15:58 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.22.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 434K Apr  3 16:01 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.2.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 3.1G Apr  3 14:52 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.2.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 394K Apr  3 15:53 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.3.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 2.7G Apr  3 14:51 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.3.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 220K Apr  3 15:25 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.4.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 1.7G Apr  3 14:48 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.4.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 286K Apr  3 15:42 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.5.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 2.1G Apr  3 14:50 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.5.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 319K Apr  3 15:52 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.6.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 3.4G Apr  3 14:51 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.6.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 331K Apr  3 15:43 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.7.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 2.6G Apr  3 14:50 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.7.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 234K Apr  3 15:26 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.8.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 1.8G Apr  3 14:48 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.8.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 243K Apr  3 15:29 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.9.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 1.9G Apr  3 14:49 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.9.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 7.4M Apr  3 17:21 ROSMAP_psichomics_bed_recipe_psichomics.dlpfc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.emprical.cis_sumstats.txt
```

### Path(s) to fine-mapping with SuSiE model 

**output of fine_mapping.ipynb**

- Wang lab: `/mnt/vast/hpc/csg/molecular_phenotype_calling/sQTL_finemapping/ROSMAP_psichomics`

The results are seperated in psi_A3SS, psi_A5SS, psi_AFE, psi_ALE, psi_MXE, psi_SE sub directories according to their event type. Due to the massive amount of files for splicing data they are not listed here.

### Path(s) to fine-mapping with SuSiE RSS model