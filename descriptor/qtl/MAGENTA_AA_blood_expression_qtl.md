# MAGENTA African American Blood Gene Expression QTL

Multi-Ancestry Genomics, Epigenomics, and Transcriptomics of Alzheimer’s (MAGENTA) Project: Participants include 465 individuals (AA – 113 with AD, 118 cognitively intact controls; NHW – 116 with AD, 118 controls) ascertained by the John P. Hussman Institute for Human Genomics (HIHG) at the University of Miami Miller School of Medicine (Miami, FL), North Carolina A&T State University (Greensboro, NC), and Case Western Reserve University (Cleveland, OH).  Participants were ascertained as part of the ADSP Follow-up Study and included both cases (>65 years of age of onset) and controls (>65 years of age at age of exam).  All participants were adjudicated by a clinical panel with expertise in AD related disorders and classified as AD according to standard criteria developed by the National Institute of Aging and the Alzheimer’s Association. 

## Contact
Makaela Mews (analyst; mxm1368@case.edu);  Dr. William S. Bush (wsb36@case.edu);  Dr. Anthony J. Griswold (Griswold, Anthony J agriswold@miami.edu)

## Study Overview

- Sample information: `MAGENTA/MAGENTA_AA_eqtl_sample_attributes.csv`.
- Lab protocol: `MAGENTA/MAGENTA_AA_eqtl_lab_protocol.csv`.
- Computational protocol: `MAGENTA/MAGENTA_AA_eqtl_computational_protocol.csv`.
- QTL summary statistics output: `MAGENTA/MAGENTA_AA_expression.qtl_results.csv`.

- Fine-mapping results individual level data model: `####/####.susie.csv`.
- Fine-mapping results summary statistics model: `####/####.susie_rss.csv`.
- Colocalization with AD GWAS: `####/####.susie_coloc.csv`.

where "Sample information" is a CSV file containing sample attributes / complete set of covariates for the exact samples used in the QTL study; 
"Lab protocol" is a CSV file containing the experimental protocol information to process the samples;
"Computational protocol" is a CSV file containing the computational protocol information to process the samples;
"QTL summary statistics output" is the list of QTL summary statistics results; 
"Fine-mapping results individual level data model" is the list of fine-mapped QTL using individual level phenotype and genotype data input for SuSiE model. "Fine-mapping results summary statistics model" uses QTL summary statistics for SuSiE RSS model.
"Colocalization with AD GWAS" is the list of colocalization analysis with different AD GWAS publications and data-sets using coloc model on SuSiE results.

## Analysis Status
TransQTL association: Need to be updated with new covariate files.

## Dataset Details
### Path(s) to genotype matrix
Here please document the exact genotype matrix used for QTL calling. 
- Path(s) to the data on your local cluster where you analyzed the data. 
- TensorQTL - cis:  Bush Lab, server:  rider.case.edu `/mnt/pan/Data14/metabrain_lasso/rna_seq_norm/aa_233/geno/by_chr/aa_chr1_22.no_rel.filtered.plink_files_list.txt`
- TensorQTL - trans:  Bush Lab, server:  rider.case.edu `/mnt/pan/Data14/metabrain_lasso/rna_seq_norm/aa_233/geno/geno_final/aa_chr1_22.no_rel.filtered.bed`
- NIAGADS FTP, `/ftp_fgc_xqtl/projects/...`


A summary of the genotype data including size used for TensorQTL - cis:


