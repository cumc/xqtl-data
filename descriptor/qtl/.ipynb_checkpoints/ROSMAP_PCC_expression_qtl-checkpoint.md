# ROSMAP PCC Expression QTL

Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) PCC alternative splicing. 

Please refer to [this document](../study_info/ROSMAP.md) for an overview of the ROSMAP project.

## Contact 

Frank Grenn

## Study Overview

**In progress**

- Sample information: `####/####_sample_attributes.csv`.
- Lab protocol: `####/####_lab_protocol.csv`.
- Computational protocol: `####/####_computational_protocol.csv`.
- QTL summary statistics output: `####/####.qtl_results.csv`.
- Fine-mapping results individual level data model: `####/####.susie.csv`.
- Fine-mapping results summary statistics model: `####/####.susie_rss.csv`.
- Colocalization with AD GWAS: `####/####.susie_coloc.csv`.

## Analysis Status

TransQTL association: Need to be performed.

## Dataset Details

### Path(s) to genotype matrix

- Zhang Lab, `/restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/genotype/genotype_partition/ROSMAP_NIA_WGS.leftnorm.filtered.unrelated.filtered.plink_files_list.txt`

```
$ head ROSMAP_NIA_WGS.leftnorm.filtered.unrelated.filtered.plink_files_list.txt
#id     dir
1       /restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/genotype/genotype_partition/ROSMAP_NIA_WGS.leftnorm.filtered.unrelated.filtered.1.bed
2       /restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/genotype/genotype_partition/ROSMAP_NIA_WGS.leftnorm.filtered.unrelated.filtered.2.bed
3       /restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/genotype/genotype_partition/ROSMAP_NIA_WGS.leftnorm.filtered.unrelated.filtered.3.bed
4       /restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/genotype/genotype_partition/ROSMAP_NIA_WGS.leftnorm.filtered.unrelated.filtered.4.bed
5       /restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/genotype/genotype_partition/ROSMAP_NIA_WGS.leftnorm.filtered.unrelated.filtered.5.bed
6       /restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/genotype/genotype_partition/ROSMAP_NIA_WGS.leftnorm.filtered.unrelated.filtered.6.bed
7       /restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/genotype/genotype_partition/ROSMAP_NIA_WGS.leftnorm.filtered.unrelated.filtered.7.bed
8       /restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/genotype/genotype_partition/ROSMAP_NIA_WGS.leftnorm.filtered.unrelated.filtered.8.bed
9       /restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/genotype/genotype_partition/ROSMAP_NIA_WGS.leftnorm.filtered.unrelated.filtered.9.bed

$ ls -lh *.{bim,bed,fam} | head
-rw-r--r-- 1 fgrennjr casa  91M Mar 17 14:03 ROSMAP_NIA_WGS.leftnorm.filtered.unrelated.filtered.1.bed
-rw-r--r-- 1 fgrennjr casa  33M Mar 17 14:03 ROSMAP_NIA_WGS.leftnorm.filtered.unrelated.filtered.1.bim
-rw-r--r-- 1 fgrennjr casa 8.7K Mar 17 14:03 ROSMAP_NIA_WGS.leftnorm.filtered.unrelated.filtered.1.fam
-rw-r--r-- 1 fgrennjr casa  59M Mar 17 14:03 ROSMAP_NIA_WGS.leftnorm.filtered.unrelated.filtered.10.bed
-rw-r--r-- 1 fgrennjr casa  23M Mar 17 14:03 ROSMAP_NIA_WGS.leftnorm.filtered.unrelated.filtered.10.bim
-rw-r--r-- 1 fgrennjr casa 8.7K Mar 17 14:03 ROSMAP_NIA_WGS.leftnorm.filtered.unrelated.filtered.10.fam
-rw-r--r-- 1 fgrennjr casa  57M Mar 17 14:03 ROSMAP_NIA_WGS.leftnorm.filtered.unrelated.filtered.11.bed
-rw-r--r-- 1 fgrennjr casa  22M Mar 17 14:03 ROSMAP_NIA_WGS.leftnorm.filtered.unrelated.filtered.11.bim
-rw-r--r-- 1 fgrennjr casa 8.7K Mar 17 14:03 ROSMAP_NIA_WGS.leftnorm.filtered.unrelated.filtered.11.fam
-rw-r--r-- 1 fgrennjr casa  56M Mar 17 14:03 ROSMAP_NIA_WGS.leftnorm.filtered.unrelated.filtered.12.bed
```

### Path(s) to omics-data matrix

- Zhang Lab, `/restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/PDP_rnaseqc/PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.per_chrom.recipe`

