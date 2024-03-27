# MAGENTA Non-Hispanic White Blood Gene Expression QTL

Multi-Ancestry Genomics, Epigenomics, and Transcriptomics of Alzheimer’s (MAGENTA) Project: Participants include 465 individuals (AA – 113 with AD, 118 cognitively intact controls; NHW – 116 with AD, 118 controls) ascertained by the John P. Hussman Institute for Human Genomics (HIHG) at the University of Miami Miller School of Medicine (Miami, FL), North Carolina A&T State University (Greensboro, NC), and Case Western Reserve University (Cleveland, OH).  Participants were ascertained as part of the ADSP Follow-up Study and included both cases (>65 years of age of onset) and controls (>65 years of age at age of exam).  All participants were adjudicated by a clinical panel with expertise in AD related disorders and classified as AD according to standard criteria developed by the National Institute of Aging and the Alzheimer’s Association. 

## Contact
Makaela Mews (analyst; mxm1368@case.edu);  Dr. William S. Bush (wsb36@case.edu);  Dr. Anthony J. Griswold (Griswold, Anthony J agriswold@miami.edu)

## Study Overview

- Sample information: `MAGENTA/MAGENTA_NHW_eqtl_sample_attributes.csv`.
- Lab protocol: `MAGENTA/MAGENTA_NHW_eqtl_lab_protocol.csv`.
- Computational protocol: `MAGENTA/MAGENTA_NHW_eqtl_computational_protocol.csv`.
- QTL summary statistics output: `MAGENTA/MAGENTA_NHW_expression.qtl_results.csv`.

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
- TensorQTL - cis:  Bush Lab, server:  rider.case.edu `/mnt/pan/Data14/metabrain_lasso/rna_seq_norm/nhw_239/geno/by_chr/nhw_chr_1_22.no_rel.filtered.plink_files_list.txt`
- TensorQTL - trans:  Bush Lab, server:  rider.case.edu `/mnt/pan/Data14/metabrain_lasso/rna_seq_norm/nhw_239/geno/geno_final/rerun/nhw_chr_1_22.no_rel.filtered.bed`
- NIAGADS FTP, `/ftp_fgc_xqtl/projects/...`

A summary of the genotype data including size used for TensorQTL - cis:

```
$ ls -lh *{bed,bim,fam,txt}
-rw-r--r-- 1 mxm1368 wsb36  29M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.10.bed
-rw-r--r-- 1 mxm1368 wsb36  19M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.10.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.10.fam
-rw-r--r-- 1 mxm1368 wsb36  28M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.11.bed
-rw-r--r-- 1 mxm1368 wsb36  18M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.11.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.11.fam
-rw-r--r-- 1 mxm1368 wsb36  28M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.12.bed
-rw-r--r-- 1 mxm1368 wsb36  18M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.12.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.12.fam
-rw-r--r-- 1 mxm1368 wsb36  21M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.13.bed
-rw-r--r-- 1 mxm1368 wsb36  13M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.13.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.13.fam
-rw-r--r-- 1 mxm1368 wsb36  19M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.14.bed
-rw-r--r-- 1 mxm1368 wsb36  12M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.14.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.14.fam
-rw-r--r-- 1 mxm1368 wsb36  16M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.15.bed
-rw-r--r-- 1 mxm1368 wsb36  10M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.15.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.15.fam
-rw-r--r-- 1 mxm1368 wsb36  18M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.16.bed
-rw-r--r-- 1 mxm1368 wsb36  11M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.16.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.16.fam
-rw-r--r-- 1 mxm1368 wsb36  16M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.17.bed
-rw-r--r-- 1 mxm1368 wsb36 9.3M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.17.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.17.fam
-rw-r--r-- 1 mxm1368 wsb36  17M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.18.bed
-rw-r--r-- 1 mxm1368 wsb36  11M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.18.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.18.fam
-rw-r--r-- 1 mxm1368 wsb36  13M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.19.bed
-rw-r--r-- 1 mxm1368 wsb36 7.9M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.19.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.19.fam
-rw-r--r-- 1 mxm1368 wsb36  44M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.1.bed
-rw-r--r-- 1 mxm1368 wsb36  27M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.1.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.1.fam
-rw-r--r-- 1 mxm1368 wsb36  13M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.20.bed
-rw-r--r-- 1 mxm1368 wsb36 7.8M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.20.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.20.fam
-rw-r--r-- 1 mxm1368 wsb36 7.8M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.21.bed
-rw-r--r-- 1 mxm1368 wsb36 4.9M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.21.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.21.fam
-rw-r--r-- 1 mxm1368 wsb36 7.9M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.22.bed
-rw-r--r-- 1 mxm1368 wsb36 4.9M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.22.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.22.fam
-rw-r--r-- 1 mxm1368 wsb36  47M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.2.bed
-rw-r--r-- 1 mxm1368 wsb36  29M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.2.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.2.fam
-rw-r--r-- 1 mxm1368 wsb36  41M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.3.bed
-rw-r--r-- 1 mxm1368 wsb36  25M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.3.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.3.fam
-rw-r--r-- 1 mxm1368 wsb36  41M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.4.bed
-rw-r--r-- 1 mxm1368 wsb36  25M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.4.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.4.fam
-rw-r--r-- 1 mxm1368 wsb36  37M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.5.bed
-rw-r--r-- 1 mxm1368 wsb36  22M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.5.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.5.fam
-rw-r--r-- 1 mxm1368 wsb36  38M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.6.bed
-rw-r--r-- 1 mxm1368 wsb36  23M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.6.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.6.fam
-rw-r--r-- 1 mxm1368 wsb36  34M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.7.bed
-rw-r--r-- 1 mxm1368 wsb36  20M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.7.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.7.fam
-rw-r--r-- 1 mxm1368 wsb36  32M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.8.bed
-rw-r--r-- 1 mxm1368 wsb36  19M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.8.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.8.fam
-rw-r--r-- 1 mxm1368 wsb36  25M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.9.bed
-rw-r--r-- 1 mxm1368 wsb36  15M Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.9.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 23 14:26 nhw_chr_1_22.no_rel.filtered.9.fam
-rw-r--r-- 1 mxm1368 wsb36 2.3K Mar 23 14:27 nhw_chr_1_22.no_rel.filtered.plink_files_list.txt

```