```
$ ls -lh *{bed,bim,fam,txt}
-rw-r--r-- 1 mxm1368 wsb36  31M Mar 23 14:41 aa_chr1_22.no_rel.filtered.10.bed
-rw-r--r-- 1 mxm1368 wsb36  21M Mar 23 14:41 aa_chr1_22.no_rel.filtered.10.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:41 aa_chr1_22.no_rel.filtered.10.fam
-rw-r--r-- 1 mxm1368 wsb36  30M Mar 23 14:41 aa_chr1_22.no_rel.filtered.11.bed
-rw-r--r-- 1 mxm1368 wsb36  20M Mar 23 14:41 aa_chr1_22.no_rel.filtered.11.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:41 aa_chr1_22.no_rel.filtered.11.fam
-rw-r--r-- 1 mxm1368 wsb36  30M Mar 23 14:41 aa_chr1_22.no_rel.filtered.12.bed
-rw-r--r-- 1 mxm1368 wsb36  20M Mar 23 14:41 aa_chr1_22.no_rel.filtered.12.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:41 aa_chr1_22.no_rel.filtered.12.fam
-rw-r--r-- 1 mxm1368 wsb36  24M Mar 23 14:41 aa_chr1_22.no_rel.filtered.13.bed
-rw-r--r-- 1 mxm1368 wsb36  16M Mar 23 14:41 aa_chr1_22.no_rel.filtered.13.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:41 aa_chr1_22.no_rel.filtered.13.fam
-rw-r--r-- 1 mxm1368 wsb36  21M Mar 23 14:41 aa_chr1_22.no_rel.filtered.14.bed
-rw-r--r-- 1 mxm1368 wsb36  14M Mar 23 14:41 aa_chr1_22.no_rel.filtered.14.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:41 aa_chr1_22.no_rel.filtered.14.fam
-rw-r--r-- 1 mxm1368 wsb36  18M Mar 23 14:41 aa_chr1_22.no_rel.filtered.15.bed
-rw-r--r-- 1 mxm1368 wsb36  12M Mar 23 14:41 aa_chr1_22.no_rel.filtered.15.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:41 aa_chr1_22.no_rel.filtered.15.fam
-rw-r--r-- 1 mxm1368 wsb36  20M Mar 23 14:41 aa_chr1_22.no_rel.filtered.16.bed
-rw-r--r-- 1 mxm1368 wsb36  13M Mar 23 14:41 aa_chr1_22.no_rel.filtered.16.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:41 aa_chr1_22.no_rel.filtered.16.fam
-rw-r--r-- 1 mxm1368 wsb36  17M Mar 23 14:41 aa_chr1_22.no_rel.filtered.17.bed
-rw-r--r-- 1 mxm1368 wsb36  11M Mar 23 14:41 aa_chr1_22.no_rel.filtered.17.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:41 aa_chr1_22.no_rel.filtered.17.fam
-rw-r--r-- 1 mxm1368 wsb36  19M Mar 23 14:41 aa_chr1_22.no_rel.filtered.18.bed
-rw-r--r-- 1 mxm1368 wsb36  12M Mar 23 14:41 aa_chr1_22.no_rel.filtered.18.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:41 aa_chr1_22.no_rel.filtered.18.fam
-rw-r--r-- 1 mxm1368 wsb36  13M Mar 23 14:41 aa_chr1_22.no_rel.filtered.19.bed
-rw-r--r-- 1 mxm1368 wsb36 7.9M Mar 23 14:41 aa_chr1_22.no_rel.filtered.19.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:41 aa_chr1_22.no_rel.filtered.19.fam
-rw-r--r-- 1 mxm1368 wsb36  49M Mar 23 14:41 aa_chr1_22.no_rel.filtered.1.bed
-rw-r--r-- 1 mxm1368 wsb36  31M Mar 23 14:41 aa_chr1_22.no_rel.filtered.1.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:41 aa_chr1_22.no_rel.filtered.1.fam
-rw-r--r-- 1 mxm1368 wsb36  15M Mar 23 14:41 aa_chr1_22.no_rel.filtered.20.bed
-rw-r--r-- 1 mxm1368 wsb36 9.1M Mar 23 14:41 aa_chr1_22.no_rel.filtered.20.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:41 aa_chr1_22.no_rel.filtered.20.fam
-rw-r--r-- 1 mxm1368 wsb36 8.9M Mar 23 14:41 aa_chr1_22.no_rel.filtered.21.bed
-rw-r--r-- 1 mxm1368 wsb36 5.8M Mar 23 14:41 aa_chr1_22.no_rel.filtered.21.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:41 aa_chr1_22.no_rel.filtered.21.fam
-rw-r--r-- 1 mxm1368 wsb36 7.9M Mar 23 14:41 aa_chr1_22.no_rel.filtered.22.bed
-rw-r--r-- 1 mxm1368 wsb36 5.2M Mar 23 14:41 aa_chr1_22.no_rel.filtered.22.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:41 aa_chr1_22.no_rel.filtered.22.fam
-rw-r--r-- 1 mxm1368 wsb36  53M Mar 23 14:41 aa_chr1_22.no_rel.filtered.2.bed
-rw-r--r-- 1 mxm1368 wsb36  34M Mar 23 14:41 aa_chr1_22.no_rel.filtered.2.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:41 aa_chr1_22.no_rel.filtered.2.fam
-rw-r--r-- 1 mxm1368 wsb36  45M Mar 23 14:41 aa_chr1_22.no_rel.filtered.3.bed
-rw-r--r-- 1 mxm1368 wsb36  29M Mar 23 14:41 aa_chr1_22.no_rel.filtered.3.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:41 aa_chr1_22.no_rel.filtered.3.fam
-rw-r--r-- 1 mxm1368 wsb36  45M Mar 23 14:41 aa_chr1_22.no_rel.filtered.4.bed
-rw-r--r-- 1 mxm1368 wsb36  28M Mar 23 14:41 aa_chr1_22.no_rel.filtered.4.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:41 aa_chr1_22.no_rel.filtered.4.fam
-rw-r--r-- 1 mxm1368 wsb36  40M Mar 23 14:41 aa_chr1_22.no_rel.filtered.5.bed
-rw-r--r-- 1 mxm1368 wsb36  25M Mar 23 14:41 aa_chr1_22.no_rel.filtered.5.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:41 aa_chr1_22.no_rel.filtered.5.fam
-rw-r--r-- 1 mxm1368 wsb36  41M Mar 23 14:41 aa_chr1_22.no_rel.filtered.6.bed
-rw-r--r-- 1 mxm1368 wsb36  26M Mar 23 14:41 aa_chr1_22.no_rel.filtered.6.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:41 aa_chr1_22.no_rel.filtered.6.fam
-rw-r--r-- 1 mxm1368 wsb36  36M Mar 23 14:41 aa_chr1_22.no_rel.filtered.7.bed
-rw-r--r-- 1 mxm1368 wsb36  22M Mar 23 14:41 aa_chr1_22.no_rel.filtered.7.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:41 aa_chr1_22.no_rel.filtered.7.fam
-rw-r--r-- 1 mxm1368 wsb36  36M Mar 23 14:41 aa_chr1_22.no_rel.filtered.8.bed
-rw-r--r-- 1 mxm1368 wsb36  23M Mar 23 14:41 aa_chr1_22.no_rel.filtered.8.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:41 aa_chr1_22.no_rel.filtered.8.fam
-rw-r--r-- 1 mxm1368 wsb36  28M Mar 23 14:41 aa_chr1_22.no_rel.filtered.9.bed
-rw-r--r-- 1 mxm1368 wsb36  18M Mar 23 14:41 aa_chr1_22.no_rel.filtered.9.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:41 aa_chr1_22.no_rel.filtered.9.fam
-rw-r--r-- 1 mxm1368 wsb36 2.2K Mar 23 14:41 aa_chr1_22.no_rel.filtered.plink_files_list.txt

```

