# ROSMAP DLPFC H3K9ac QTL

Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) h3k9ac QTL analysis using the FGC xQTL pipeline. 

Please refer to [this document](../study_info/ROSMAP.md) for an overview of the ROSMAP project.

## Contact

Xuanhe Chen (xuanhechenxhc@163.com)

## Study Overview
 
- Study name : ROSMAP DLPFC H3K9ac QTL
- Study Description : Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) h3k9ac QTL analysis summary statistics using the FGC xQTL pipeline. 

Samples' phenotype information (sex, age, race etc.) can be found in ROSMAP metadata, see "Other information" section in [this document](../study_info/ROSMAP.md)

## Analysis Status

TransQTL association: Need to be performed.

## Analysis Details

### Sample size tracking through the analysis workflow

| Step                                                  | Sample Size |
| ----------------------------------------------------- | ----------- |
| Raw data                                              | 669         |
| Sample 90214403 as been removed from 2022Feb08 ROSMAP | 668         |
| After overlapping with ROSMAP WGS                     | 607         |
| After overlapping with ROSMAP joint call              | 596         |

### QC and Normalization Details for Phenotype Data

Used h3k9ac readcount data directly without further QC. For QCs performed in Chip-seq and peak calling please refer to `descriptor/omics/ROSMAP_DLPFC_ChIPSeq_H3K9ac.md`

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

- https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Wang_Columbia/haqtl

The notebooks in this folder contain the commands and data wrangling codes for analysis of the h3k9ac data in ROSMAP. (data wrangling exist because not all data are processed using the xqtl-pipeline from the beginning and need to be reformatted to fit one intermediate step of the pipeline).

### Association data preprocessing
#### Genotype data preprocessing
We conducted Whole Genome Sequencing (WGS) on 1160 DLPFC samples as part of the ROSMAP study. Post-sequencing, these samples were aligned to the GRCh38 reference genome, and the resulting genetic variants were meticulously cataloged, subsequently being saved in VCF (Variant Call Format) files. To ensure the integrity of our findings, we embarked on a rigorous quality control regimen. This involved the utilization of the GRCh38 reference genome complemented by the GENCODE 34 annotation. Notably, our quality control approach was further augmented by integrating the ERCC spike-in annotations, ensuring comprehensive and accurate genomic data analysis. Specific parameters were meticulously applied: a read depth (--DP) of 1, an indel depth (--DP-indel) of 1, and a Genotype Quality (GQ) threshold exceeding 20. Furthermore, each site was mandated to have at least one sample surpassing the allele balance threshold, specifically set at >= 0.15 for Single Nucleotide Polymorphisms (SNPs) and >= 0.20 for insertion-deletion mutations (indels). This structured approach aimed to ensure a systematic and logical progression in our genomic analysis, reinforcing the academic rigor of our research. After the initial QC, the VCF files were merged using PLINK for downstream analysis. Subsequently, we applied further filters to exclude variants with more than 10% missing data and set a Hardy-Weinberg Equilibrium (HWE) cutoff of 1E-8. The generated genotype files will be subjected to subsequent Principal Component analysis (PCA) as part of the covariates, as well as utilized for QTL mapping. 

#### Principal component analysis for haQTL mapping (this would be the new pipeline)
For the generation of a covariate file for QTL mapping, we initiated the process with Principal Component analysis (PCA) applied to both genome and phenotype data, incorporating several pivotal steps. In the quality control stage, we utilized the KING to segregate samples into related and unrelated categories. PCA was then performed on the unrelated samples using the flashpcaR library, followed by outlier detection to identify pertinent genotype PCs. We retained those with a cumulative explained variance (PVE_cum) of 0.8 or higher and combined them with relevant metadata sexm, gender and post-mortem interval (pmi).
Subsequently, we calculated residuals on these merged covariates and embarked on hidden factor analysis to identify potential batch effects or artifacts in the phenotype data. The number of principal components to be included was determined through a comparison of their eigenvalues to the Marchenko-Pastur Distribution. The principal components identified as hidden factors were incorporated with genotype PCs and metadata into the final amalgamation, serving as the basis for subsequent QTL mapping analysis. 


phenotype preprocessing can be run in parallel but covariate preprocessing needsto be done last since it requires both phenotype data and PCs from PCA in genotype preprocessing.

