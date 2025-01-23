# ROSMAP snRNA-seq pseudo-bulk gene expression QTL

Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) snRNA-seq from different cells in Dorsolateral Prefrontal Cortex (DLPFC). 

Please refer to [this document](../study_info/ROSMAP.md) for an overview of the ROSMAP project.

## Contact

Hao Sun (eQTL), Masashi Fujita (eQTL), Haochen Sun (fine-mapping), Jiajun Tao (replication)

## Study Overview

- Sample information: `ROSMAP/ROSMAP_Pseudo_Bulk_sample_attributes.csv`.
- Lab protocol: `ROSMAP/ROSMAP_Pseudo_Bulk_lab_protocol.csv`.
- Computational protocol: `ROSMAP/ROSMAP_Pseudo_Bulk_computational_protocol.csv`.
- QTL summary statistics output: `####/####.qtl_results.csv`.
- Fine-mapping results individual level data model: `####/####.susie.csv`.
- Fine-mapping results summary statistics model: `####/####.susie_rss.csv`.

## Analysis Status

TransQTL association: Finished.

## Dataset Description

### Path(s) to genotype matrix

#### Using `MatrixQTL` pipeline (by Masashi)

1. genotype is an all-chromosome, all-samples vcf collection
2. The original `gz` vcf is `gzipped` but not `bgzipped`, thus cannot `tabix -p`
3. The vcf is not imputed.
- Dosage file. The number of ALT allele were counted per donor.
`/mnt/mfs/ctcn/team/masashi/snuc-eqtl/genotype/get-dosage.ALL.dosage`
- SNP position file in GRCh38
`/mnt/mfs/ctcn/team/masashi/snuc-eqtl/genotype/get-dosage.ALL.snppos`
- VCF file used to generate above files. This is a subset of ROSMAP WGS VCF.
`/mnt/mfs/ctcn/team/masashi/snuc-eqtl/genotype/get-dosage.ALL.vcf.gz`
- The original VCF files of ROS/MAP WGS is here (N = 1,196; GRCh37):
`/mnt/mfs/ctcn/datasets/rosmap/wgs/ampad/variants/snvCombined/`
- A summary of quality control is here:
`/mnt/mfs/ctcn/datasets/rosmap/wgs/ampad/qualityControl/sampleSheetQc.csv`
- Liftover of the above VCFs from GRCh37 to GRCh38.
`/mnt/mfs/hgrcgrid/shared/MenonLab/snRNAseq/rosmap_mastervcf/GRCh38_liftedover_sorted_all.vcf.gz`
- Sorted positions of SNPs, added rsID in dbSNP154, and renamed chromosomes (e.g. 1 to chr1).
`/mnt/mfs/ctcn/resources/snRNAseq/rosmap_mastervcf/GRCh38_liftedover_re-sorted_dbSNP154_chr-renamed_all.bcf`
- 424 donors extracted for snRNAseq and applied filtering of MAF, HWE, etc.
`/mnt/mfs/ctcn/team/masashi/snuc-eqtl/genotype/get-dosage.ALL.vcf.gz`

### Path(s) to omics-data matrix

### Path(s) to covariate data matrix

#### Using `MatrixQTL` pipeline (by Masashi)

Here, I use astrocytes as an example. But all other cell types have the same folder structure.

Covariates of eQTL analysis are sex, age, PMI, study, total genes detected, top 3 genotype PCs, and up to 30 expression PCs. 

- De Jager Lab: `/mnt/mfs/ctcn/team/masashi/snuc-eqtl/v20211109.celltypes/Ast/covariates-20211118.tsv`.

#### Using `TenorQTL` pipeline (by Hao)

### Path(s) to QTL results

#### Using `MatrixQTL` pipeline (by Masashi)

- De Jager Lab: `/mnt/mfs/ctcn/team/masashi/snuc-eqtl`

Take astrocytes as an example,

- De Jager Lab: `/mnt/mfs/ctcn/team/masashi/snuc-eqtl/v20211109.celltypes/Ast/matrix-eqtl/covariates-20211118/matrix-eqtl.rds`. 

