# ROSMAP DLPFC protein expression QTL

Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) DLPFC protein expression. 

Please refer to [this document](../study_info/ROSMAP.md) for an overview of the ROSMAP project.

## Contact

Zining Qi(zq2209@cumc.columbia.edu)

## Study Overview
 
- Study name : ROSMAP DLPFC proteomics QTL
- Study Description : Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) proteomics QTL analysis summary statistics using the FGC xQTL pipeline. 

Samples' phenotype information (sex, age, race etc.) can be found in ROSMAP metadata, see "Other information" section in [this document](../study_info/ROSMAP.md)

## Analysis Status

TransQTL association: Finished.

## Links to QTL analysis notebooks

See notebooks in: 

- https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Wang_Columbia/pqtl

The notebooks in this folder contain the commands and data wrangling codes for analysis of the proteomics data in ROSMAP. (data wrangling exist because not all data are processed using the xqtl-pipeline from the beginning and need to be reformatted to fit one intermediate step of the pipeline).

### Association data preprocessing

phenotype preprocessing can be run in parallel but covariate preprocessing need to be done last since it requires both phenotype data and PCs from PCA in genotype preprocessing.

- [genotype_preprocessing.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/genotype/genotype_preprocessing.ipynb) shows the commands used for genotype processing and preparation steps, including QC and formatting for genotype data.
- [genotype_pca.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/pqtl/genotype_pca.ipynb) shows the commands used for computing genotype PC for population structure inference.
- [phenotype_preprocessing.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/pqtl/phenotype_preprocessing.ipynb) shows the commands used for the phenotype data formatting steps. QC is not included (should be performed already elsewhere).
- [covariate_preprocessing.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/pqtl/covariates_preprocessing.ipynb) shows the commands used for the covariate data processing and preparation steps, including icomputing molecular phenotype PCA for hidden factor analysis and merging all covariates together.
  
### Association scan using TensorQTL and summary statistics standardization

- [cis_association.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/pqtl/cis_association.ipynb) provides information and result of cis-QTL analysis.
- [trans_association.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/pqtl/trans_association.ipynb) provides information and result of AD genes trans-QTL analysis.

## Analysis Details

### Sample size tracking through the analysis workflow

|Step |Sample Size|
|-----|-----------|
|Raw data|596|
|After overlapping with ROSMAP WGS|512|
|After overlapping with ROSMAP joint call|416|

### QC and Normalization Details for Phenotype Data

Used proteomics data directly without further QC. For QCs performed on data please refer to `descriptor/omics/ROSMAP_DLPFC_proteomics.md`

### Genotype parameters

- Kinship coefficient for related individuals: 0.0625
- Minor allele count cutoff for single variant analysis: 0
- Variant level missingness threshold: 0.1
- Sample level missingness threshold: 0.1
- HWE cutoof: 1E-08

### Covariate parameters

PCA analysis:
- Minor allele count cutoff for PCA: 5
- LD pruning via PLINK for PCA analysis: window 50, shift 10, r2 0.1
- Tolerance of missingness in covariates: 0.3
- number of pc that captured more than 70% PVE were kept

Hidden Factor analysis - PCA
- Use Marchenko-Pastur limit to choose PCs

Final covariates: Sex, Age at death, PMI, PCs(12), hidden factors(41)

### TensorQTL association scan parameters