- [genotype_preprocessing.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/haqtl/genotype_preprocessing.ipynb) shows the commands used for genotype processing and preparation steps.
  - Includes QC, PCA, and PCA result figures, for example [h3k9ac_whole.k9_cov.xqtl_protocol_data.filtered.h3k9ac.related.filtered.extracted.pca.projected.resid.PEER.diag.pdf](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/haqtl/figures/h3k9ac_whole.k9_cov.xqtl_protocol_data.filtered.h3k9ac.related.filtered.extracted.pca.projected.resid.PEER.diag.pdf) is the view of PCA result of the haQTL analysis.
- [phenotype_preprocessing.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/haqtl/phenotype_preprocessing.ipynb) shows the commands used for the phenotype data processing and preparation steps.
  - This notebook strated from some already cleaned data and convert them to bed format inputs taken by tensorQTL.
- [covariate_preprocessing.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/haqtl/covariates_preprocessing.ipynb) shows the commands used for the covariate data processing and preparation steps.
  - This includes PEER factor analysis steps and merging the PEER factors to covariates in raw data and PCA. 
  
### Association scan using TensorQTL and summary statistics standardization
For molecular cis-QTL mapping, we utilized quantified H3K9ac levels in BED format as phenotypes, principal components (PCs) obtained as previously described as covariates, and corresponding genotype data from the same dataset in PLINK format, as delineated in prior descriptions. 
We employed the TensorQTL pipeline to perform the association analysis, setting a minor allele count (MAC) cutoff of 5. This approach allowed us to generate phenotype-level summary statistics with empirical p-values, facilitating the calculation of genome-wide false discovery rates (FDR) through permutations. Additionally, summary statistics were obtained for all variant-phenotype pairs.
During this process, we strategically expanded the cis window to capture signals that were not confined to the coordinate level, but rather operated on the spatial level within a specific region. The cis window was meticulously defined as a region encompassing 1,000,000 base pairs, in addition to the topologically associated domain (TAD) and its boundary (TAB). This was executed with an understanding that variants located within this spatial domain could exert an impact on gene expression, thus associating with the corresponding gene. In instances where a gene was positioned within the confines of two generalized TABD boundaries, we systematically selected the outermost TABD boundary for incorporation into the cis window definition, ensuring a comprehensive and rigorous approach to our spatial genomic analysis.

### Aggregating QTLs across datasets?

- [cis_haqtl_association.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/haqtl/cis_haqtl_association.ipynb) provides information about the TensorQTL cis association scan.

### SuSiE univariate fine mapping

