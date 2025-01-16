# ROSMAP PCC alternative splicing QTL

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

- Zhang Lab, `/restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/PDP_leafcutter/batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.per_chrom.recipe`

```
$ ls -lh batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.txt
-rw-r--r-- 1 fgrennjr casa 3.1G Mar  6 14:06 batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.txt
```

### Path(s) to covariate data matrix

- Zhang Lab, `/restricted/projectnb/casa/skandoi/ROSMAP_DLPFC/reference_data/ROSMAP_xqtl_covariates_sex_death_pmi_study.tsv`
```
$ head batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.per_chrom.recipe
#id     #dir
5       /restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/PDP_leafcutter/batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.chr5.bed.gz
18      /restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/PDP_leafcutter/batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.chr18.bed.gz
7       /restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/PDP_leafcutter/batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.chr7.bed.gz
10      /restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/PDP_leafcutter/batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.chr10.bed.gz
8       /restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/PDP_leafcutter/batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.chr8.bed.gz
Y       /restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/PDP_leafcutter/batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.chrY.bed.gz
11      /restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/PDP_leafcutter/batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.chr11.bed.gz
13      /restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/PDP_leafcutter/batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.chr13.bed.gz
9       /restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/PDP_leafcutter/batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.chr9.bed.gz

$ ls -lh *bed.gz | head
-rw-r--r-- 1 fgrennjr casa 125M Mar  8 16:08 batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.chr1.bed.gz
-rw-r--r-- 1 fgrennjr casa  56M Mar  8 16:07 batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.chr10.bed.gz
-rw-r--r-- 1 fgrennjr casa  67M Mar  8 16:07 batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.chr11.bed.gz
-rw-r--r-- 1 fgrennjr casa  69M Mar  8 16:07 batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.chr12.bed.gz
-rw-r--r-- 1 fgrennjr casa  26M Mar  8 16:07 batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.chr13.bed.gz
-rw-r--r-- 1 fgrennjr casa  43M Mar  8 16:07 batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.chr14.bed.gz
-rw-r--r-- 1 fgrennjr casa  50M Mar  8 16:07 batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.chr15.bed.gz
-rw-r--r-- 1 fgrennjr casa  58M Mar  8 16:07 batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.chr16.bed.gz
-rw-r--r-- 1 fgrennjr casa  74M Mar  8 16:07 batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.chr17.bed.gz
-rw-r--r-- 1 fgrennjr casa  22M Mar  8 16:07 batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.chr18.bed.gz
```

### Path(s) to QTL results

- Zhang Lab, `/restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/TensorQTL/sQTL`
```
$ ls -lh | head
total 27G
-rw-r--r-- 1 fgrennjr casa 374M Mar 24 11:42 batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.per_chrom_leafcutter.pcc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.1.cis_qtl_pairs.1.parquet
-rw-r--r-- 1 fgrennjr casa  285 Mar 24 22:12 batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.per_chrom_leafcutter.pcc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.1.cis_qtl_pairs.1.parquet.stderr
-rw-r--r-- 1 fgrennjr casa 138K Mar 24 22:12 batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.per_chrom_leafcutter.pcc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.1.cis_qtl_pairs.1.parquet.stdout
-rw-r--r-- 1 fgrennjr casa 433K Mar 24 22:12 batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.per_chrom_leafcutter.pcc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.1.emprical.cis_sumstats.txt
-rw-r--r-- 1 fgrennjr casa 2.2G Mar 24 11:44 batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.per_chrom_leafcutter.pcc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.1.norminal.cis_long_table.txt
-rw-r--r-- 1 fgrennjr casa 180M Mar 24 11:28 batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.per_chrom_leafcutter.pcc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.10.cis_qtl_pairs.10.parquet
-rw-r--r-- 1 fgrennjr casa  285 Mar 24 16:48 batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.per_chrom_leafcutter.pcc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.10.cis_qtl_pairs.10.parquet.stderr
-rw-r--r-- 1 fgrennjr casa  58K Mar 24 16:48 batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.per_chrom_leafcutter.pcc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.10.cis_qtl_pairs.10.parquet.stdout
-rw-r--r-- 1 fgrennjr casa 187K Mar 24 16:48 batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.per_chrom_leafcutter.pcc_batch_all.ROSMAP_covariates.ROSMAP_NIA_WGS.pca.PEER.txt.10.emprical.cis_sumstats.txt
```


## Links to QTL analysis notebooks

### Data Preprocessing
- [sQTL_LeafCutter2](https://github.com/gaow/leafcutter2-paper/tree/main/analysis/ROSMAP) provides data preprocessing procedures for genotype/phenotype and covariate data/

### Path(s) to cis-QTL association testing

- [TensorQTL.ipynb](https://github.com/cumc/xqtl-protocol/blob/main/code/association_scan/TensorQTL/TensorQTL.ipynb) provides the pipeline to generate TensorQTL cis association results for all QTLs. 
- [ROSMAP_sQTL_LeafCutter2](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/cis_association/ROSMAP_sQTL_LeafCutter2/command_generator.ipynb)provides information about the input files for AC/DLPFC/PCC TensorQTL cis association in the base_params variable in [generate_command_1].

**output of TensorQTL.ipynb**

- `s3://statfungen/ftp_fgc_xqtl/analysis_result/cis_association/ROSMAP/sQTL/PCC/leafcutter2/`
  
### Path(s) to fine-mapping with SuSiE model

### Path(s) to fine-mapping with SuSiE RSS model

### Path(s) to colocalization with SuSiE-coloc