- [Extened TADB windows](https://github.com/cumc/fungen-xqtl-analysis/blob/main/resource/extended_cis_before_winsorize.tsv) for cis analysis.
- Trans window for the up and downstream radius to analyze around the region of interest, in units of bp: 1000000
- Minor allele count cutoff: 5
- Minor allele frequency cutoff: 5/(2.0*416) = 0.00422297


## Dataset Description

### Path(s) to genotype matrix

- Wang Lab, `/mnt/vast/hpc/csg/FunGen_xQTL/ROSMAP/Genotype` Whole Genotype

```
$ ls -lh *.{bim,bed,fam}
-rw-r--r-- 1 zq2209 zq2209  27G Aug 14 19:48 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.bed
-rw-r--r-- 1 zq2209 zq2209 3.6G Aug 14 19:47 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.bim
-rw-r--r-- 1 zq2209 zq2209  23K Aug 14 19:47 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.fam
```

- Wang Lab, `/mnt/vast/hpc/csg/FunGen_xQTL/ROSMAP/Genotype/plink_by_chr` Genotype by chromosome 

```
$ ls -lh *.{bim,bed,fam}
-rw-r--r-- 1 zq2209 zq2209 1.3G Aug 14 22:16 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.10.bed
-rw-r--r-- 1 zq2209 zq2209 188M Aug 14 22:16 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.10.bim
-rw-r--r-- 1 zq2209 zq2209  23K Aug 14 22:16 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.10.fam
-rw-r--r-- 1 zq2209 zq2209 1.3G Aug 14 22:16 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.11.bed
-rw-r--r-- 1 zq2209 zq2209 183M Aug 14 22:16 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.11.bim
-rw-r--r-- 1 zq2209 zq2209  23K Aug 14 22:16 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.11.fam
-rw-r--r-- 1 zq2209 zq2209 1.3G Aug 14 21:54 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.12.bed
-rw-r--r-- 1 zq2209 zq2209 179M Aug 14 21:54 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.12.bim
-rw-r--r-- 1 zq2209 zq2209  23K Aug 14 21:54 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.12.fam
-rw-r--r-- 1 zq2209 zq2209 941M Aug 14 21:54 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.13.bed
-rw-r--r-- 1 zq2209 zq2209 133M Aug 14 21:54 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.13.bim
-rw-r--r-- 1 zq2209 zq2209  23K Aug 14 21:54 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.13.fam
-rw-r--r-- 1 zq2209 zq2209 870M Aug 14 21:53 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.14.bed
-rw-r--r-- 1 zq2209 zq2209 121M Aug 14 21:53 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.14.bim
-rw-r--r-- 1 zq2209 zq2209  23K Aug 14 21:53 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.14.fam
-rw-r--r-- 1 zq2209 zq2209 797M Aug 14 21:54 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.15.bed
-rw-r--r-- 1 zq2209 zq2209 111M Aug 14 21:54 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.15.bim
-rw-r--r-- 1 zq2209 zq2209  23K Aug 14 21:54 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.15.fam
-rw-r--r-- 1 zq2209 zq2209 902M Aug 14 22:28 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.16.bed
-rw-r--r-- 1 zq2209 zq2209 126M Aug 14 22:28 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.16.bim
-rw-r--r-- 1 zq2209 zq2209  23K Aug 14 22:28 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.16.fam
-rw-r--r-- 1 zq2209 zq2209 796M Aug 14 21:55 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.17.bed
-rw-r--r-- 1 zq2209 zq2209 113M Aug 14 21:55 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.17.bim
-rw-r--r-- 1 zq2209 zq2209  23K Aug 14 21:55 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.17.fam
-rw-r--r-- 1 zq2209 zq2209 747M Aug 14 21:55 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.18.bed
-rw-r--r-- 1 zq2209 zq2209 104M Aug 14 21:55 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.18.bim
-rw-r--r-- 1 zq2209 zq2209  23K Aug 14 21:55 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.18.fam
-rw-r--r-- 1 zq2209 zq2209 639M Aug 14 21:55 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.19.bed
-rw-r--r-- 1 zq2209 zq2209  91M Aug 14 21:55 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.19.bim
-rw-r--r-- 1 zq2209 zq2209  23K Aug 14 21:55 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.19.fam
-rw-r--r-- 1 zq2209 zq2209 2.2G Aug 14 21:53 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.1.bed
-rw-r--r-- 1 zq2209 zq2209 293M Aug 14 21:53 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.1.bim
-rw-r--r-- 1 zq2209 zq2209  23K Aug 14 21:53 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.1.fam
-rw-r--r-- 1 zq2209 zq2209 628M Aug 14 21:54 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.20.bed
-rw-r--r-- 1 zq2209 zq2209  89M Aug 14 21:54 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.20.bim
-rw-r--r-- 1 zq2209 zq2209  23K Aug 14 21:54 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.20.fam
-rw-r--r-- 1 zq2209 zq2209 367M Aug 14 21:55 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.21.bed
-rw-r--r-- 1 zq2209 zq2209  53M Aug 14 21:55 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.21.bim
-rw-r--r-- 1 zq2209 zq2209  23K Aug 14 21:55 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.21.fam
-rw-r--r-- 1 zq2209 zq2209 397M Aug 14 22:22 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.22.bed
-rw-r--r-- 1 zq2209 zq2209  58M Aug 14 22:22 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.22.bim
-rw-r--r-- 1 zq2209 zq2209  23K Aug 14 22:22 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.22.fam
-rw-r--r-- 1 zq2209 zq2209 2.3G Aug 14 22:29 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.2.bed
-rw-r--r-- 1 zq2209 zq2209 315M Aug 14 22:29 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.2.bim
-rw-r--r-- 1 zq2209 zq2209  23K Aug 14 22:29 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.2.fam
-rw-r--r-- 1 zq2209 zq2209 1.9G Aug 14 21:53 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.3.bed
-rw-r--r-- 1 zq2209 zq2209 254M Aug 14 21:53 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.3.bim
-rw-r--r-- 1 zq2209 zq2209  23K Aug 14 21:53 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.3.fam
-rw-r--r-- 1 zq2209 zq2209 1.9G Aug 14 21:53 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.4.bed
-rw-r--r-- 1 zq2209 zq2209 248M Aug 14 21:53 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.4.bim
-rw-r--r-- 1 zq2209 zq2209  23K Aug 14 21:53 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.4.fam
-rw-r--r-- 1 zq2209 zq2209 1.7G Aug 14 21:53 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.5.bed
-rw-r--r-- 1 zq2209 zq2209 231M Aug 14 21:53 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.5.bim
-rw-r--r-- 1 zq2209 zq2209  23K Aug 14 21:53 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.5.fam
-rw-r--r-- 1 zq2209 zq2209 1.7G Aug 14 21:53 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.6.bed
-rw-r--r-- 1 zq2209 zq2209 220M Aug 14 21:53 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.6.bim
-rw-r--r-- 1 zq2209 zq2209  23K Aug 14 21:53 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.6.fam
-rw-r--r-- 1 zq2209 zq2209 1.6G Aug 14 22:11 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.7.bed
-rw-r--r-- 1 zq2209 zq2209 214M Aug 14 22:11 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.7.bim
-rw-r--r-- 1 zq2209 zq2209  23K Aug 14 22:11 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.7.fam
-rw-r--r-- 1 zq2209 zq2209 1.5G Aug 14 21:53 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.8.bed
-rw-r--r-- 1 zq2209 zq2209 199M Aug 14 21:53 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.8.bim
-rw-r--r-- 1 zq2209 zq2209  23K Aug 14 21:53 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.8.fam
-rw-r--r-- 1 zq2209 zq2209 1.2G Aug 14 21:54 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.9.bed
-rw-r--r-- 1 zq2209 zq2209 160M Aug 14 21:54 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.9.bim
-rw-r--r-- 1 zq2209 zq2209  23K Aug 14 21:54 ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.9.fam
```


### Path(s) to omics-data matrix

- Wang Lab, `/mnt/vast/hpc/csg/zq2209/data_production/proteomics/rosmap/pheno`

```
$ ls -lh *.{gz}
-rw-r--r-- 1 zq2209 zq2209   35M Jun  1 13:09  rosmap_pheno.bed.gz
-rw-r--r-- 1 zq2209 zq2209  1.5M Jun  1 13:09  rosmap_pheno_chr10.bed.gz
-rw-r--r-- 1 zq2209 zq2209  2.2M Jun  1 13:09  rosmap_pheno_chr11.bed.gz
-rw-r--r-- 1 zq2209 zq2209  1.9M Jun  1 13:09  rosmap_pheno_chr12.bed.gz
-rw-r--r-- 1 zq2209 zq2209  655K Jun  1 13:09  rosmap_pheno_chr13.bed.gz
-rw-r--r-- 1 zq2209 zq2209  1.3M Jun  1 13:09  rosmap_pheno_chr14.bed.gz
-rw-r--r-- 1 zq2209 zq2209  1.1M Jun  1 13:09  rosmap_pheno_chr15.bed.gz
-rw-r--r-- 1 zq2209 zq2209  1.5M Jun  1 13:09  rosmap_pheno_chr16.bed.gz
-rw-r--r-- 1 zq2209 zq2209  2.1M Jun  1 13:09  rosmap_pheno_chr17.bed.gz
-rw-r--r-- 1 zq2209 zq2209  509K Jun  1 13:09  rosmap_pheno_chr18.bed.gz
-rw-r--r-- 1 zq2209 zq2209  2.1M Jun  1 13:09  rosmap_pheno_chr19.bed.gz
-rw-r--r-- 1 zq2209 zq2209  3.5M Jun  1 13:09  rosmap_pheno_chr1.bed.gz
-rw-r--r-- 1 zq2209 zq2209 1007K Jun  1 13:09  rosmap_pheno_chr20.bed.gz
-rw-r--r-- 1 zq2209 zq2209  299K Jun  1 13:09  rosmap_pheno_chr21.bed.gz
-rw-r--r-- 1 zq2209 zq2209  901K Jun  1 13:09  rosmap_pheno_chr22.bed.gz
-rw-r--r-- 1 zq2209 zq2209  2.5M Jun  1 13:09  rosmap_pheno_chr2.bed.gz
-rw-r--r-- 1 zq2209 zq2209  2.1M Jun  1 13:09  rosmap_pheno_chr3.bed.gz
-rw-r--r-- 1 zq2209 zq2209  1.4M Jun  1 13:09  rosmap_pheno_chr4.bed.gz
-rw-r--r-- 1 zq2209 zq2209  1.7M Jun  1 13:09  rosmap_pheno_chr5.bed.gz
-rw-r--r-- 1 zq2209 zq2209  1.8M Jun  1 13:09  rosmap_pheno_chr6.bed.gz
-rw-r--r-- 1 zq2209 zq2209  1.6M Jun  1 13:09  rosmap_pheno_chr7.bed.gz
-rw-r--r-- 1 zq2209 zq2209  1.2M Jun  1 13:09  rosmap_pheno_chr8.bed.gz
-rw-r--r-- 1 zq2209 zq2209  1.4M Jun  1 13:09  rosmap_pheno_chr9.bed.gz
-rw-r--r-- 1 zq2209 zq2209  1.3M Jun  1 13:09  rosmap_pheno_chrX.bed.gz
-rw-r--r-- 1 zq2209 zq2209  9.3K Jun  1 13:09  rosmap_pheno_chrY.bed.gz
```

### Path(s) to covariate data matrix

- Wang Lab, `/mnt/vast/hpc/csg/zq2209/data_production/proteomics/rosmap/cov`

```
$ ls -lh *.gz
-rw-r--r-- 1 zq2209 zq2209 201K Jun  1 13:13 rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.gz
```

### Path(s) to QTL results

- Wang lab: `/mnt/vast/hpc/csg/molecular_phenotype_calling/pQTL_cis/rosmap`
```
ls -lh *.txt
-rw-r--r-- 1 zq2209 zq2209  76K May 22 13:50 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.10.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209 487M May 22 13:47 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.10.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209 116K May 22 13:53 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.11.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209 678M May 22 13:49 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.11.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209 103K May 22 13:53 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.12.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209 629M May 22 13:50 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.12.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209  36K May 22 13:46 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.13.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209 233M May 22 13:45 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.13.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209  66K May 22 13:48 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.14.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209 424M May 22 13:46 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.14.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209  58K May 22 13:52 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.15.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209 317M May 22 13:51 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.15.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209  83K May 22 13:54 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.16.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209 514M May 22 13:51 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.16.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209 114K May 22 13:59 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.17.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209 693M May 22 13:55 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.17.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209  27K May 22 13:55 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.18.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209 169M May 22 13:54 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.18.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209 112K May 22 13:59 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.19.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209 831M May 22 13:55 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.19.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209 187K May 22 13:42 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.1.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209 1.1G May 22 13:36 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.1.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209  54K May 22 13:58 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.20.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209 334M May 22 13:56 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.20.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209  16K May 22 13:56 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.21.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209 102M May 22 13:56 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.21.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209  50K May 22 13:55 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.22.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209 331M May 22 13:53 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.22.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209 131K May 22 13:44 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.2.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209 755M May 22 13:40 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.2.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209 110K May 22 13:44 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.3.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209 637M May 22 13:40 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.3.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209  71K May 22 13:43 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.4.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209 450M May 22 13:41 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.4.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209  87K May 22 13:39 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.5.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209 521M May 22 13:36 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.5.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209  95K May 22 13:48 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.6.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209 803M May 22 13:44 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.6.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209  85K May 22 13:38 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.7.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209 545M May 22 13:35 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.7.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209  64K May 22 13:38 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.8.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209 387M May 22 13:36 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.8.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209  75K May 22 13:48 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.9.emprical.cis_sumstats.txt
-rw-r--r-- 1 zq2209 zq2209 475M May 22 13:46 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.9.norminal.cis_long_table.txt
-rw-r--r-- 1 zq2209 zq2209 2.4M May 22 13:59 pheno_recipe_rosmap_pheno.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.Marchenko_pc.emprical.cis_sumstats.txt
```

- FTP: 

### Path(s) to fine-mapping with SuSiE model

### Path(s) to fine-mapping with SuSiE RSS model

