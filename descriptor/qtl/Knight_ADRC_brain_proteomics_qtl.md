# Knight ADRC brain proteomics QTL
Charles F. And Joanne Knight Alzheimer's Disease Research Center (Knight-ADRC)

Please refer to [this document](../study_info/KnightADRC.ipynb) for an overview of the Knight project.

## Contact
Zining Qi(zq2209@cumc.columbia.edu)

## Study Overview
 
- Study name : Knight ADRC brain proteomics QTL
- Study Description : Charles F. And Joanne Knight Alzheimer's Disease Research Center (Knight-ADRC) brain proteomics QTL analysis summary statistics using the FGC xQTL pipeline. 

Samples' phenotype information (sex, age, race etc.) can be found in Knight metadata, see "Other information" section in [this document](../study_info/KnightADRC.md)

## Analysis Status
TransQTL association: Need to be updated with new covariate files.

## Analysis Details

### Sample size tracking through the analysis workflow

|Step |Sample Size|
|-----|-----------|
|Raw data|442|
|After overlapping with Knight covariates|418|
|After overlapping with Knight genotype|412|

### QC and Normalization Details for Phenotype Data

For QCs performed on data please refer to `descriptor/omics/Knight_ADRC_brain_proteomics.md`

### Genotype parameters

- Kinship coefficient for related individuals: 0.0625
- Minor allele count cutoff for single variant analysis: 5
- Variant level missingness threshold: 0.1
- Sample level missingness threshold: 0.1

### Covariate parameters

PCA analysis:
- MAF for PCA: 0.05
- LD pruning via PLINK for PCA analysis: window 50, shift 10, r2 0.1
- Tolerance of missingness in covariates: 0.3
- number of pc that captured more than 70% PVE were kept

Hidden Factor analysis - PCA
- Use Marchenko-Pastur limit to choose PCs

Final covariates: Sex, Age at death, PMI, PCs(12), hidden factors(18)

### TensorQTL association scan parameters

- cis/trans window for the up and downstream radius to analyze around the region of interest, in units of bp: 1000000
- Minor allele count cutoff: 5
- Minor allele frequency cutoff: 5/(2.0*592) = 0.00422297

## Links to QTL analysis notebooks

See notebooks in: 

- https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Wang_Columbia/knight/pqtl

The notebooks in this folder contain the commands and data wrangling codes for analysis of the proteomics data in ROSMAP. (data wrangling exist because not all data are processed using the xqtl-pipeline from the begnning and need to be reformated to fit one intermediate step of the pipeline).

### Association data preprocessing

phenotype preprocessing can be run in parallel but covariate preprocessing need to be done last since it requires both phenotype data and PCs from PCA in genotype preprocessing.

- [genotype_preprocessing.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/knight/pqtl/genotype_preprocessing.ipynb) shows the commands used for genotype processing and preparation steps.
  - Includes QC, PCA, and PCA result figures.
- [phenotype_preprocessing.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/knight/pqtl/phenotype_preprocessing.ipynb) shows the commands used for the phenotype data processing and preparation steps.
  - This notebook strated from some already cleaned data and covert them to bed format inputs taken by tensorQTL.
- [covariate_preprocessing.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/knight/pqtl/covariates_preprocessing.ipynb) shows the commands used for the covariate data processing and preparation steps.
  - This includes PCA hidden factor analysis steps and merging the PCA hidden factors to covariates and PCA. 
  
### Association scan using TensorQTL and summary statistics standardization

- [cis_pqtl_association.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/knight/pqtl/cis_haqtl_association.ipynb) provides information and result of cis-QTL analysis.
- [trans_pqtl_association.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/knight/pqtl/trans_pqtl_association.ipynb) provides information and result of AD genes trans-QTL analysis.

## Dataset Description

### Path(s) to genotype matrix

- Wang Lab, `/mnt/vast/hpc/csg/molecular_phenotype_calling/WashU_genotype/genotype_qc`