A summary of the genotype data including size used for TensorQTL - trans:

```
$ ls -lh aa_chr1_22.no_rel.filtered.{bim,bed,fam}
-rw-r--r-- 1 mxm1368 wsb36 619M Mar 23 14:41 aa_chr1_22.no_rel.filtered.bed
-rw-r--r-- 1 mxm1368 wsb36 394M Mar 23 14:41 aa_chr1_22.no_rel.filtered.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:41 aa_chr1_22.no_rel.filtered.fam

```

### Path(s) to omics-data matrix
Here please document the exact omics-data matrix used for QTL calling.
- Path(s) to the data on your local cluster where you analyzed the data. 
- TensorQTL - cis:  Bush Lab, server: rider.case.edu `/mnt/pan/Data14/metabrain_lasso/rna_seq_norm/aa_233/mol_phe/tmm_per_chr/`
- TensorQTL - trans:  Bush Lab, server: rider.case.edu `/mnt/pan/Data14/metabrain_lasso/rna_seq_norm/aa_233/mol_phe`
- NIAGADS FTP, `/ftp_fgc_xqtl/projects/...`
 
A summary of the phenotype data including size used for TensorQTL - cis:


```
$ pwd
/mnt/pan/Data14/metabrain_lasso/rna_seq_norm/aa_233/mol_phe/tmm_per_chr

$ ls -lh *.bed.gz
-rw-r--r-- 1 mxm1368 wsb36 469K Feb 27 17:55 aa_233_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr10.bed.gz
-rw-r--r-- 1 mxm1368 wsb36 689K Feb 27 17:55 aa_233_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr11.bed.gz
-rw-r--r-- 1 mxm1368 wsb36 689K Feb 27 17:55 aa_233_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr12.bed.gz
-rw-r--r-- 1 mxm1368 wsb36 216K Feb 27 17:55 aa_233_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr13.bed.gz
-rw-r--r-- 1 mxm1368 wsb36 494K Feb 27 17:55 aa_233_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr14.bed.gz
-rw-r--r-- 1 mxm1368 wsb36 416K Feb 27 17:55 aa_233_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr15.bed.gz
-rw-r--r-- 1 mxm1368 wsb36 665K Feb 27 17:55 aa_233_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr16.bed.gz
-rw-r--r-- 1 mxm1368 wsb36 828K Feb 27 17:55 aa_233_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr17.bed.gz
-rw-r--r-- 1 mxm1368 wsb36 186K Feb 27 17:55 aa_233_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr18.bed.gz
-rw-r--r-- 1 mxm1368 wsb36 969K Feb 27 17:55 aa_233_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr19.bed.gz
-rw-r--r-- 1 mxm1368 wsb36 1.3M Feb 27 17:55 aa_233_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr1.bed.gz
-rw-r--r-- 1 mxm1368 wsb36 334K Feb 27 17:55 aa_233_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr20.bed.gz
-rw-r--r-- 1 mxm1368 wsb36 138K Feb 27 17:55 aa_233_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr21.bed.gz
-rw-r--r-- 1 mxm1368 wsb36 373K Feb 27 17:55 aa_233_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr22.bed.gz
-rw-r--r-- 1 mxm1368 wsb36 842K Feb 27 17:55 aa_233_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr2.bed.gz
-rw-r--r-- 1 mxm1368 wsb36 675K Feb 27 17:55 aa_233_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr3.bed.gz
-rw-r--r-- 1 mxm1368 wsb36 426K Feb 27 17:55 aa_233_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr4.bed.gz
-rw-r--r-- 1 mxm1368 wsb36 552K Feb 27 17:55 aa_233_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr5.bed.gz
-rw-r--r-- 1 mxm1368 wsb36 649K Feb 27 17:55 aa_233_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr6.bed.gz
-rw-r--r-- 1 mxm1368 wsb36 663K Feb 27 17:55 aa_233_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr7.bed.gz
-rw-r--r-- 1 mxm1368 wsb36 421K Feb 27 17:55 aa_233_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr8.bed.gz
-rw-r--r-- 1 mxm1368 wsb36 487K Feb 27 17:55 aa_233_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr9.bed.gz
-rw-r--r-- 1 mxm1368 wsb36 399K Feb 27 17:55 aa_233_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chrX.bed.gz
-rw-r--r-- 1 mxm1368 wsb36  12K Feb 27 17:55 aa_233_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chrY.bed.gz
```