- [univariate_fine_mapping.ipynb](https://github.com/cumc/xqtl-pipeline/blob/main/code/fine_mapping/univariate_fine_mapping.ipynb) contains the workflow of haQTL univariate fine mapping.

## Dataset Details

- Number of cases : 
- Number of controls :
- Annotation information : 
- Genotype level imputation : 
- Imputation Panel : 

### Path(s) to genotype matrix 

**output of genotype_preprocessing.ipynb**

- Wang Lab, `/mnt/vast/hpc/csg/molecular_phenotype_calling/genotype_arch`

```
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

**output of phenotype_preprocessing.ipynb**

- Wang Lab, `/mnt/mfs/hgrcgrid/homes/xc2610/k9_data/pheno/`

```
$ ls -lh *.{txt,gz}
-rw-r--r-- 1 xc2610 xc2610 1.5K Sep 30 01:20 h3k9ac_bed_recipe.txt
-rw-r--r-- 1 xc2610 xc2610 3.3M Sep 30 00:05 h3k9ac_chr10.bed.gz
-rw-r--r-- 1 xc2610 xc2610 4.1M Sep 30 00:06 h3k9ac_chr11.bed.gz
-rw-r--r-- 1 xc2610 xc2610 3.4M Sep 30 00:06 h3k9ac_chr12.bed.gz
-rw-r--r-- 1 xc2610 xc2610 1.5M Sep 30 00:06 h3k9ac_chr13.bed.gz
-rw-r--r-- 1 xc2610 xc2610 2.3M Sep 30 00:06 h3k9ac_chr14.bed.gz
-rw-r--r-- 1 xc2610 xc2610 2.3M Sep 30 00:06 h3k9ac_chr15.bed.gz
-rw-r--r-- 1 xc2610 xc2610 2.7M Sep 30 00:06 h3k9ac_chr16.bed.gz
-rw-r--r-- 1 xc2610 xc2610 4.0M Sep 30 00:06 h3k9ac_chr17.bed.gz
-rw-r--r-- 1 xc2610 xc2610 1.3M Sep 30 00:06 h3k9ac_chr18.bed.gz
-rw-r--r-- 1 xc2610 xc2610 3.2M Sep 30 00:06 h3k9ac_chr19.bed.gz
-rw-r--r-- 1 xc2610 xc2610 6.8M Sep 30 00:05 h3k9ac_chr1.bed.gz
-rw-r--r-- 1 xc2610 xc2610 2.1M Sep 30 00:06 h3k9ac_chr20.bed.gz
-rw-r--r-- 1 xc2610 xc2610 672K Sep 30 00:06 h3k9ac_chr21.bed.gz
-rw-r--r-- 1 xc2610 xc2610 1.9M Sep 30 00:06 h3k9ac_chr22.bed.gz
-rw-r--r-- 1 xc2610 xc2610 4.8M Sep 30 00:05 h3k9ac_chr2.bed.gz
-rw-r--r-- 1 xc2610 xc2610 4.0M Sep 30 00:05 h3k9ac_chr3.bed.gz
-rw-r--r-- 1 xc2610 xc2610 2.5M Sep 30 00:05 h3k9ac_chr4.bed.gz
-rw-r--r-- 1 xc2610 xc2610 3.3M Sep 30 00:05 h3k9ac_chr5.bed.gz
-rw-r--r-- 1 xc2610 xc2610 3.5M Sep 30 00:05 h3k9ac_chr6.bed.gz
-rw-r--r-- 1 xc2610 xc2610 3.1M Sep 30 00:05 h3k9ac_chr7.bed.gz
-rw-r--r-- 1 xc2610 xc2610 2.6M Sep 30 00:06 h3k9ac_chr8.bed.gz
-rw-r--r-- 1 xc2610 xc2610 3.2M Sep 30 00:06 h3k9ac_chr9.bed.gz
```

### Path(s) to covariate data matrix 

**output of covariate_preprocessing.ipynb**

- Wang Lab, `/mnt/mfs/hgrcgrid/homes/xc2610/k9_data/pheno/cov_new`

```
$ ls -lh *.gz
-rw-r--r-- 1 xc2610 xc2610 391K Oct  1 02:54 h3k9ac_whole.k9_cov.xqtl_protocol_data.filtered.related.filtered.extracted.pca.projected.resid.PEER.merged.gz
```

### Path(s) to cis-QTL association testing

**output of cis_haqtl_association.ipynb**

- `/projects/histone-methylation/CU/h3k9_sumstats/`
```
ls -lh *.txt
-rw-r--r-- 1 xc2610 root 7.5G Nov 29 13:44 h3k9ac_bed_recipe_h3k9ac_whole.k9_cov.xqtl_protocol_data.filtered.related.filtered.extracted.pca.projected.resid.PEER.merged.10.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 root 8.4G Nov 29 13:46 h3k9ac_bed_recipe_h3k9ac_whole.k9_cov.xqtl_protocol_data.filtered.related.filtered.extracted.pca.projected.resid.PEER.merged.11.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 root 7.3G Nov 29 13:47 h3k9ac_bed_recipe_h3k9ac_whole.k9_cov.xqtl_protocol_data.filtered.related.filtered.extracted.pca.projected.resid.PEER.merged.12.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 root 3.3G Nov 29 13:48 h3k9ac_bed_recipe_h3k9ac_whole.k9_cov.xqtl_protocol_data.filtered.related.filtered.extracted.pca.projected.resid.PEER.merged.13.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 root 5.1G Nov 29 13:49 h3k9ac_bed_recipe_h3k9ac_whole.k9_cov.xqtl_protocol_data.filtered.related.filtered.extracted.pca.projected.resid.PEER.merged.14.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 root 4.6G Nov 29 13:49 h3k9ac_bed_recipe_h3k9ac_whole.k9_cov.xqtl_protocol_data.filtered.related.filtered.extracted.pca.projected.resid.PEER.merged.15.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 root 5.7G Nov 29 13:50 h3k9ac_bed_recipe_h3k9ac_whole.k9_cov.xqtl_protocol_data.filtered.related.filtered.extracted.pca.projected.resid.PEER.merged.16.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 root 8.5G Nov 29 13:52 h3k9ac_bed_recipe_h3k9ac_whole.k9_cov.xqtl_protocol_data.filtered.related.filtered.extracted.pca.projected.resid.PEER.merged.17.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 root 2.7G Nov 29 13:52 h3k9ac_bed_recipe_h3k9ac_whole.k9_cov.xqtl_protocol_data.filtered.related.filtered.extracted.pca.projected.resid.PEER.merged.18.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 root 7.7G Nov 29 13:53 h3k9ac_bed_recipe_h3k9ac_whole.k9_cov.xqtl_protocol_data.filtered.related.filtered.extracted.pca.projected.resid.PEER.merged.19.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 root  14G Nov 29 13:43 h3k9ac_bed_recipe_h3k9ac_whole.k9_cov.xqtl_protocol_data.filtered.related.filtered.extracted.pca.projected.resid.PEER.merged.1.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 root 4.4G Nov 29 13:56 h3k9ac_bed_recipe_h3k9ac_whole.k9_cov.xqtl_protocol_data.filtered.related.filtered.extracted.pca.projected.resid.PEER.merged.20.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 root 1.6G Nov 29 13:56 h3k9ac_bed_recipe_h3k9ac_whole.k9_cov.xqtl_protocol_data.filtered.related.filtered.extracted.pca.projected.resid.PEER.merged.21.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 root 4.4G Nov 29 13:57 h3k9ac_bed_recipe_h3k9ac_whole.k9_cov.xqtl_protocol_data.filtered.related.filtered.extracted.pca.projected.resid.PEER.merged.22.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 root 9.8G Nov 29 13:55 h3k9ac_bed_recipe_h3k9ac_whole.k9_cov.xqtl_protocol_data.filtered.related.filtered.extracted.pca.projected.resid.PEER.merged.2.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 root 7.9G Nov 29 13:58 h3k9ac_bed_recipe_h3k9ac_whole.k9_cov.xqtl_protocol_data.filtered.related.filtered.extracted.pca.projected.resid.PEER.merged.3.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 root 5.6G Nov 29 13:59 h3k9ac_bed_recipe_h3k9ac_whole.k9_cov.xqtl_protocol_data.filtered.related.filtered.extracted.pca.projected.resid.PEER.merged.4.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 root 6.9G Nov 29 14:00 h3k9ac_bed_recipe_h3k9ac_whole.k9_cov.xqtl_protocol_data.filtered.related.filtered.extracted.pca.projected.resid.PEER.merged.5.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 root 8.6G Nov 29 14:02 h3k9ac_bed_recipe_h3k9ac_whole.k9_cov.xqtl_protocol_data.filtered.related.filtered.extracted.pca.projected.resid.PEER.merged.6.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 root 6.9G Nov 29 14:03 h3k9ac_bed_recipe_h3k9ac_whole.k9_cov.xqtl_protocol_data.filtered.related.filtered.extracted.pca.projected.resid.PEER.merged.7.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 root 5.8G Nov 29 14:04 h3k9ac_bed_recipe_h3k9ac_whole.k9_cov.xqtl_protocol_data.filtered.related.filtered.extracted.pca.projected.resid.PEER.merged.8.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 root 7.0G Nov 29 14:05 h3k9ac_bed_recipe_h3k9ac_whole.k9_cov.xqtl_protocol_data.filtered.related.filtered.extracted.pca.projected.resid.PEER.merged.9.norminal.cis_long_table.txt
-rw-r--r-- 1 xc2610 root  32M Nov 29 14:05 h3k9ac_bed_recipe_h3k9ac_whole.k9_cov.xqtl_protocol_data.filtered.related.filtered.extracted.pca.projected.resid.PEER.merged.emprical.cis_sumstats.txt
```
- FTP: `/ftp_fgc_xqtl/projects/histone-methylation/CU/h3k9_sumstats/`

### Path(s) to fine-mapping with SuSiE model 

**output of univariate_fine_mapping.ipynb**

- Wang lab: `/mnt/vast/hpc/csg/molecular_phenotype_calling/QTL_fine_mapping/output/haQTL_pure_completed_unlimited.tsv`

```
-rw-r--r-- 1 hs3163 hs3163 3.5M Apr 21 16:19 /mnt/vast/hpc/csg/molecular_phenotype_calling/QTL_fine_mapping/output/haQTL_pure_completed_unlimited.tsv
```

### Path(s) to fine-mapping with SuSiE RSS model