```
-rw-r--r-- 1 zq2209 zq2209  48M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.10.bed
-rw-r--r-- 1 zq2209 zq2209  17M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.10.bim
-rw-r--r-- 1 zq2209 zq2209 9.4K Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.10.fam
-rw-r--r-- 1 zq2209 zq2209  47M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.11.bed
-rw-r--r-- 1 zq2209 zq2209  16M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.11.bim
-rw-r--r-- 1 zq2209 zq2209 9.4K Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.11.fam
-rw-r--r-- 1 zq2209 zq2209  45M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.12.bed
-rw-r--r-- 1 zq2209 zq2209  16M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.12.bim
-rw-r--r-- 1 zq2209 zq2209 9.4K Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.12.fam
-rw-r--r-- 1 zq2209 zq2209  35M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.13.bed
-rw-r--r-- 1 zq2209 zq2209  12M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.13.bim
-rw-r--r-- 1 zq2209 zq2209 9.4K Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.13.fam
-rw-r--r-- 1 zq2209 zq2209  30M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.14.bed
-rw-r--r-- 1 zq2209 zq2209  11M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.14.bim
-rw-r--r-- 1 zq2209 zq2209 9.4K Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.14.fam
-rw-r--r-- 1 zq2209 zq2209  26M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.15.bed
-rw-r--r-- 1 zq2209 zq2209 8.9M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.15.bim
-rw-r--r-- 1 zq2209 zq2209 9.4K Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.15.fam
-rw-r--r-- 1 zq2209 zq2209  29M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.16.bed
-rw-r--r-- 1 zq2209 zq2209 9.6M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.16.bim
-rw-r--r-- 1 zq2209 zq2209 9.4K Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.16.fam
-rw-r--r-- 1 zq2209 zq2209  25M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.17.bed
-rw-r--r-- 1 zq2209 zq2209 8.3M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.17.bim
-rw-r--r-- 1 zq2209 zq2209 9.4K Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.17.fam
-rw-r--r-- 1 zq2209 zq2209  27M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.18.bed
-rw-r--r-- 1 zq2209 zq2209 9.1M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.18.bim
-rw-r--r-- 1 zq2209 zq2209 9.4K Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.18.fam
-rw-r--r-- 1 zq2209 zq2209  21M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.19.bed
-rw-r--r-- 1 zq2209 zq2209 7.0M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.19.bim
-rw-r--r-- 1 zq2209 zq2209 9.4K Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.19.fam
-rw-r--r-- 1 zq2209 zq2209  72M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.1.bed
-rw-r--r-- 1 zq2209 zq2209  24M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.1.bim
-rw-r--r-- 1 zq2209 zq2209 9.4K Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.1.fam
-rw-r--r-- 1 zq2209 zq2209  21M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.20.bed
-rw-r--r-- 1 zq2209 zq2209 7.0M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.20.bim
-rw-r--r-- 1 zq2209 zq2209 9.4K Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.20.fam
-rw-r--r-- 1 zq2209 zq2209  13M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.21.bed
-rw-r--r-- 1 zq2209 zq2209 4.3M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.21.bim
-rw-r--r-- 1 zq2209 zq2209 9.4K Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.21.fam
-rw-r--r-- 1 zq2209 zq2209  13M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.22.bed
-rw-r--r-- 1 zq2209 zq2209 4.3M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.22.bim
-rw-r--r-- 1 zq2209 zq2209 9.4K Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.22.fam
-rw-r--r-- 1 zq2209 zq2209  77M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.2.bed
-rw-r--r-- 1 zq2209 zq2209  26M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.2.bim
-rw-r--r-- 1 zq2209 zq2209 9.4K Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.2.fam
-rw-r--r-- 1 zq2209 zq2209  66M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.3.bed
-rw-r--r-- 1 zq2209 zq2209  22M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.3.bim
-rw-r--r-- 1 zq2209 zq2209 9.4K Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.3.fam
-rw-r--r-- 1 zq2209 zq2209  68M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.4.bed
-rw-r--r-- 1 zq2209 zq2209  23M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.4.bim
-rw-r--r-- 1 zq2209 zq2209 9.4K Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.4.fam
-rw-r--r-- 1 zq2209 zq2209  61M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.5.bed
-rw-r--r-- 1 zq2209 zq2209  20M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.5.bim
-rw-r--r-- 1 zq2209 zq2209 9.4K Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.5.fam
-rw-r--r-- 1 zq2209 zq2209  62M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.6.bed
-rw-r--r-- 1 zq2209 zq2209  21M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.6.bim
-rw-r--r-- 1 zq2209 zq2209 9.4K Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.6.fam
-rw-r--r-- 1 zq2209 zq2209  55M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.7.bed
-rw-r--r-- 1 zq2209 zq2209  18M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.7.bim
-rw-r--r-- 1 zq2209 zq2209 9.4K Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.7.fam
-rw-r--r-- 1 zq2209 zq2209  51M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.8.bed
-rw-r--r-- 1 zq2209 zq2209  17M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.8.bim
-rw-r--r-- 1 zq2209 zq2209 9.4K Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.8.fam
-rw-r--r-- 1 zq2209 zq2209  41M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.9.bed
-rw-r--r-- 1 zq2209 zq2209  14M Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.9.bim
-rw-r--r-- 1 zq2209 zq2209 9.4K Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.9.fam
-rw-r--r-- 1 zq2209 zq2209 922M Feb 14 10:37 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.bed
-rw-r--r-- 1 zq2209 zq2209 309M Feb 14 10:37 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.bim
-rw-r--r-- 1 zq2209 zq2209 9.4K Feb 14 17:30 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.fam
-rw-r--r-- 1 zq2209 zq2209  19K Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.X.bed
-rw-r--r-- 1 zq2209 zq2209 6.2K Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.X.bim
-rw-r--r-- 1 zq2209 zq2209 9.4K Feb 14 17:36 MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.X.fam
```