A summary of the phenotype data including size used for TensorQTL - trans:


```
$ pwd
/mnt/pan/Data14/metabrain_lasso/rna_seq_norm/aa_233/mol_phe

$ ls -lh *tmm.expression.bed.gz
-rw-r----- 1 mxm1368 wsb36 13M Feb 27 17:55 aa_233_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.gz

```

### Path(s) to covariate data matrix

Here please document the exact covariate matrix used for QTL calling, **including selected covariates from sample attribute file, genotype PC and phenotype hidden confounding factors computed in your previous analysis**
- Path(s) to the data on your local cluster where you analyzed the data. 
- Bush Lab, server:  rider.case.edu `/mnt/pan/Data14/metabrain_lasso/rna_seq_norm/aa_233/cov/`
- NIAGADS FTP, `/ftp_fgc_xqtl/projects/...`

A summary of the covariate data including size used for TensorQTL - cis & trans:

```
$ ls -lh *tmm.expression.cov_pca.resid.PEER.cov.gz
-rw-r--r-- 1 mxm1368 wsb36 85K Feb 27 18:04 aa_no_rel.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.cov_pca.resid.PEER.cov.gz

```
### Path(s) to QTL results
- TensorQTL - cis: Bush Lab, server:  rider.case.edu `/mnt/pan/Data14/metabrain_lasso/rna_seq_norm/aa_233/tensorqtl/cis/plink_mac5`
- TensorQTL - trans: Bush Lab, server:  rider.case.edu `/mnt/pan/Data14/metabrain_lasso/rna_seq_norm/aa_233/tensorqtl/trans/plink_mac5`

