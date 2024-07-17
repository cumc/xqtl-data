# ROSMAP AC alternative splicing QTL

Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) AC alternative splicing. 

Please refer to [this document](../study_info/ROSMAP.md) for an overview of the ROSMAP project.

## Contact

Frank Grenn

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


## eQTL analysis performed by Gao Wang's Lab and Xiaoling Zhang's lab

### Analyst

Shrishtee Kandoi, Hao Sun

## Analysis Status

TransQTL association: Need to be performed.

### Analysis Description

Brain multi-region RNA-seq data was proccessed with the xQTL-pipeline, for analysis detial please check records here: [eQTL](https://github.com/cumc/brain-xqtl-analysis/tree/main/analysis/Zhang_BU/ROSMAP_DLPFC/eQTL) [eQTL_susie_result_analysis
](https://github.com/cumc/brain-xqtl-analysis/tree/main/analysis/Wang_Columbia/eqtl)

- Genotype used in this analysis on BU cluster: `/restricted/projectnb/casa/skandoi/ROSMAP_DLPFC/genotype_partition/ROSMAP_NIA_WGS.leftnorm.filtered.filtered.plink_files_list.txt`

- Covariates used in this analysis on BU cluster: `/restricted/projectnb/casa/skandoi/ROSMAP_DLPFC/reference_data/ROSMAP_xqtl_covariates_sex_death_pmi_study.tsv`

### Results

- Output summary statistics are uploaded to the FTP server: `/ftp_fgc_xqtl/projects/rna-seq/BU/ROSMAP_DLPFC/eQTL/association_scan`

## sQTL analysis performed by Gao Wang's Lab and Xiaoling Zhang's lab

### Analyst

Shrishtee Kandoi, Xuanhe Chen

### Analysis Description

Brain multi-region RNA-seq data was proccessed with the xQTL-pipeline, for analysis detial please check records here: [sQTL](https://github.com/cumc/brain-xqtl-analysis/tree/main/analysis/Zhang_BU/ROSMAP_DLPFC/sQTL)

- Genotype used in this analysis on BU cluster: `/restricted/projectnb/casa/skandoi/ROSMAP_DLPFC/genotype_partition/ROSMAP_NIA_WGS.leftnorm.filtered.filtered.plink_files_list.txt`

- Covariates used in this analysis on BU cluster: `/restricted/projectnb/casa/skandoi/ROSMAP_DLPFC/reference_data/ROSMAP_xqtl_covariates_sex_death_pmi_study.tsv`

### Results

In this analysis we performed two methods: leafcutter and psichomics.

#### leafcutter

- Output summary statistics are uploaded to the FTP server: `/ftp_fgc_xqtl/projects/rna-seq/BU/ROSMAP_DLPFC/sQTL/association_scan/`

#### psichomics

- data generation using psichomics still in progress

### Path(s) to cis-QTL association testing

**output of TensorQTL.ipynb**

- `/ftp_fgc_xqtl/analysis_result/cis_association/ROSMAP/sQTL/AC`