A summary of the genotype data including size used for TensorQTL - trans:

```
$ ls -lh *.no_rel.filtered.{bim,bed,fam}
-rw-r--r-- 1 mxm1368 wsb36 563M Mar 22 13:30 nhw_chr_1_22.no_rel.filtered.bed
-rw-r--r-- 1 mxm1368 wsb36 344M Mar 22 13:30 nhw_chr_1_22.no_rel.filtered.bim
-rw-r--r-- 1 mxm1368 wsb36 5.9K Mar 22 13:30 nhw_chr_1_22.no_rel.filtered.fam

```

### Path(s) to omics-data matrix
Here please document the exact omics-data matrix used for QTL calling.
- Path(s) to the data on your local cluster where you analyzed the data. 
- TensorQTL - cis:  Bush Lab, server: rider.case.edu `/mnt/pan/Data14/metabrain_lasso/rna_seq_norm/nhw_239/mol_phe/tmm_per_chr`
- TensorQTL - trans:  Bush Lab, server: rider.case.edu `/mnt/pan/Data14/metabrain_lasso/rna_seq_norm/nhw_239/mol_phe`
- NIAGADS FTP, `/ftp_fgc_xqtl/projects/...`
 
A summary of the phenotype data including size used for TensorQTL - cis:


```
$ pwd
/mnt/pan/Data14/metabrain_lasso/rna_seq_norm/nhw_239/mol_phe/tmm_per_chr

$ ls -lh *.bed.gz
-rw-r--r-- 1 mxm1368 wsb36  489K Mar  2 19:05 nhw_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr10.bed.gz
-rw-r--r-- 1 mxm1368 wsb36  718K Mar  2 19:06 nhw_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr11.bed.gz
-rw-r--r-- 1 mxm1368 wsb36  722K Mar  2 19:06 nhw_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr12.bed.gz
-rw-r--r-- 1 mxm1368 wsb36  224K Mar  2 19:06 nhw_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr13.bed.gz
-rw-r--r-- 1 mxm1368 wsb36  508K Mar  2 19:06 nhw_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr14.bed.gz
-rw-r--r-- 1 mxm1368 wsb36  436K Mar  2 19:05 nhw_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr15.bed.gz
-rw-r--r-- 1 mxm1368 wsb36  692K Mar  2 19:06 nhw_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr16.bed.gz
-rw-r--r-- 1 mxm1368 wsb36  870K Mar  2 19:06 nhw_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr17.bed.gz
-rw-r--r-- 1 mxm1368 wsb36  196K Mar  2 19:05 nhw_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr18.bed.gz
-rw-r--r-- 1 mxm1368 wsb36 1003K Mar  2 19:05 nhw_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr19.bed.gz
-rw-r--r-- 1 mxm1368 wsb36  1.4M Mar  2 19:05 nhw_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr1.bed.gz
-rw-r--r-- 1 mxm1368 wsb36  347K Mar  2 19:06 nhw_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr20.bed.gz
-rw-r--r-- 1 mxm1368 wsb36  143K Mar  2 19:06 nhw_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr21.bed.gz
-rw-r--r-- 1 mxm1368 wsb36  388K Mar  2 19:06 nhw_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr22.bed.gz
-rw-r--r-- 1 mxm1368 wsb36  873K Mar  2 19:06 nhw_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr2.bed.gz
-rw-r--r-- 1 mxm1368 wsb36  700K Mar  2 19:06 nhw_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr3.bed.gz
-rw-r--r-- 1 mxm1368 wsb36  442K Mar  2 19:05 nhw_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr4.bed.gz
-rw-r--r-- 1 mxm1368 wsb36  576K Mar  2 19:05 nhw_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr5.bed.gz
-rw-r--r-- 1 mxm1368 wsb36  680K Mar  2 19:05 nhw_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr6.bed.gz
-rw-r--r-- 1 mxm1368 wsb36  688K Mar  2 19:05 nhw_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr7.bed.gz
-rw-r--r-- 1 mxm1368 wsb36  436K Mar  2 19:05 nhw_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr8.bed.gz
-rw-r--r-- 1 mxm1368 wsb36  506K Mar  2 19:06 nhw_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chr9.bed.gz
-rw-r--r-- 1 mxm1368 wsb36  417K Mar  2 19:05 nhw_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chrX.bed.gz
-rw-r--r-- 1 mxm1368 wsb36   14K Mar  2 19:05 nhw_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.chrY.bed.gz

```