```
$ls -lh /restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/rnaseqc_call/normalize/PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.gz
-rw-r--r-- 1 fgrennjr casa 45M Mar 16 19:25 /restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/rnaseqc_call/normalize/PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.gz
```

### Path(s) to covariate data matrix

- Zhang Lab, `/restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/reference_data/ROSMAP_xqtl_covariates_sex_death_pmi_study.tsv`

```
$ head PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.per_chrom.recipe
#id     #dir
16      /restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/PDP_rnaseqc/PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.chr16.bed.gz
4       /restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/PDP_rnaseqc/PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.chr4.bed.gz
9       /restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/PDP_rnaseqc/PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.chr9.bed.gz
3       /restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/PDP_rnaseqc/PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.chr3.bed.gz
6       /restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/PDP_rnaseqc/PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.chr6.bed.gz
21      /restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/PDP_rnaseqc/PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.chr21.bed.gz
12      /restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/PDP_rnaseqc/PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.chr12.bed.gz
17      /restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/PDP_rnaseqc/PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.chr17.bed.gz
18      /restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/PDP_rnaseqc/PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.chr18.bed.gz

$ ls -lh *bed.gz | head
-rw-r--r-- 1 fgrennjr casa 4.3M Mar 16 19:33 PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.chr1.bed.gz
-rw-r--r-- 1 fgrennjr casa 1.8M Mar 16 19:33 PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.chr10.bed.gz
-rw-r--r-- 1 fgrennjr casa 2.4M Mar 16 19:33 PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.chr11.bed.gz
-rw-r--r-- 1 fgrennjr casa 2.4M Mar 16 19:33 PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.chr12.bed.gz
-rw-r--r-- 1 fgrennjr casa 963K Mar 16 19:33 PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.chr13.bed.gz
-rw-r--r-- 1 fgrennjr casa 1.5M Mar 16 19:33 PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.chr14.bed.gz
-rw-r--r-- 1 fgrennjr casa 1.7M Mar 16 19:33 PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.chr15.bed.gz
-rw-r--r-- 1 fgrennjr casa 2.2M Mar 16 19:33 PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.chr16.bed.gz
-rw-r--r-- 1 fgrennjr casa 2.7M Mar 16 19:33 PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.chr17.bed.gz
-rw-r--r-- 1 fgrennjr casa 814K Mar 16 19:33 PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.chr18.bed.gz
```

### Path(s) to QTL results

- Zhang Lab, `/restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/TensorQTL/eQTL`

```
$ ls -lh | head
total 35G
-rw-r--r-- 1 fgrennjr casa  529M Mar 17 16:02 PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.per_chrom_pcc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.1.cis_qtl_pairs.1.parquet
-rw-r--r-- 1 fgrennjr casa   285 Mar 17 17:06 PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.per_chrom_pcc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.1.cis_qtl_pairs.1.parquet.stderr
-rw-r--r-- 1 fgrennjr casa  173K Mar 17 17:06 PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.per_chrom_pcc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.1.cis_qtl_pairs.1.parquet.stdout
-rw-r--r-- 1 fgrennjr casa  555K Mar 17 17:06 PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.per_chrom_pcc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.1.emprical.cis_sumstats.txt
-rw-r--r-- 1 fgrennjr casa  2.6G Mar 17 16:04 PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.per_chrom_pcc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.1.norminal.cis_long_table.txt
-rw-r--r-- 1 fgrennjr casa  253M Mar 17 16:00 PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.per_chrom_pcc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.10.cis_qtl_pairs.10.parquet
-rw-r--r-- 1 fgrennjr casa   285 Mar 17 16:31 PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.per_chrom_pcc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.10.cis_qtl_pairs.10.parquet.stderr
-rw-r--r-- 1 fgrennjr casa   72K Mar 17 16:31 PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.per_chrom_pcc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.10.cis_qtl_pairs.10.parquet.stdout
-rw-r--r-- 1 fgrennjr casa  234K Mar 17 16:31 PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.per_chrom_pcc_batch_all.rnaseqc.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.10.emprical.cis_sumstats.txt
```

### Path(s) to fine-mapping with SuSiE model

### Path(s) to fine-mapping with SuSiE RSS model

### Path(s) to colocalization with SuSiE-coloc

## Links to QTL analysis notebooks

Analysis notebook generation in progress and will be uploaded to [https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Zhang_BU/PCC_AC](https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Zhang_BU/PCC_AC). Steps will be similar to what is found in [https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Zhang_BU/ROSMAP_DLPFC](https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Zhang_BU/ROSMAP_DLPFC).