### Path(s) to omics-data matrix

- Wang Lab, `/mnt/vast/hpc/csg/zq2209/data_production/proteomics/knight/pheno`

```
$ ls -lh *.{txt,gz}
-rw-r--r-- 1 zq2209 zq2209 4.2M Jun  1 13:18  WashU_pheno.bed.gz
-rw-r--r-- 1 zq2209 zq2209 133K Jun  1 13:18  WashU_pheno_chr10.bed.gz
-rw-r--r-- 1 zq2209 zq2209 243K Jun  1 13:18  WashU_pheno_chr11.bed.gz
-rw-r--r-- 1 zq2209 zq2209 284K Jun  1 13:18  WashU_pheno_chr12.bed.gz
-rw-r--r-- 1 zq2209 zq2209  83K Jun  1 13:18  WashU_pheno_chr13.bed.gz
-rw-r--r-- 1 zq2209 zq2209 122K Jun  1 13:18  WashU_pheno_chr14.bed.gz
-rw-r--r-- 1 zq2209 zq2209 111K Jun  1 13:18  WashU_pheno_chr15.bed.gz
-rw-r--r-- 1 zq2209 zq2209 144K Jun  1 13:18  WashU_pheno_chr16.bed.gz
-rw-r--r-- 1 zq2209 zq2209 291K Jun  1 13:18  WashU_pheno_chr17.bed.gz
-rw-r--r-- 1 zq2209 zq2209  57K Jun  1 13:18  WashU_pheno_chr18.bed.gz
-rw-r--r-- 1 zq2209 zq2209 348K Jun  1 13:18  WashU_pheno_chr19.bed.gz
-rw-r--r-- 1 zq2209 zq2209 453K Jun  1 13:18  WashU_pheno_chr1.bed.gz
-rw-r--r-- 1 zq2209 zq2209 151K Jun  1 13:18  WashU_pheno_chr20.bed.gz
-rw-r--r-- 1 zq2209 zq2209  91K Jun  1 13:18  WashU_pheno_chr21.bed.gz
-rw-r--r-- 1 zq2209 zq2209 103K Jun  1 13:18  WashU_pheno_chr22.bed.gz
-rw-r--r-- 1 zq2209 zq2209 238K Jun  1 13:18  WashU_pheno_chr2.bed.gz
-rw-r--r-- 1 zq2209 zq2209 220K Jun  1 13:18  WashU_pheno_chr3.bed.gz
-rw-r--r-- 1 zq2209 zq2209 235K Jun  1 13:18  WashU_pheno_chr4.bed.gz
-rw-r--r-- 1 zq2209 zq2209 222K Jun  1 13:18  WashU_pheno_chr5.bed.gz
-rw-r--r-- 1 zq2209 zq2209 177K Jun  1 13:18  WashU_pheno_chr6.bed.gz
-rw-r--r-- 1 zq2209 zq2209 182K Jun  1 13:18  WashU_pheno_chr7.bed.gz
-rw-r--r-- 1 zq2209 zq2209 129K Jun  1 13:18  WashU_pheno_chr8.bed.gz
-rw-r--r-- 1 zq2209 zq2209 138K Jun  1 13:18  WashU_pheno_chr9.bed.gz
-rw-r--r-- 1 zq2209 zq2209 115K Jun  1 13:18  WashU_pheno_chrX.bed.gz
```

