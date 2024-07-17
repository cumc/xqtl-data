# ROSMAP DLPFC gene expression QTL

Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) DLPFC gene expression. 

Please refer to [this document](../study_info/ROSMAP.md) for an overview of the ROSMAP project.

## Contact

Shrishtee Kandoi; Frank Grenn

- Contact Email : ; hs3163@cumc.columbia.edu; hs3393@cumc.columbia.edu; jt3386@cumc.columbia.edu
- Contact Affiliation : Boston University; Columbia University
- Contact Role : Shrishtee Kandoi and Hao Sun performed QTL analysis; Haochen Sun performed fine-mapping, and Jiajun Tao performed replication

## Study Overview
 
- Study name : ROSMAP DLPFC eQTL
- Study Description : Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) eQTL analysis summary statistics using the FGC xQTL pipeline. 

Samples' phenotype information (sex, age, race etc.) can be found in ROSMAP metadata, see "Other information" section in [this document](../study_info/ROSMAP.md)

## Analysis Details

## Analysis Status

TransQTL association: Finished.

### Sample size tracking through the analysis workflow

|Step |Sample Size|
|-----|-----------|
|Raw data|1141|
|After overlapping with ROSMAP WGS|839|

### QC and Normalization Details for Phenotype Data

Brain multi-region RNA-seq data was proccessed with the xQTL-pipeline, for analysis detial please check records here: [eQTL](https://github.com/cumc/brain-xqtl-analysis/tree/main/analysis/Zhang_BU/ROSMAP_DLPFC/eQTL) [eQTL_susie_result_analysis
](https://github.com/cumc/brain-xqtl-analysis/tree/main/analysis/Wang_Columbia/eqtl)

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

The notebooks in this folder contain the commands, data wrangling codes for analysis of the eQTL and sQTL data in ROSMAP (data wrangling exist because not all data are processed using the xqtl-pipeline from the beginning and need to be reformatted to fit one intermediate step of the pipeline), log files and some of the results visualizations produced by the pipeline when processing and analyzing the RNA-seq expression in the Dorsolateral Prefrontal Cortex region of the ROSMAP brain data (DLPFC-ROSMAP).

### Association data preprocessing

phenotype preprocessing and genotype preprocessing can be run in parallel but covariate preprocessing needs to be done last since it requires both phenotype data and PCs from PCA in genotype preprocessing.

- [genotype_qc.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Zhang_BU/ROSMAP_DLPFC/genotype/genotype_qc.ipynb) shows the commands used for genotype processing and preparation steps, including why we decided not to remove any outliers.
    - Mostly contains the commands used to run the pipeline, but includes some pre-pipeline data wrangling.
    - This includes QC, PCA, and GRM steps
- [phenotype_preprocessing_eqtl.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Zhang_BU/ROSMAP_DLPFC/eQTL/phenotype_preprocessing_eQTL.ipynb) shows the commands used for the phenotype data processing and preparation steps.
    - As above, it mostly contains the commands used to run the pipeline, but includes some pre-pipeline data wrangling.
    - This includes quantification steps, QC, annotation, and residual expression steps
- [covariate_preprocessing_eQTL.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Zhang_BU/ROSMAP_DLPFC/eQTL/covariate_preprocessing_eQTL.ipynb) shows the commands used for the covariate data processing and preparation steps.
    - This includes PEER factor analysis steps and merging the PEER factors to covariates in raw data and PCA. 
- [rnaSeq_PEER.diag.pdf](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Zhang_BU/ROSMAP_DLPFC/eQTL/rnaSeq_PEER.diag.pdf) PEER factor analysis result
  
### Association scan using TensorQTL and summary statistics standardization

- [association_scan_eQTL.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Zhang_BU/ROSMAP_DLPFC/eQTL/association_scan_eQTL.ipynb) provides information about the TensorQTL cis association scan.

### SuSiE univariate fine mapping

- [Fine_mapping_with_SuSIE.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Zhang_BU/ROSMAP_DLPFC/eQTL/Fine_mapping_with_SuSIE.ipynb) 

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

(FIXME: not sure where it is on BU cluster)

### Path(s) to covariate data matrix

- Covariates used in this analysis on BU cluster: `/restricted/projectnb/casa/skandoi/ROSMAP_DLPFC/reference_data/ROSMAP_xqtl_covariates_sex_death_pmi_study.tsv`

### Path(s) to QTL results

- FTP server, `/ftp_fgc_xqtl/projects/rna-seq/BU/ROSMAP_DLPFC/eQTL/association_scan`
- Wang Lab, `/mnt/vast/hpc/csg/ftp_lisanwanglab_sync/ftp_fgc_xqtl/projects/rna-seq/BU/ROSMAP_DLPFC/eQTL/association_scan/`

empirical_files:

```
$ls -lh *.txt
-rw-r--r-- 1 xc2610 xc2610 235K Mar  2 00:02 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.10.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 312K Mar  2 00:02 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.11.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 324K Mar  2 00:02 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.12.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 124K Mar  2 00:02 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.13.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 186K Mar  2 00:02 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.14.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 214K Mar  2 00:02 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.15.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 287K Mar  2 00:02 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.16.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 349K Mar  2 00:02 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.17.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 104K Mar  2 00:02 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.18.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 378K Mar  2 00:02 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.19.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 573K Mar  2 00:02 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.1.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 151K Mar  2 00:02 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.20.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610  62K Mar  2 00:02 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.21.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 150K Mar  2 00:02 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.22.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 392K Mar  2 00:02 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.2.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 330K Mar  2 00:02 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.3.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 218K Mar  2 00:02 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.4.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 282K Mar  2 00:02 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.5.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 304K Mar  2 00:02 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.6.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 279K Mar  2 00:02 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.7.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 220K Mar  2 00:02 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.8.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 230K Mar  2 00:02 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.9.emprical.cis_sumstats.txt
-rw-r--r-- 1 xc2610 xc2610 7.6M Mar  2 00:02 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.emprical.cis_sumstats.txt
```

norminal_qced_files:

```
ls -lh *.txt
-rw-r--r-- 1 xc2610 xc2610 1.8G Jan 23 12:05 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.10.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 2.1G Jan 23 12:08 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.11.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 2.4G Jan 23 12:13 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.12.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 936M Jan 23 12:15 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.13.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 1.4G Jan 23 12:17 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.14.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 1.4G Jan 23 12:19 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.15.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 2.1G Jan 23 12:23 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.16.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 2.6G Jan 23 12:27 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.17.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 735M Jan 23 12:30 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.18.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 3.2G Jan 23 12:35 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.19.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 3.8G Jan 23 11:28 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.1.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 1.2G Jan 23 12:37 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.20.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 485M Jan 23 12:38 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.21.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 1.3G Jan 23 12:40 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.22.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 2.6G Jan 23 11:36 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.2.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 2.2G Jan 23 11:41 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.3.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 1.6G Jan 23 11:44 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.4.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 1.9G Jan 23 11:48 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.5.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 2.7G Jan 23 11:52 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.6.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 2.0G Jan 23 11:56 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.7.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 1.6G Jan 23 11:58 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.8.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 xc2610 1.7G Jan 23 12:01 dlpfc_batch_all.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.processed_phenotype.per_chrom_dlpfc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.9.norminal.cis_long_table.txt
```
### Path(s) to cis-QTL association testing

**output of TensorQTL.ipynb**

- `/ftp_fgc_xqtl/analysis_result/cis_association/ROSMAP/eQTL/DLPFC`

### Path(s) to trans-QTL results

- Wang Lab, `/mnt/vast/hpc/csg/ftp_lisanwanglab_sync/ftp_fgc_xqtl/projects/rna-seq/BU/ROSMAP_DLPFC/eQTL/output_new/association/trans/`

### Path(s) to fine-mapping with SuSiE model

### Path(s) to fine-mapping with SuSiE RSS model

### Path(s) to colocalization with SuSiE-coloc