A summary of the phenotype data including size used for TensorQTL - trans:


```
$ pwd
/mnt/pan/Data14/metabrain_lasso/rna_seq_norm/nhw_239/mol_phe

$ ls -lh *tmm.expression.bed.gz
-rw-r--r-- 1 mxm1368 wsb36 14M Feb 27 18:02 nhw_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.bed.gz

```

### Path(s) to covariate data matrix

Here please document the exact covariate matrix used for QTL calling, **including selected covariates from sample attribute file, genotype PC and phenotype hidden confounding factors computed in your previous analysis**
- Path(s) to the data on your local cluster where you analyzed the data. 
- Bush Lab, server:  rider.case.edu `/mnt/pan/Data14/metabrain_lasso/rna_seq_norm/nhw_239/cov`
- NIAGADS FTP, `/ftp_fgc_xqtl/projects/...`

A summary of the covariate data including size used for TensorQTL - cis & trans:

```
$ ls -lh *tmm.expression.cov_pca.resid.PEER.cov.gz
-rw-r--r-- 1 mxm1368 wsb36 91K Mar  2 19:01 nhw_no_rel.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.cov_pca.resid.PEER.cov.gz

```
### Path(s) to QTL results
- TensorQTL - cis: Bush Lab, server:  rider.case.edu `/mnt/pan/Data14/metabrain_lasso/rna_seq_norm/nhw_239/tensorqtl/cis/plink_mac5`
- TensorQTL - trans: Bush Lab, server:  rider.case.edu `/mnt/pan/Data14/metabrain_lasso/rna_seq_norm/nhw_239/tensorqtl/trans/plink_mac5`

A summary of the TensorQTL - cis data including size:

