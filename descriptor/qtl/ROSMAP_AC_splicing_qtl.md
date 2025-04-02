# ROSMAP AC alternative splicing QTL

Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) AC alternative splicing. 

Please refer to [this document](../study_info/ROSMAP.md) for an overview of the ROSMAP project.

## Contact

Ru Feng

## Data Descriptions

**Verifying current avaliable location for the dataset now**

Samples were extracted using Qiagen's miRNeasy mini kit (cat. no. 217004) and the RNase free DNase Set (cat. no. 79254), and quantified by Nanodrop and quality was evaluated by Agilent Bioanalyzer.

| Brain      | Description |
| -----------| ----------- |
| Batch 1    | 638         |
| Batch 2    | 252 (117 for PolyA selection & 135 for rRNA depletion)        |
| Batch 3    | 251         |
| Total      | 1141        |

**Notes regarding sample naming:** Sequencing samples that were sequenced more than once include the sequencing batch number as the last 2 digits of the id. For example, sample 123_456789_02 is sample "123_456789", from batch 2. The sample IDs are otherwise randomly-assigned identifiers. Some samples were re-sequenced due to poor quality or low output, they may have "redo" in the sample identifier.


## Links to QTL analysis notebooks for LeafCutter2

See notebooks in: 

- https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/ROSMAP/sQTL/AC

The notebooks in this folder contain the commands and data wrangling codes for analysis of the eQTL and sQTL data in ROSMAP. (data wrangling exist because not all data are processed using the xqtl-pipeline from the beginning and need to be reformatted to fit one intermediate step of the pipeline). Since the sQTL phenotype pre-processing used eQTL STAR alignment output, some of the early stage code are shared.

### Association data preprocessing

- [LeafCutter2_QC](https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/ROSMAP/sQTL/AC/1.2_ac_leafcutter2_results_QC.ipynb) shows the commands used for quality control of the LeafCutter2 results.

- [genotype_preprocessing.ipynb](https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/ROSMAP/haQTL/genotype_preprocessing.ipynb) shows the commands used for genotype processing and preparation steps.All QTLs in one cohort have the same genotype_preprocessing procedure.

- [phenotype_preprocessing.ipynb](https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/ROSMAP/sQTL/AC/1_ac_phenotype_preprocessing.ipynb) shows the commands used for the phenotype data processing and preparation steps.

- [covariate_preprocessing.ipynb](https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/ROSMAP/sQTL/AC/3_ac_covariate_preprocessing.ipynb) shows the commands used for the covariate data processing and preparation steps.

  
### Association scan using TensorQTL and summary statistics standardization

- [TensorQTL.ipynb](https://github.com/cumc/xqtl-protocol/blob/main/code/association_scan/TensorQTL/TensorQTL.ipynb) provides the pipeline to generate TensorQTL cis association results for all QTLs. 
- [ROSMAP_sQTL_LeafCutter2_commands](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/cis_association/ROSMAP_sQTL_LeafCutter2/command_generator.ipynb) provides information about the input files for AC/DLPFC/PCC TensorQTL cis association in the base_params variable in [generate_command_1].

### Analysis Description

Brain multi-region RNA-seq data using LeafCutter2 was proccessed with the xQTL-pipeline, for analysis detial please check records here: [sQTL_LeafCutter2](https://github.com/gaow/leafcutter2-paper/tree/main/analysis/ROSMAP)

- Genotype used in this analysis on AWS: `s3://statfungen/ftp_fgc_xqtl/ROSMAP/genotype/analysis_ready/geno_by_chrom/`
- Phenotype used in this analysis on AWS: `s3://statfungen/ftp_fgc_xqtl/sQTL/ROSMAP/AC/leafcutter2/analysis_ready/phenotype_preprocessing/`
- Covariates used in this analysis on AWS: `s3://statfungen/ftp_fgc_xqtl/sQTL/ROSMAP/AC/leafcutter2/analysis_ready/covariate_preprocessing/ROSMAP_AC_perind.counts.noise_by_intron.QCed_minc1_mins10.gz_raw_data.qqnorm.imputed.bed.formated.rosmap_cov.ROSMAP_NIA_WGS.leftnorm.bcftools_qc.plink_qc.plink_qc.prune.pca.Marchenko_PC.gz`

### Results

In this analysis we performed two methods: leafcutter2 and psichomics.

#### leafcutter2

- Output summary statistics are uploaded to the FTP server: `/ftp_fgc_xqtl/projects/rna-seq/BU/ROSMAP_DLPFC/sQTL/association_scan/`
- Original files: `s3://statfungen/ftp_fgc_xqtl/analysis_result/cis_association/ROSMAP/sQTL/AC/leafcutter2/`

#### psichomics

- data generation using psichomics still in progress



