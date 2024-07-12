# STARNET macrophage gene expression QTL

STARNET is an RNA expression study of various disease-relevant tissues obtained from living patients with cardiovascular disease (CVD). The inclusion criterion for patients was eligibility for coronary artery by-pass graft (CABG) surgery.

## Contact

- Contact Name: Travyse Edwards
- Contact Email: travyse.edwards@icahn.mssm.edu
- Contact Affiliation: Icahn School of Medicine at Mount Sinai
- Contact Role: Travyse performed QC & QTL analysis

## Study Overview

- Study name : STARNET Macrophage eQTL
- Study Description : Stockholm-Tartu Atherosclerosis Reverse Network Engineering Task (STARNET) macrophage eQTL analysis summary statistics generated using the FGC xQTL pipeline.

## Analysis Details

### Sample Size Tracking Through Analysis Workflow

|Step |Sample Size|
|-----|-----------|
|Raw Expression Data|480|
|QC'd Expression Data|479|
|After overlapping with STARNET genotype data|471|

### Quality Control and Normalization Details for Phenotype Data

For quality control performed for the macrophage gene expression dataset, please refer to [this markdown document](https://github.com/Travyse/brain-xqtl-analysis/blob/main/data/descriptor/omics/STARNET_macrophage.md).

### Genotype Parameters

|Parameter |Value|
|----------|-----|
|Minimum Minor Allele Freq|0.01|
|Maximum Minor Allele Freq|0.99|
|Kinship Coefficient for Related Individuals|0.0625|
|Maximum Missingness Per Variant|0.1|
|Maximum Missingness Per Sample|0.1|
|Hardy-Weinberg Equilibrium Filter|1e-15|

### Covariate Parameters

PCA Analysis:

|Parameter |Value|
|----------|-----|
|Minor Allele Freq for PCA|0.01|
|LD Pruning: Window|0.1|
|LD Pruning: Shift|0.1|
|LD Pruning: Window|0.1|
|Number of PCs|13|

PEER Analysis:

|Parameter |Value|
|----------|-----|
|Max Iterations|1000|
|Prior Parameter: `Alpha_a`|0.001|
|Prior Parameter: `Alpha_b`|0.1|
|Prior Parameter: `Eps_a`|0.1|
|Prior Parameter: `Eps_b`|10.0|
|Tolerance Parameter: `tol`|0.001|
|Tolerance Parameter: `var_tol`|1e-5|
|Convergence Mode| "fast"|

Final Covariates: Sex, Age, PCs (13), PEER Factors (60)

PCA Method for Latent Factor Identification (Using Marchenko-Pastur Method):

TBD

### TensorQTL Parameters

|Parameter |Value|
|----------|-----|
|Cis Window|1,000,000|
|Minor Allele Count Cutoff|0|
|Minor Allele Freq Cutoff|0|

## Links to QTL analysis notebooks

Currently rearranging this section and below

The notebooks in this folder, 

https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Marcora_MSSM/STARNET

contain the commands and some of the results visualizations produced by the pipeline when analyzing the STARNET macrophage RNA-seq expression data.

- `STARNET_Analysis_Complete.ipynb` provides information about the imputation of genotype, summary from other preprocessing steps, and a look into the cisQTL association scan.
- `genotype_preprocessing.ipynb` shows the commands used for genotype processing and preparation steps.
  - Mostly contains the commands used to run the pipeline, but includes some pre-pipeline data wrangling.
  - This includes QC, PCA, and GRM steps
- `phenotype_preprocessing.ipynb` shows the commands used for the phenotype data processing and preparation steps.
  - As above, it mostly contains the commands used to run the pipeline, but includes some pre-pipeline data wrangling.
  - This includes quantification steps, QC, annotation, and residual expression steps
- `covariate_preprocessing.ipynb` shows the commands used for the covariate data processing and preparation steps.
  - This includes factor analysis steps
- `association_scan_cis.ipynb` provides information about the TensorQTL cis association scan.

## Dataset Details

- Number of cases :
- Number of controls :
- Annotation information :
- Genotype level imputation :
- Imputation Panel :

### Path(s) to Genotype Matrix

- Goate Lab (Minerva), `/sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/`
```
$ ls -lh /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/*.{bed,bim,fam}
-rw-r-xr--+ 1 edwart10 LOAD  58M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.10.bed
-rw-r-xr--+ 1 edwart10 LOAD  19M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.10.bim
-rw-r-xr--+ 1 edwart10 LOAD  14K May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.10.fam
-rw-r-xr--+ 1 edwart10 LOAD  57M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.11.bed
-rw-r-xr--+ 1 edwart10 LOAD  18M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.11.bim
-rw-r-xr--+ 1 edwart10 LOAD  14K May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.11.fam
-rw-r-xr--+ 1 edwart10 LOAD  55M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.12.bed
-rw-r-xr--+ 1 edwart10 LOAD  18M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.12.bim
-rw-r-xr--+ 1 edwart10 LOAD  14K May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.12.fam
-rw-r-xr--+ 1 edwart10 LOAD  43M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.13.bed
-rw-r-xr--+ 1 edwart10 LOAD  14M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.13.bim
-rw-r-xr--+ 1 edwart10 LOAD  14K May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.13.fam
-rw-r-xr--+ 1 edwart10 LOAD  37M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.14.bed
-rw-r-xr--+ 1 edwart10 LOAD  12M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.14.bim
-rw-r-xr--+ 1 edwart10 LOAD  14K May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.14.fam
-rw-r-xr--+ 1 edwart10 LOAD  32M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.15.bed
-rw-r-xr--+ 1 edwart10 LOAD  11M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.15.bim
-rw-r-xr--+ 1 edwart10 LOAD  14K May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.15.fam
-rw-r-xr--+ 1 edwart10 LOAD  35M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.16.bed
-rw-r-xr--+ 1 edwart10 LOAD  11M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.16.bim
-rw-r-xr--+ 1 edwart10 LOAD  14K May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.16.fam
-rw-r-xr--+ 1 edwart10 LOAD  31M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.17.bed
-rw-r-xr--+ 1 edwart10 LOAD 9.5M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.17.bim
-rw-r-xr--+ 1 edwart10 LOAD  14K May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.17.fam
-rw-r-xr--+ 1 edwart10 LOAD  33M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.18.bed
-rw-r-xr--+ 1 edwart10 LOAD  11M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.18.bim
-rw-r-xr--+ 1 edwart10 LOAD  14K May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.18.fam
-rw-r-xr--+ 1 edwart10 LOAD  26M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.19.bed
-rw-r-xr--+ 1 edwart10 LOAD 8.0M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.19.bim
-rw-r-xr--+ 1 edwart10 LOAD  14K May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.19.fam
-rw-r-xr--+ 1 edwart10 LOAD  89M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.1.bed
-rw-r-xr--+ 1 edwart10 LOAD  28M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.1.bim
-rw-r-xr--+ 1 edwart10 LOAD  14K May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.1.fam
-rw-r-xr--+ 1 edwart10 LOAD  26M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.20.bed
-rw-r-xr--+ 1 edwart10 LOAD 8.0M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.20.bim
-rw-r-xr--+ 1 edwart10 LOAD  14K May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.20.fam
-rw-r-xr--+ 1 edwart10 LOAD  16M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.21.bed
-rw-r-xr--+ 1 edwart10 LOAD 4.9M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.21.bim
-rw-r-xr--+ 1 edwart10 LOAD  14K May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.21.fam
-rw-r-xr--+ 1 edwart10 LOAD  16M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.22.bed
-rw-r-xr--+ 1 edwart10 LOAD 4.8M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.22.bim
-rw-r-xr--+ 1 edwart10 LOAD  14K May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.22.fam
-rw-r-xr--+ 1 edwart10 LOAD  96M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.2.bed
-rw-r-xr--+ 1 edwart10 LOAD  30M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.2.bim
-rw-r-xr--+ 1 edwart10 LOAD  14K May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.2.fam
-rw-r-xr--+ 1 edwart10 LOAD  81M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.3.bed
-rw-r-xr--+ 1 edwart10 LOAD  25M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.3.bim
-rw-r-xr--+ 1 edwart10 LOAD  14K May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.3.fam
-rw-r-xr--+ 1 edwart10 LOAD  83M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.4.bed
-rw-r-xr--+ 1 edwart10 LOAD  26M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.4.bim
-rw-r-xr--+ 1 edwart10 LOAD  14K May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.4.fam
-rw-r-xr--+ 1 edwart10 LOAD  74M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.5.bed
-rw-r-xr--+ 1 edwart10 LOAD  23M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.5.bim
-rw-r-xr--+ 1 edwart10 LOAD  14K May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.5.fam
-rw-r-xr--+ 1 edwart10 LOAD  76M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.6.bed
-rw-r-xr--+ 1 edwart10 LOAD  24M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.6.bim
-rw-r-xr--+ 1 edwart10 LOAD  14K May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.6.fam
-rw-r-xr--+ 1 edwart10 LOAD  67M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.7.bed
-rw-r-xr--+ 1 edwart10 LOAD  21M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.7.bim
-rw-r-xr--+ 1 edwart10 LOAD  14K May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.7.fam
-rw-r-xr--+ 1 edwart10 LOAD  63M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.8.bed
-rw-r-xr--+ 1 edwart10 LOAD  19M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.8.bim
-rw-r-xr--+ 1 edwart10 LOAD  14K May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.8.fam
-rw-r-xr--+ 1 edwart10 LOAD  50M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.9.bed
-rw-r-xr--+ 1 edwart10 LOAD  15M May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.9.bim
-rw-r-xr--+ 1 edwart10 LOAD  14K May 28  2022 /sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Data-Pre-Processing/Genotype-Data-Pre-Processing/output/genotype_by_chrom/STARNET_qced.9.fam
```
### Path(s) to Phenotype Matrix

- Goate lab, `/sc/arion/projects/load/users/edwart10/projects/04-19-2023-STARNET-PCA-Replication/output/data-preprocessing/phenotype/per_chrom/`
```
$ ls -lh /sc/arion/projects/load/users/edwart10/projects/04-19-2023-STARNET-PCA-Replication/output/data-preprocessing/phenotype/per_chrom/*.bed.gz
-rw-r-xr--+ 1 edwart10 LOAD 1.8M Apr 20 12:00 /sc/arion/projects/load/users/edwart10/projects/04-19-2023-STARNET-PCA-Replication/output/data-preprocessing/phenotype/per_chrom/STARNET.tpm.gct.bed.chr10.bed.gz
-rw-r-xr--+ 1 edwart10 LOAD 2.5M Apr 20 12:00 /sc/arion/projects/load/users/edwart10/projects/04-19-2023-STARNET-PCA-Replication/output/data-preprocessing/phenotype/per_chrom/STARNET.tpm.gct.bed.chr11.bed.gz
-rw-r-xr--+ 1 edwart10 LOAD 2.5M Apr 20 12:00 /sc/arion/projects/load/users/edwart10/projects/04-19-2023-STARNET-PCA-Replication/output/data-preprocessing/phenotype/per_chrom/STARNET.tpm.gct.bed.chr12.bed.gz
-rw-r-xr--+ 1 edwart10 LOAD 842K Apr 20 12:00 /sc/arion/projects/load/users/edwart10/projects/04-19-2023-STARNET-PCA-Replication/output/data-preprocessing/phenotype/per_chrom/STARNET.tpm.gct.bed.chr13.bed.gz
-rw-r-xr--+ 1 edwart10 LOAD 1.6M Apr 20 12:00 /sc/arion/projects/load/users/edwart10/projects/04-19-2023-STARNET-PCA-Replication/output/data-preprocessing/phenotype/per_chrom/STARNET.tpm.gct.bed.chr14.bed.gz
-rw-r-xr--+ 1 edwart10 LOAD 1.6M Apr 20 12:00 /sc/arion/projects/load/users/edwart10/projects/04-19-2023-STARNET-PCA-Replication/output/data-preprocessing/phenotype/per_chrom/STARNET.tpm.gct.bed.chr15.bed.gz
-rw-r-xr--+ 1 edwart10 LOAD 2.3M Apr 20 12:00 /sc/arion/projects/load/users/edwart10/projects/04-19-2023-STARNET-PCA-Replication/output/data-preprocessing/phenotype/per_chrom/STARNET.tpm.gct.bed.chr16.bed.gz
-rw-r-xr--+ 1 edwart10 LOAD 2.8M Apr 20 12:00 /sc/arion/projects/load/users/edwart10/projects/04-19-2023-STARNET-PCA-Replication/output/data-preprocessing/phenotype/per_chrom/STARNET.tpm.gct.bed.chr17.bed.gz
-rw-r-xr--+ 1 edwart10 LOAD 723K Apr 20 12:00 /sc/arion/projects/load/users/edwart10/projects/04-19-2023-STARNET-PCA-Replication/output/data-preprocessing/phenotype/per_chrom/STARNET.tpm.gct.bed.chr18.bed.gz
-rw-r-xr--+ 1 edwart10 LOAD 3.0M Apr 20 12:00 /sc/arion/projects/load/users/edwart10/projects/04-19-2023-STARNET-PCA-Replication/output/data-preprocessing/phenotype/per_chrom/STARNET.tpm.gct.bed.chr19.bed.gz
-rw-r-xr--+ 1 edwart10 LOAD 4.6M Apr 20 12:00 /sc/arion/projects/load/users/edwart10/projects/04-19-2023-STARNET-PCA-Replication/output/data-preprocessing/phenotype/per_chrom/STARNET.tpm.gct.bed.chr1.bed.gz
-rw-r-xr--+ 1 edwart10 LOAD 1.2M Apr 20 12:00 /sc/arion/projects/load/users/edwart10/projects/04-19-2023-STARNET-PCA-Replication/output/data-preprocessing/phenotype/per_chrom/STARNET.tpm.gct.bed.chr20.bed.gz
-rw-r-xr--+ 1 edwart10 LOAD 489K Apr 20 12:00 /sc/arion/projects/load/users/edwart10/projects/04-19-2023-STARNET-PCA-Replication/output/data-preprocessing/phenotype/per_chrom/STARNET.tpm.gct.bed.chr21.bed.gz
-rw-r-xr--+ 1 edwart10 LOAD 1.2M Apr 20 12:00 /sc/arion/projects/load/users/edwart10/projects/04-19-2023-STARNET-PCA-Replication/output/data-preprocessing/phenotype/per_chrom/STARNET.tpm.gct.bed.chr22.bed.gz
-rw-r-xr--+ 1 edwart10 LOAD 3.0M Apr 20 12:00 /sc/arion/projects/load/users/edwart10/projects/04-19-2023-STARNET-PCA-Replication/output/data-preprocessing/phenotype/per_chrom/STARNET.tpm.gct.bed.chr2.bed.gz
-rw-r-xr--+ 1 edwart10 LOAD 2.5M Apr 20 12:00 /sc/arion/projects/load/users/edwart10/projects/04-19-2023-STARNET-PCA-Replication/output/data-preprocessing/phenotype/per_chrom/STARNET.tpm.gct.bed.chr3.bed.gz
-rw-r-xr--+ 1 edwart10 LOAD 1.6M Apr 20 12:00 /sc/arion/projects/load/users/edwart10/projects/04-19-2023-STARNET-PCA-Replication/output/data-preprocessing/phenotype/per_chrom/STARNET.tpm.gct.bed.chr4.bed.gz
-rw-r-xr--+ 1 edwart10 LOAD 2.0M Apr 20 12:00 /sc/arion/projects/load/users/edwart10/projects/04-19-2023-STARNET-PCA-Replication/output/data-preprocessing/phenotype/per_chrom/STARNET.tpm.gct.bed.chr5.bed.gz
-rw-r-xr--+ 1 edwart10 LOAD 2.4M Apr 20 12:00 /sc/arion/projects/load/users/edwart10/projects/04-19-2023-STARNET-PCA-Replication/output/data-preprocessing/phenotype/per_chrom/STARNET.tpm.gct.bed.chr6.bed.gz
-rw-r-xr--+ 1 edwart10 LOAD 2.2M Apr 20 12:00 /sc/arion/projects/load/users/edwart10/projects/04-19-2023-STARNET-PCA-Replication/output/data-preprocessing/phenotype/per_chrom/STARNET.tpm.gct.bed.chr7.bed.gz
-rw-r-xr--+ 1 edwart10 LOAD 1.6M Apr 20 12:00 /sc/arion/projects/load/users/edwart10/projects/04-19-2023-STARNET-PCA-Replication/output/data-preprocessing/phenotype/per_chrom/STARNET.tpm.gct.bed.chr8.bed.gz
-rw-r-xr--+ 1 edwart10 LOAD 1.8M Apr 20 12:00 /sc/arion/projects/load/users/edwart10/projects/04-19-2023-STARNET-PCA-Replication/output/data-preprocessing/phenotype/per_chrom/STARNET.tpm.gct.bed.chr9.bed.gz
```

### Path(s) to Covariate Matrix

- Goate lab, `/sc/arion/projects/load/users/edwart10/projects/04-19-2023-STARNET-PCA-Replication/output/no-status/data-preprocessing/covariates/STARNET.MP.cov.merged.gz`
  
```
-rw-r-x---+ 1 edwart10 LOAD 204K May  4 09:57 STARNET.MP.cov.merged.gz
```

### Path(s) to cis-eQTL Results

- Goate lab, `/sc/arion/projects/load/users/edwart10/projects/04-19-2023-STARNET-PCA-Replication/output/no-status/association_scan/TensorQTL/Marchenko-Pastur-Method`

```
$ ls -lh *.cis_long_table.txt
-rw-r-xr--+ 1 edwart10 LOAD 995M May  6 11:46 STARNET.tpm.gct.bed.per_chrom_STARNET.MP.cov.merged.10.norminal.cis_long_table.txt
-rw-r-xr--+ 1 edwart10 LOAD 1.3G May  6 11:49 STARNET.tpm.gct.bed.per_chrom_STARNET.MP.cov.merged.11.norminal.cis_long_table.txt
-rw-r-xr--+ 1 edwart10 LOAD 1.4G May  6 11:48 STARNET.tpm.gct.bed.per_chrom_STARNET.MP.cov.merged.12.norminal.cis_long_table.txt
-rw-r-xr--+ 1 edwart10 LOAD 516M May  6 11:45 STARNET.tpm.gct.bed.per_chrom_STARNET.MP.cov.merged.13.norminal.cis_long_table.txt
-rw-r-xr--+ 1 edwart10 LOAD 908M May  6 11:46 STARNET.tpm.gct.bed.per_chrom_STARNET.MP.cov.merged.14.norminal.cis_long_table.txt
-rw-r-xr--+ 1 edwart10 LOAD 820M May  6 11:46 STARNET.tpm.gct.bed.per_chrom_STARNET.MP.cov.merged.15.norminal.cis_long_table.txt
-rw-r-xr--+ 1 edwart10 LOAD 1.3G May  6 11:46 STARNET.tpm.gct.bed.per_chrom_STARNET.MP.cov.merged.16.norminal.cis_long_table.txt
-rw-r-xr--+ 1 edwart10 LOAD 1.5G May  6 11:46 STARNET.tpm.gct.bed.per_chrom_STARNET.MP.cov.merged.17.norminal.cis_long_table.txt
-rw-r-xr--+ 1 edwart10 LOAD 452M May  6 11:45 STARNET.tpm.gct.bed.per_chrom_STARNET.MP.cov.merged.18.norminal.cis_long_table.txt
-rw-r-xr--+ 1 edwart10 LOAD 1.8G May  6 11:47 STARNET.tpm.gct.bed.per_chrom_STARNET.MP.cov.merged.19.norminal.cis_long_table.txt
-rw-r-xr--+ 1 edwart10 LOAD 2.3G May  6 11:47 STARNET.tpm.gct.bed.per_chrom_STARNET.MP.cov.merged.1.norminal.cis_long_table.txt
-rw-r-xr--+ 1 edwart10 LOAD 638M May  6 11:45 STARNET.tpm.gct.bed.per_chrom_STARNET.MP.cov.merged.20.norminal.cis_long_table.txt
-rw-r-xr--+ 1 edwart10 LOAD 282M May  6 11:45 STARNET.tpm.gct.bed.per_chrom_STARNET.MP.cov.merged.21.norminal.cis_long_table.txt
-rw-r-xr--+ 1 edwart10 LOAD 636M May  6 11:45 STARNET.tpm.gct.bed.per_chrom_STARNET.MP.cov.merged.22.norminal.cis_long_table.txt
-rw-r-xr--+ 1 edwart10 LOAD 1.6G May  6 11:47 STARNET.tpm.gct.bed.per_chrom_STARNET.MP.cov.merged.2.norminal.cis_long_table.txt
-rw-r-xr--+ 1 edwart10 LOAD 1.4G May  6 11:46 STARNET.tpm.gct.bed.per_chrom_STARNET.MP.cov.merged.3.norminal.cis_long_table.txt
-rw-r-xr--+ 1 edwart10 LOAD 935M May  6 11:46 STARNET.tpm.gct.bed.per_chrom_STARNET.MP.cov.merged.4.norminal.cis_long_table.txt
-rw-r-xr--+ 1 edwart10 LOAD 1.1G May  6 11:46 STARNET.tpm.gct.bed.per_chrom_STARNET.MP.cov.merged.5.norminal.cis_long_table.txt
-rw-r-xr--+ 1 edwart10 LOAD 1.7G May  6 11:47 STARNET.tpm.gct.bed.per_chrom_STARNET.MP.cov.merged.6.norminal.cis_long_table.txt
-rw-r-xr--+ 1 edwart10 LOAD 1.2G May  6 11:46 STARNET.tpm.gct.bed.per_chrom_STARNET.MP.cov.merged.7.norminal.cis_long_table.txt
-rw-r-xr--+ 1 edwart10 LOAD 915M May  6 11:46 STARNET.tpm.gct.bed.per_chrom_STARNET.MP.cov.merged.8.norminal.cis_long_table.txt
-rw-r-xr--+ 1 edwart10 LOAD 922M May  6 11:46 STARNET.tpm.gct.bed.per_chrom_STARNET.MP.cov.merged.9.norminal.cis_long_table.txt
```

### Path(s) to Fine-Mapping via SuSiE
TBD

### Path(s) to Fine-Mapping via SuSiE-RSS
TBD