A summary of the TensorQTL - cis data including size:

```
$ ls -lh
total 34G
-rw-r--r-- 1 mxm1368 wsb36 177M Mar 23 15:48 aa_no_rel.10.cis_qtl_pairs.10.parquet
-rw-r--r-- 1 mxm1368 wsb36  360 Mar 23 16:51 aa_no_rel.10.cis_qtl_pairs.10.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36  52K Mar 23 16:51 aa_no_rel.10.cis_qtl_pairs.10.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 169K Mar 23 16:51 aa_no_rel.10.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 970M Mar 23 15:53 aa_no_rel.10.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36 229M Mar 23 15:03 aa_no_rel.11.cis_qtl_pairs.11.parquet
-rw-r--r-- 1 mxm1368 wsb36  285 Mar 23 16:31 aa_no_rel.11.cis_qtl_pairs.11.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36  78K Mar 23 16:31 aa_no_rel.11.cis_qtl_pairs.11.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 247K Mar 23 16:31 aa_no_rel.11.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 1.3G Mar 23 15:09 aa_no_rel.11.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36 241M Mar 23 16:51 aa_no_rel.12.cis_qtl_pairs.12.parquet
-rw-r--r-- 1 mxm1368 wsb36  285 Mar 23 17:55 aa_no_rel.12.cis_qtl_pairs.12.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36  79K Mar 23 17:55 aa_no_rel.12.cis_qtl_pairs.12.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 248K Mar 23 17:55 aa_no_rel.12.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 1.4G Mar 23 16:58 aa_no_rel.12.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36  84M Mar 23 16:13 aa_no_rel.13.cis_qtl_pairs.13.parquet
-rw-r--r-- 1 mxm1368 wsb36  360 Mar 23 16:42 aa_no_rel.13.cis_qtl_pairs.13.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36  24K Mar 23 16:42 aa_no_rel.13.cis_qtl_pairs.13.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36  78K Mar 23 16:42 aa_no_rel.13.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 454M Mar 23 16:15 aa_no_rel.13.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36 186M Mar 23 14:59 aa_no_rel.14.cis_qtl_pairs.14.parquet
-rw-r--r-- 1 mxm1368 wsb36  285 Mar 23 16:06 aa_no_rel.14.cis_qtl_pairs.14.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36  55K Mar 23 16:06 aa_no_rel.14.cis_qtl_pairs.14.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 178K Mar 23 16:06 aa_no_rel.14.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 1.1G Mar 23 15:03 aa_no_rel.14.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36 145M Mar 23 15:51 aa_no_rel.15.cis_qtl_pairs.15.parquet
-rw-r--r-- 1 mxm1368 wsb36  360 Mar 23 16:45 aa_no_rel.15.cis_qtl_pairs.15.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36  46K Mar 23 16:45 aa_no_rel.15.cis_qtl_pairs.15.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 151K Mar 23 16:45 aa_no_rel.15.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 778M Mar 23 15:56 aa_no_rel.15.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36 214M Mar 23 15:02 aa_no_rel.16.cis_qtl_pairs.16.parquet
-rw-r--r-- 1 mxm1368 wsb36  285 Mar 23 16:25 aa_no_rel.16.cis_qtl_pairs.16.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36  76K Mar 23 16:25 aa_no_rel.16.cis_qtl_pairs.16.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 238K Mar 23 16:25 aa_no_rel.16.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 1.2G Mar 23 15:08 aa_no_rel.16.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36 253M Mar 23 17:13 aa_no_rel.17.cis_qtl_pairs.17.parquet
-rw-r--r-- 1 mxm1368 wsb36  285 Mar 23 18:02 aa_no_rel.17.cis_qtl_pairs.17.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36  92K Mar 23 18:02 aa_no_rel.17.cis_qtl_pairs.17.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 289K Mar 23 18:02 aa_no_rel.17.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 1.4G Mar 23 17:18 aa_no_rel.17.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36  72M Mar 23 14:51 aa_no_rel.18.cis_qtl_pairs.18.parquet
-rw-r--r-- 1 mxm1368 wsb36  285 Mar 23 15:11 aa_no_rel.18.cis_qtl_pairs.18.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36  20K Mar 23 15:11 aa_no_rel.18.cis_qtl_pairs.18.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36  63K Mar 23 15:11 aa_no_rel.18.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 382M Mar 23 14:52 aa_no_rel.18.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36 347M Mar 23 15:10 aa_no_rel.19.cis_qtl_pairs.19.parquet
-rw-r--r-- 1 mxm1368 wsb36  285 Mar 23 17:17 aa_no_rel.19.cis_qtl_pairs.19.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36 110K Mar 23 17:17 aa_no_rel.19.cis_qtl_pairs.19.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 346K Mar 23 17:17 aa_no_rel.19.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 1.9G Mar 23 15:20 aa_no_rel.19.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36 415M Mar 23 15:18 aa_no_rel.1.cis_qtl_pairs.1.parquet
-rw-r--r-- 1 mxm1368 wsb36  360 Mar 23 17:44 aa_no_rel.1.cis_qtl_pairs.1.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36 147K Mar 23 17:44 aa_no_rel.1.cis_qtl_pairs.1.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 459K Mar 23 17:44 aa_no_rel.1.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 2.3G Mar 23 15:30 aa_no_rel.1.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36 115M Mar 23 14:54 aa_no_rel.20.cis_qtl_pairs.20.parquet
-rw-r--r-- 1 mxm1368 wsb36  285 Mar 23 15:33 aa_no_rel.20.cis_qtl_pairs.20.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36  36K Mar 23 15:33 aa_no_rel.20.cis_qtl_pairs.20.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 117K Mar 23 15:33 aa_no_rel.20.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 621M Mar 23 14:57 aa_no_rel.20.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36  58M Mar 23 16:30 aa_no_rel.21.cis_qtl_pairs.21.parquet
-rw-r--r-- 1 mxm1368 wsb36  360 Mar 23 16:49 aa_no_rel.21.cis_qtl_pairs.21.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36  15K Mar 23 16:49 aa_no_rel.21.cis_qtl_pairs.21.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36  48K Mar 23 16:49 aa_no_rel.21.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 299M Mar 23 16:32 aa_no_rel.21.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36 116M Mar 23 14:55 aa_no_rel.22.cis_qtl_pairs.22.parquet
-rw-r--r-- 1 mxm1368 wsb36  285 Mar 23 15:39 aa_no_rel.22.cis_qtl_pairs.22.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36  41K Mar 23 15:39 aa_no_rel.22.cis_qtl_pairs.22.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 133K Mar 23 15:39 aa_no_rel.22.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 667M Mar 23 14:58 aa_no_rel.22.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36 286M Mar 23 15:35 aa_no_rel.2.cis_qtl_pairs.2.parquet
-rw-r--r-- 1 mxm1368 wsb36  360 Mar 23 17:18 aa_no_rel.2.cis_qtl_pairs.2.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36  96K Mar 23 17:18 aa_no_rel.2.cis_qtl_pairs.2.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 302K Mar 23 17:18 aa_no_rel.2.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 1.6G Mar 23 15:43 aa_no_rel.2.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36 227M Mar 23 17:05 aa_no_rel.3.cis_qtl_pairs.3.parquet
-rw-r--r-- 1 mxm1368 wsb36  360 Mar 23 17:58 aa_no_rel.3.cis_qtl_pairs.3.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36  77K Mar 23 17:58 aa_no_rel.3.cis_qtl_pairs.3.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 242K Mar 23 17:58 aa_no_rel.3.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 1.3G Mar 23 17:11 aa_no_rel.3.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36 152M Mar 23 16:14 aa_no_rel.4.cis_qtl_pairs.4.parquet
-rw-r--r-- 1 mxm1368 wsb36  360 Mar 23 17:10 aa_no_rel.4.cis_qtl_pairs.4.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36  47K Mar 23 17:10 aa_no_rel.4.cis_qtl_pairs.4.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 153K Mar 23 17:10 aa_no_rel.4.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 856M Mar 23 16:19 aa_no_rel.4.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36 192M Mar 23 16:58 aa_no_rel.5.cis_qtl_pairs.5.parquet
-rw-r--r-- 1 mxm1368 wsb36  360 Mar 23 17:50 aa_no_rel.5.cis_qtl_pairs.5.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36  61K Mar 23 17:50 aa_no_rel.5.cis_qtl_pairs.5.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 198K Mar 23 17:50 aa_no_rel.5.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 1.1G Mar 23 17:04 aa_no_rel.5.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36 294M Mar 23 17:08 aa_no_rel.6.cis_qtl_pairs.6.parquet
-rw-r--r-- 1 mxm1368 wsb36  360 Mar 23 18:01 aa_no_rel.6.cis_qtl_pairs.6.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36  74K Mar 23 18:01 aa_no_rel.6.cis_qtl_pairs.6.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 233K Mar 23 18:01 aa_no_rel.6.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 1.7G Mar 23 17:16 aa_no_rel.6.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36 218M Mar 23 15:02 aa_no_rel.7.cis_qtl_pairs.7.parquet
-rw-r--r-- 1 mxm1368 wsb36  285 Mar 23 16:25 aa_no_rel.7.cis_qtl_pairs.7.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36  75K Mar 23 16:25 aa_no_rel.7.cis_qtl_pairs.7.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 238K Mar 23 16:25 aa_no_rel.7.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 1.2G Mar 23 15:07 aa_no_rel.7.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36 170M Mar 23 16:39 aa_no_rel.8.cis_qtl_pairs.8.parquet
-rw-r--r-- 1 mxm1368 wsb36  360 Mar 23 17:30 aa_no_rel.8.cis_qtl_pairs.8.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36  47K Mar 23 17:30 aa_no_rel.8.cis_qtl_pairs.8.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 152K Mar 23 17:30 aa_no_rel.8.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 904M Mar 23 16:44 aa_no_rel.8.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36 178M Mar 23 14:58 aa_no_rel.9.cis_qtl_pairs.9.parquet
-rw-r--r-- 1 mxm1368 wsb36  285 Mar 23 16:00 aa_no_rel.9.cis_qtl_pairs.9.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36  52K Mar 23 16:00 aa_no_rel.9.cis_qtl_pairs.9.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 169K Mar 23 16:00 aa_no_rel.9.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 944M Mar 23 15:02 aa_no_rel.9.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36  100 Mar 23 18:02 aa_no_rel.emprical.cis_sumstats.summary
-rw-r--r-- 1 mxm1368 wsb36 5.9M Mar 23 18:02 aa_no_rel.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36  311 Mar 23 18:02 TensorQTL.cis._column_info.txt
-rw-r--r-- 1 mxm1368 wsb36 5.0K Mar 23 18:02 TensorQTL.cis._recipe.tsv
-rw-r--r-- 1 mxm1368 wsb36  18K Mar 23 18:02 TensorQTL.cis._recipe.tsv.stderr
-rw-r--r-- 1 mxm1368 wsb36   46 Mar 23 18:02 TensorQTL.cis._recipe.tsv.stdout

```