```
$ ls -lh
total 30G
-rw-r--r-- 1 mxm1368 wsb36 144M Mar 23 14:48 nhw_no_rel.10.cis_qtl_pairs.10.parquet
-rw-r--r-- 1 mxm1368 wsb36  285 Mar 23 15:40 nhw_no_rel.10.cis_qtl_pairs.10.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36  75K Mar 23 15:40 nhw_no_rel.10.cis_qtl_pairs.10.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 169K Mar 23 15:40 nhw_no_rel.10.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 801M Mar 23 14:51 nhw_no_rel.10.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36 193M Mar 23 15:59 nhw_no_rel.11.cis_qtl_pairs.11.parquet
-rw-r--r-- 1 mxm1368 wsb36  360 Mar 23 17:08 nhw_no_rel.11.cis_qtl_pairs.11.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36 113K Mar 23 17:08 nhw_no_rel.11.cis_qtl_pairs.11.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 246K Mar 23 17:08 nhw_no_rel.11.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 1.1G Mar 23 16:05 nhw_no_rel.11.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36 201M Mar 23 16:58 nhw_no_rel.12.cis_qtl_pairs.12.parquet
-rw-r--r-- 1 mxm1368 wsb36  360 Mar 23 17:25 nhw_no_rel.12.cis_qtl_pairs.12.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36 112K Mar 23 17:25 nhw_no_rel.12.cis_qtl_pairs.12.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 248K Mar 23 17:25 nhw_no_rel.12.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 1.2G Mar 23 17:02 nhw_no_rel.12.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36  69M Mar 23 16:01 nhw_no_rel.13.cis_qtl_pairs.13.parquet
-rw-r--r-- 1 mxm1368 wsb36  360 Mar 23 16:24 nhw_no_rel.13.cis_qtl_pairs.13.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36  38K Mar 23 16:24 nhw_no_rel.13.cis_qtl_pairs.13.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36  77K Mar 23 16:24 nhw_no_rel.13.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 378M Mar 23 16:02 nhw_no_rel.13.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36 147M Mar 23 16:01 nhw_no_rel.14.cis_qtl_pairs.14.parquet
-rw-r--r-- 1 mxm1368 wsb36  360 Mar 23 16:55 nhw_no_rel.14.cis_qtl_pairs.14.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36  82K Mar 23 16:55 nhw_no_rel.14.cis_qtl_pairs.14.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 175K Mar 23 16:55 nhw_no_rel.14.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 845M Mar 23 16:05 nhw_no_rel.14.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36 121M Mar 23 14:46 nhw_no_rel.15.cis_qtl_pairs.15.parquet
-rw-r--r-- 1 mxm1368 wsb36  285 Mar 23 15:30 nhw_no_rel.15.cis_qtl_pairs.15.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36  67K Mar 23 15:30 nhw_no_rel.15.cis_qtl_pairs.15.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 151K Mar 23 15:30 nhw_no_rel.15.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 654M Mar 23 14:49 nhw_no_rel.15.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36 191M Mar 23 15:49 nhw_no_rel.16.cis_qtl_pairs.16.parquet
-rw-r--r-- 1 mxm1368 wsb36  360 Mar 23 16:57 nhw_no_rel.16.cis_qtl_pairs.16.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36 100K Mar 23 16:57 nhw_no_rel.16.cis_qtl_pairs.16.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 238K Mar 23 16:57 nhw_no_rel.16.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 1.1G Mar 23 15:54 nhw_no_rel.16.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36 232M Mar 23 16:12 nhw_no_rel.17.cis_qtl_pairs.17.parquet
-rw-r--r-- 1 mxm1368 wsb36  360 Mar 23 17:20 nhw_no_rel.17.cis_qtl_pairs.17.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36 125K Mar 23 17:20 nhw_no_rel.17.cis_qtl_pairs.17.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 300K Mar 23 17:20 nhw_no_rel.17.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 1.3G Mar 23 16:19 nhw_no_rel.17.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36  63M Mar 23 14:41 nhw_no_rel.18.cis_qtl_pairs.18.parquet
-rw-r--r-- 1 mxm1368 wsb36  285 Mar 23 14:59 nhw_no_rel.18.cis_qtl_pairs.18.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36  31K Mar 23 14:59 nhw_no_rel.18.cis_qtl_pairs.18.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36  68K Mar 23 14:59 nhw_no_rel.18.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 339M Mar 23 14:42 nhw_no_rel.18.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36 325M Mar 23 15:00 nhw_no_rel.19.cis_qtl_pairs.19.parquet
-rw-r--r-- 1 mxm1368 wsb36  285 Mar 23 16:53 nhw_no_rel.19.cis_qtl_pairs.19.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36 144K Mar 23 16:53 nhw_no_rel.19.cis_qtl_pairs.19.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 344K Mar 23 16:53 nhw_no_rel.19.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 1.8G Mar 23 15:08 nhw_no_rel.19.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36 345M Mar 23 15:07 nhw_no_rel.1.cis_qtl_pairs.1.parquet
-rw-r--r-- 1 mxm1368 wsb36  285 Mar 23 17:12 nhw_no_rel.1.cis_qtl_pairs.1.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36 189K Mar 23 17:12 nhw_no_rel.1.cis_qtl_pairs.1.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 458K Mar 23 17:12 nhw_no_rel.1.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 1.9G Mar 23 15:17 nhw_no_rel.1.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36 102M Mar 23 15:09 nhw_no_rel.20.cis_qtl_pairs.20.parquet
-rw-r--r-- 1 mxm1368 wsb36  285 Mar 23 15:47 nhw_no_rel.20.cis_qtl_pairs.20.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36  54K Mar 23 15:47 nhw_no_rel.20.cis_qtl_pairs.20.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 119K Mar 23 15:47 nhw_no_rel.20.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 555M Mar 23 15:11 nhw_no_rel.20.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36  48M Mar 23 15:40 nhw_no_rel.21.cis_qtl_pairs.21.parquet
-rw-r--r-- 1 mxm1368 wsb36  285 Mar 23 15:54 nhw_no_rel.21.cis_qtl_pairs.21.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36  25K Mar 23 15:54 nhw_no_rel.21.cis_qtl_pairs.21.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36  48K Mar 23 15:54 nhw_no_rel.21.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 241M Mar 23 15:41 nhw_no_rel.21.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36 112M Mar 23 16:35 nhw_no_rel.22.cis_qtl_pairs.22.parquet
-rw-r--r-- 1 mxm1368 wsb36  285 Mar 23 17:10 nhw_no_rel.22.cis_qtl_pairs.22.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36  50K Mar 23 17:10 nhw_no_rel.22.cis_qtl_pairs.22.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 134K Mar 23 17:10 nhw_no_rel.22.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 647M Mar 23 16:38 nhw_no_rel.22.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36 234M Mar 23 16:28 nhw_no_rel.2.cis_qtl_pairs.2.parquet
-rw-r--r-- 1 mxm1368 wsb36  360 Mar 23 17:24 nhw_no_rel.2.cis_qtl_pairs.2.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36 124K Mar 23 17:24 nhw_no_rel.2.cis_qtl_pairs.2.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 300K Mar 23 17:24 nhw_no_rel.2.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 1.3G Mar 23 16:34 nhw_no_rel.2.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36 188M Mar 23 16:40 nhw_no_rel.3.cis_qtl_pairs.3.parquet
-rw-r--r-- 1 mxm1368 wsb36  360 Mar 23 17:23 nhw_no_rel.3.cis_qtl_pairs.3.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36 102K Mar 23 17:23 nhw_no_rel.3.cis_qtl_pairs.3.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 240K Mar 23 17:23 nhw_no_rel.3.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 1.1G Mar 23 16:45 nhw_no_rel.3.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36 133M Mar 23 14:47 nhw_no_rel.4.cis_qtl_pairs.4.parquet
-rw-r--r-- 1 mxm1368 wsb36  285 Mar 23 15:35 nhw_no_rel.4.cis_qtl_pairs.4.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36  69K Mar 23 15:35 nhw_no_rel.4.cis_qtl_pairs.4.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 153K Mar 23 15:35 nhw_no_rel.4.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 752M Mar 23 14:49 nhw_no_rel.4.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36 163M Mar 23 14:49 nhw_no_rel.5.cis_qtl_pairs.5.parquet
-rw-r--r-- 1 mxm1368 wsb36  285 Mar 23 15:50 nhw_no_rel.5.cis_qtl_pairs.5.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36  81K Mar 23 15:50 nhw_no_rel.5.cis_qtl_pairs.5.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 198K Mar 23 15:50 nhw_no_rel.5.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 886M Mar 23 14:53 nhw_no_rel.5.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36 248M Mar 23 14:53 nhw_no_rel.6.cis_qtl_pairs.6.parquet
-rw-r--r-- 1 mxm1368 wsb36  285 Mar 23 16:21 nhw_no_rel.6.cis_qtl_pairs.6.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36  85K Mar 23 16:21 nhw_no_rel.6.cis_qtl_pairs.6.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 235K Mar 23 16:21 nhw_no_rel.6.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 1.5G Mar 23 15:00 nhw_no_rel.6.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36 196M Mar 23 14:52 nhw_no_rel.7.cis_qtl_pairs.7.parquet
-rw-r--r-- 1 mxm1368 wsb36  285 Mar 23 16:04 nhw_no_rel.7.cis_qtl_pairs.7.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36  98K Mar 23 16:04 nhw_no_rel.7.cis_qtl_pairs.7.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 237K Mar 23 16:04 nhw_no_rel.7.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 1.1G Mar 23 14:57 nhw_no_rel.7.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36 132M Mar 23 14:47 nhw_no_rel.8.cis_qtl_pairs.8.parquet
-rw-r--r-- 1 mxm1368 wsb36  285 Mar 23 15:33 nhw_no_rel.8.cis_qtl_pairs.8.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36  66K Mar 23 15:33 nhw_no_rel.8.cis_qtl_pairs.8.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 150K Mar 23 15:33 nhw_no_rel.8.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 712M Mar 23 14:49 nhw_no_rel.8.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36 150M Mar 23 15:47 nhw_no_rel.9.cis_qtl_pairs.9.parquet
-rw-r--r-- 1 mxm1368 wsb36  360 Mar 23 16:39 nhw_no_rel.9.cis_qtl_pairs.9.parquet.stderr
-rw-r--r-- 1 mxm1368 wsb36  73K Mar 23 16:39 nhw_no_rel.9.cis_qtl_pairs.9.parquet.stdout
-rw-r--r-- 1 mxm1368 wsb36 174K Mar 23 16:39 nhw_no_rel.9.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36 793M Mar 23 15:51 nhw_no_rel.9.norminal.cis_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36  106 Mar 23 17:26 nhw_no_rel.emprical.cis_sumstats.summary
-rw-r--r-- 1 mxm1368 wsb36 5.9M Mar 23 17:26 nhw_no_rel.emprical.cis_sumstats.txt
-rw-r--r-- 1 mxm1368 wsb36  311 Mar 23 17:25 TensorQTL.cis._column_info.txt
-rw-r--r-- 1 mxm1368 wsb36 5.0K Mar 23 17:25 TensorQTL.cis._recipe.tsv
-rw-r--r-- 1 mxm1368 wsb36  18K Mar 23 17:26 TensorQTL.cis._recipe.tsv.stderr
-rw-r--r-- 1 mxm1368 wsb36   46 Mar 23 17:25 TensorQTL.cis._recipe.tsv.stdout

```