```r
df <- readRDS("matrix-eqtl.rds")$cis$eqtl
``` 

#### Using `TenorQTL` pipeline (by Hao)

- Wang Lab: `/ftp_fgc_xqtl/projects/single-cell-rna-seq/pseudo_bulk/eight_celltypes_sumstat`

- Wang Lab(CU Server):  `/mnt/vast/hpc/csg/wanggroup/fungen-xqtl-analysis/analysis/Wang_Columbia/ROSMAP/pseudo_bulk_eqtl`


### Association scan using TensorQTL and summary statistics standardization

- [TensorQTL.ipynb](https://github.com/cumc/xqtl-protocol/blob/main/code/association_scan/TensorQTL/TensorQTL.ipynb) provides the pipeline to generate TensorQTL cis association results for all QTLs. 
- [ROSMAP_DeJager_snuc_eQTL](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/cis_association/ROSMAP_DeJager_snuc_eQTL/command_generator.ipynb) provides information about the input files for TensorQTL cis association in the base_params variable in [generate_command_1].
- [ROSMAP_Kellis_eQTL](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/cis_association/ROSMAP_Kellis_eQTL/command_generator.ipynb) provides information about the input files for TensorQTL cis association in the base_params variable in [generate_command_1].
- [ROSMAP_mega_eQTL](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/cis_association/ROSMAP_mega_eQTL/command_generator.ipynb) provides information about the input files for TensorQTL cis association in the base_params variable in [generate_command_1].


### Path(s) to cis-QTL association testing

**output of TensorQTL.ipynb**

- `s3://statfungen/ftp_fgc_xqtl/analysis_result/cis_association/ROSMAP/eQTL/snuc_DeJager/`
- `s3://statfungen/ftp_fgc_xqtl/analysis_result/cis_association/ROSMAP/eQTL/snuc_Kellis/`
- `s3://statfungen/ftp_fgc_xqtl/analysis_result/cis_association/ROSMAP/eQTL/snuc_mega/`
  
### Path(s) to fine-mapping with SuSiE model

### Path(s) to fine-mapping with SuSiE RSS model

## Links to QTL analysis notebooks 
pseudo_bulk_eQTL_DeJager:
[Preprocess_bundle](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/pseudo_bulk_eQTL_DeJager/Preprocess_bundle.ipynb) provides commands to preprocess genotype, phenotype and covariate data all at once.
[Phenotype_preprocessing](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/pseudo_bulk_eQTL_DeJager/ALL/phenotype_preprocessing.ipynb) shows the commands used for the phenotype data processing and preparation steps for all cell types. Cell-specific phenotype preprocessing are listed [here in different folders](https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/ROSMAP/pseudo_bulk_eQTL_DeJager).


pseudo_bulk_eQTL_Kellis:
[Preprocess_bundle](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/pseudo_bulk_eQTL_Kellis/Preprocess_bundle.ipynb) provides commands to preprocess genotype, phenotype and covariate data all at once.
[Genotype_pca](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/pseudo_bulk_eQTL_Kellis/genotype_pca.ipynb) provides steps for PCA analysis for genotype data.
[Phenotype_preprocessing](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/pseudo_bulk_eQTL_Kellis/phenotype_preprocessing.ipynb) shows the commands used for the phenotype data processing and preparation steps.
[Covariates_preprocessing](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/pseudo_bulk_eQTL_Kellis/covariates_preprocessing.ipynb) shows the commands used for the covariate data processing and preparation steps.


pseudo_bulk_eQTL_mega:
[Genotype_pca](https://github.com/rl3328/xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/pseudo_bulk_eQTL_mega/genotype_pca.ipynb) provides steps for PCA analysis for genotype data.
[Phenotype_preprocessing](https://github.com/rl3328/xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/pseudo_bulk_eQTL_mega/phenotype_preprocessing.ipynb) shows the commands used for the phenotype data processing and preparation steps.
[Covariates_preprocessing](https://github.com/rl3328/xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/pseudo_bulk_eQTL_mega/covariates_preprocessing.ipynb) shows the commands used for the covariate data processing and preparation steps.