A summary of the TensorQTL - trans data including size:


```
$ ls -lh
total 5.1M
-rw-r--r-- 1 mxm1368 wsb36 3.7M Mar 24 09:41 aa_233_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.norminal.trans_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36  360 Mar 24 09:41 aa_233_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.norminal.trans_long_table.txt.stderr
-rw-r--r-- 1 mxm1368 wsb36  68K Mar 24 09:41 aa_233_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.norminal.trans_long_table.txt.stdout
-rw-r--r-- 1 mxm1368 wsb36  189 Mar 24 09:41 TensorQTL.trans._column_info.txt
-rw-r--r-- 1 mxm1368 wsb36  324 Mar 24 09:41 TensorQTL.trans._recipe.tsv

```


### Path(s) to fine-mapping with SuSiE model
### Path(s) to fine-mapping with SuSiE RSS model
### Path(s) to colocalization with SuSiE-coloc

## Links to QTL analysis notebooks

Please list the links to analysis notebooks in the order you executed our pipeline:
	1. Genotype processing: https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Bush_CWRU/magenta_aa_eqtl_genotype_processing.ipynb
	2. Phenotype processing: https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Bush_CWRU/magenta_aa_eqtl_phenotype_processing.ipynb
	3. Covariate processing: https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Bush_CWRU/magenta_aa_eqtl_covariate_processing.ipynb
	4. TensorQTL analysis:  https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Bush_CWRU/magenta_aa_eqtl_tensorqtl.ipynb
  5. Complete analysis pipeline: https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Bush_CWRU/magenta_aa_eqtl_complete_analysis.ipynb