### Path(s) to covariate data matrix

- Wang Lab, `/mnt/vast/hpc/csg/zq2209/data_production/proteomics/knight/cov`

```
$ ls -lh *.gz
-rw-r--r-- 1 zq2209 zq2209 113K Jun  1 13:22 WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.gz
```

### Path(s) to QTL results

- Wang lab: `/mnt/vast/hpc/csg/molecular_phenotype_calling/pQTL_cis/WashU`
```
ls -lh *.txt
-rw-r--r-- 1 zq2209 zq2209 8.9K May 19 14:33 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.10.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209  44M May 19 14:32 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.10.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209  17K May 19 14:34 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.11.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209  76M May 19 14:34 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.11.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209  19K May 19 14:36 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.12.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209  81M May 19 14:35 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.12.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209 5.5K May 19 14:35 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.13.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209  26M May 19 14:35 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.13.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209 8.6K May 19 14:35 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.14.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209  41M May 19 14:34 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.14.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209 7.2K May 19 14:35 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.15.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209  29M May 19 14:35 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.15.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209 9.8K May 19 14:35 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.16.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209  42M May 19 14:35 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.16.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209  20K May 19 14:37 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.17.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209  81M May 19 14:36 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.17.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209 3.8K May 19 14:36 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.18.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209  18M May 19 14:36 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.18.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209  24K May 19 14:36 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.19.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209 122M May 19 14:36 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.19.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209  31K May 19 14:33 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.1.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209 118M May 19 14:32 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.1.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209  11K May 19 14:37 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.20.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209  46M May 19 14:37 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.20.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209 6.2K May 19 14:36 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.21.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209  31M May 19 14:36 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.21.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209 7.2K May 19 14:37 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.22.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209  29M May 19 14:37 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.22.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209  17K May 19 14:31 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.2.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209  69M May 19 14:31 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.2.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209  15K May 19 14:32 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.3.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209  60M May 19 14:31 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.3.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209  16K May 19 14:32 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.4.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209  70M May 19 14:31 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.4.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209  15K May 19 14:32 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.5.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209  64M May 19 14:31 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.5.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209  12K May 19 14:34 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.6.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209  83M May 19 14:33 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.6.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209  13K May 19 14:33 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.7.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209  51M May 19 14:33 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.7.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209 9.0K May 19 14:34 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.8.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209  40M May 19 14:34 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.8.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209 9.5K May 19 14:34 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.9.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209  41M May 19 14:33 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.9.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209 363K May 19 14:38 pheno_recipe_WashU_pheno.WashU_cov.MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.filtered.pQTL.related.filtered.extracted.pca.projected.resid.Marchenko_pc.emprical.cis_sumstats.txt
```
- FTP: 

### Path(s) to cis-QTL association testing

**output of TensorQTL.ipynb**

- `/ftp_fgc_xqtl/analysis_result/cis_association/KNIGHT/pQTL/`
  
### Path(s) to fine-mapping with SuSiE model

### Path(s) to fine-mapping with SuSiE RSS model