A summary of the TensorQTL - trans data including size:

```
$ ls -lh
total 6.5M
-rw-r--r-- 1 mxm1368 wsb36 4.9M Mar 24 09:42 nhw_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.norminal.trans_long_table.txt
-rw-r--r-- 1 mxm1368 wsb36  360 Mar 24 09:42 nhw_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.norminal.trans_long_table.txt.stderr
-rw-r--r-- 1 mxm1368 wsb36  56K Mar 24 09:42 nhw_gene_tpm_prep_v2.low_expression_filtered.outlier_removed.tmm.expression.norminal.trans_long_table.txt.stdout
-rw-r--r-- 1 mxm1368 wsb36  189 Mar 24 09:42 TensorQTL.trans._column_info.txt
-rw-r--r-- 1 mxm1368 wsb36  323 Mar 24 09:42 TensorQTL.trans._recipe.tsv

```


### Path(s) to fine-mapping with SuSiE model
### Path(s) to fine-mapping with SuSiE RSS model
### Path(s) to colocalization with SuSiE-coloc

## Links to QTL analysis notebooks

Please list the links to analysis notebooks in the order you executed our pipeline:
	1. Genotype processing: https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Bush_CWRU/magenta_nhw_eqtl_genotype_processing.ipynb
	2. Phenotype processing: https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Bush_CWRU/magenta_nhw_eqtl_phenotype_processing.ipynb
	3. Covariate processing: https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Bush_CWRU/magenta_nhw_eqtl_covariate_processing.ipynb
	4. TensorQTL analysis:  https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Bush_CWRU/magenta_nhw_eqtl_tensorqtl.ipynb
  5. Complete analysis pipeline: https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Bush_CWRU/magenta_nhw_eqtl_complete_analysis.ipynb


