#  MAGENTA African American blood gene expression

Multi-Ancestry Genomics, Epigenomics, and Transcriptomics of Alzheimer’s (MAGENTA) Project: Participants include 465 individuals (AA – 113 with AD, 118 cognitively intact controls; NHW – 116 with AD, 118 controls) ascertained by the John P. Hussman Institute for Human Genomics (HIHG) at the University of Miami Miller School of Medicine (Miami, FL), North Carolina A&T State University (Greensboro, NC), and Case Western Reserve University (Cleveland, OH).  Participants were ascertained as part of the ADSP Follow-up Study and included both cases (>65 years of age of onset) and controls (>65 years of age at age of exam).  All participants were adjudicated by a clinical panel with expertise in AD related disorders and classified as AD according to standard criteria developed by the National Institute of Aging and the Alzheimer’s Association. 

## Contact

Makaela Mews (analyst); Dr. William S. Bush (wsb36@case.edu);  Dr. Anthony J. Griswold (Griswold, Anthony J agriswold@miami.edu) 

## Study Overview

- Study information: `study_info/MAGENTA.md`. 

## Dataset Details

### Raw data

URL to original data, if applicable:

- TO ADD: https://dss.niagads.org/datasets/... 

Path(s) on HPC:

- Bush Lab - Raw Genotypes, server: aneris-dev.case.edu `/storage2/BushLab/transfer/miami/AfricanAmerican`
- Bush Lab - Imputed Genotypes, server: aneris-dev.case.edu `/storage2/BushLab/transfer/miami/TPMs/revised_01_12_23/aa/imputed_geno`
- Bush Lab - Analysis, server: rider.case.edu `/mnt/pan/Data14/metabrain_lasso/rna_seq_norm/aa_233`

Summary of Raw Genotypes: 

```
$  ls -lh
total 53M
-rw-r--r-- 1 wsb36 users  35M Oct 19 07:39 aa_all.bed
-rw-r--r-- 1 wsb36 users  19M Oct 19 07:39 aa_all.bim
-rw-r--r-- 1 wsb36 users 3.8K Oct 19 07:39 aa_all.fam
-rw-r--r-- 1 wsb36 users 2.0K Oct 19 07:39 all_AA_plink.txt
-rw-r--r-- 1 wsb36 users  924 Oct 19 07:39 case_AA_plink.txt
-rw-r--r-- 1 wsb36 users 1.1K Oct 19 07:39 con_AA_plink.txt

```

Summary of Imputed Genotypes:

```
$ ls -lh
total 26G
-rwxrwxr-x 1 mxm1368 mxm1368 1.3G Feb  6 10:14 chr10.dose.vcf.gz
-rwxrwxr-x 1 mxm1368 mxm1368  21M Feb  6 10:14 chr10.info.gz
-rwxrwxr-x 1 mxm1368 mxm1368 1.4K Feb  6 10:14 chr_10.log
-rwxrwxr-x 1 mxm1368 mxm1368 1.2G Feb  6 10:14 chr11.dose.vcf.gz
-rwxrwxr-x 1 mxm1368 mxm1368  20M Feb  6 10:14 chr11.info.gz
-rwxrwxr-x 1 mxm1368 mxm1368 1.4K Feb  6 10:14 chr_11.log
-rwxrwxr-x 1 mxm1368 mxm1368 1.2G Feb  6 10:15 chr12.dose.vcf.gz
-rwxrwxr-x 1 mxm1368 mxm1368  20M Feb  6 10:15 chr12.info.gz
-rwxrwxr-x 1 mxm1368 mxm1368 1.4K Feb  6 10:15 chr_12.log
-rwxrwxr-x 1 mxm1368 mxm1368 888M Feb  6 10:15 chr13.dose.vcf.gz
-rwxrwxr-x 1 mxm1368 mxm1368  15M Feb  6 10:15 chr13.info.gz
-rwxrwxr-x 1 mxm1368 mxm1368 1.2K Feb  6 10:15 chr_13.log
-rwxrwxr-x 1 mxm1368 mxm1368 826M Feb  6 10:15 chr14.dose.vcf.gz
-rwxrwxr-x 1 mxm1368 mxm1368  14M Feb  6 10:15 chr14.info.gz
-rwxrwxr-x 1 mxm1368 mxm1368  997 Feb  6 10:15 chr_14.log
-rwxrwxr-x 1 mxm1368 mxm1368 723M Feb  6 10:15 chr15.dose.vcf.gz
-rwxrwxr-x 1 mxm1368 mxm1368  12M Feb  6 10:15 chr15.info.gz
-rwxrwxr-x 1 mxm1368 mxm1368  997 Feb  6 10:15 chr_15.log
-rwxrwxr-x 1 mxm1368 mxm1368 801M Feb  6 10:15 chr16.dose.vcf.gz
-rwxrwxr-x 1 mxm1368 mxm1368  14M Feb  6 10:15 chr16.info.gz
-rwxrwxr-x 1 mxm1368 mxm1368  998 Feb  6 10:15 chr_16.log
-rwxrwxr-x 1 mxm1368 mxm1368 739M Feb  6 10:15 chr17.dose.vcf.gz
-rwxrwxr-x 1 mxm1368 mxm1368  12M Feb  6 10:15 chr17.info.gz
-rwxrwxr-x 1 mxm1368 mxm1368  995 Feb  6 10:15 chr_17.log
-rwxrwxr-x 1 mxm1368 mxm1368 743M Feb  6 10:15 chr18.dose.vcf.gz
-rwxrwxr-x 1 mxm1368 mxm1368  12M Feb  6 10:15 chr18.info.gz
-rwxrwxr-x 1 mxm1368 mxm1368  798 Feb  6 10:15 chr_18.log
-rwxrwxr-x 1 mxm1368 mxm1368 640M Feb  6 10:15 chr19.dose.vcf.gz
-rwxrwxr-x 1 mxm1368 mxm1368 9.1M Feb  6 10:15 chr19.info.gz
-rwxrwxr-x 1 mxm1368 mxm1368  598 Feb  6 10:15 chr_19.log
-rwxrwxr-x 1 mxm1368 mxm1368 2.0G Feb  6 10:15 chr1.dose.vcf.gz
-rwxrwxr-x 1 mxm1368 mxm1368  33M Feb  6 10:15 chr1.info.gz
-rwxrwxr-x 1 mxm1368 mxm1368 2.5K Feb  6 10:15 chr_1.log
-rwxrwxr-x 1 mxm1368 mxm1368 582M Feb  6 10:16 chr20.dose.vcf.gz
-rwxrwxr-x 1 mxm1368 mxm1368 9.5M Feb  6 10:16 chr20.info.gz
-rwxrwxr-x 1 mxm1368 mxm1368  796 Feb  6 10:16 chr_20.log
-rwxrwxr-x 1 mxm1368 mxm1368 379M Feb  6 10:16 chr21.dose.vcf.gz
-rwxrwxr-x 1 mxm1368 mxm1368 5.8M Feb  6 10:16 chr21.info.gz
-rwxrwxr-x 1 mxm1368 mxm1368  597 Feb  6 10:16 chr_21.log
-rwxrwxr-x 1 mxm1368 mxm1368 354M Feb  6 10:16 chr22.dose.vcf.gz
-rwxrwxr-x 1 mxm1368 mxm1368 5.4M Feb  6 10:16 chr22.info.gz
-rwxrwxr-x 1 mxm1368 mxm1368  596 Feb  6 10:16 chr_22.log
-rwxrwxr-x 1 mxm1368 mxm1368 2.2G Feb  6 10:16 chr2.dose.vcf.gz
-rwxrwxr-x 1 mxm1368 mxm1368  36M Feb  6 10:16 chr2.info.gz
-rwxrwxr-x 1 mxm1368 mxm1368 2.5K Feb  6 10:16 chr_2.log
-rwxrwxr-x 1 mxm1368 mxm1368 1.9G Feb  6 10:16 chr3.dose.vcf.gz
-rwxrwxr-x 1 mxm1368 mxm1368  30M Feb  6 10:16 chr3.info.gz
-rwxrwxr-x 1 mxm1368 mxm1368 2.0K Feb  6 10:16 chr_3.log
-rwxrwxr-x 1 mxm1368 mxm1368 2.0G Feb  6 10:16 chr4.dose.vcf.gz
-rwxrwxr-x 1 mxm1368 mxm1368  30M Feb  6 10:16 chr4.info.gz
-rwxrwxr-x 1 mxm1368 mxm1368 2.0K Feb  6 10:16 chr_4.log
-rwxrwxr-x 1 mxm1368 mxm1368 1.8G Feb  6 10:17 chr5.dose.vcf.gz
-rwxrwxr-x 1 mxm1368 mxm1368  28M Feb  6 10:17 chr5.info.gz
-rwxrwxr-x 1 mxm1368 mxm1368 2.0K Feb  6 10:17 chr_5.log
-rwxrwxr-x 1 mxm1368 mxm1368 1.6G Feb  6 10:17 chr6.dose.vcf.gz
-rwxrwxr-x 1 mxm1368 mxm1368  27M Feb  6 10:17 chr6.info.gz
-rwxrwxr-x 1 mxm1368 mxm1368 1.8K Feb  6 10:17 chr_6.log
-rwxrwxr-x 1 mxm1368 mxm1368 1.5G Feb  6 10:17 chr7.dose.vcf.gz
-rwxrwxr-x 1 mxm1368 mxm1368  24M Feb  6 10:17 chr7.info.gz
-rwxrwxr-x 1 mxm1368 mxm1368 1.6K Feb  6 10:17 chr_7.log
-rwxrwxr-x 1 mxm1368 mxm1368 1.5G Feb  6 10:17 chr8.dose.vcf.gz
-rwxrwxr-x 1 mxm1368 mxm1368  24M Feb  6 10:17 chr8.info.gz
-rwxrwxr-x 1 mxm1368 mxm1368 1.6K Feb  6 10:17 chr_8.log
-rwxrwxr-x 1 mxm1368 mxm1368 1.1G Feb  6 10:17 chr9.dose.vcf.gz
-rwxrwxr-x 1 mxm1368 mxm1368  18M Feb  6 10:17 chr9.info.gz
-rwxrwxr-x 1 mxm1368 mxm1368 1.4K Feb  6 10:17 chr_9.log
-rwxrwxr-x 1 mxm1368 mxm1368 808K Feb  6 10:17 qcreport.html

```

### Molecular phenotype matrices

Path(s) on HPC:

- Bush Lab - Raw Gene Reads/TPMs, server: aneris-dev.case.edu `/storage2/BushLab/transfer/miami/TPMs/revised_01_12_23/aa`
- Bush Lab - Analysis, server: rider.case.edu `/mnt/pan/Data14/metabrain_lasso/rna_seq_norm/aa_233`

A description of these matrices:

- Raw Gene Reads/TPMs: 1st row is version (e.g., #1.2), 2nd row dimensions of file in terms of # genes x # samples (e.g., 60668   233), 3rd row Column Names (e.g., Name  Description   SAMPLE...), 4th+ row gene values (e.g., ENSG00000223972 DDX11L1 0 ...)

- Analysis Reads/TPMs: see `aa_miami_eQTL_phenotype.ipynb` for processing of raw gene reads/TPMs into analysis ready reads/TPMs; format: columns (e.g., gene_ID, SAMPLE...), rows (e.g., ENSG00000223972 0...)

```
$ cd /mnt/pan/Data14/metabrain_lasso/rna_seq_norm/aa_233

# Number of rows: 
$ wc -l aa_233_gene_reads_prep_v2.gct
60669 aa_233_gene_reads_prep_v2.gct
$ wc -l aa_233_gene_tpm_prep_v2.gct
60669 aa_233_gene_tpm_prep_v2.gct

# Number of columns:
$ awk '{print NF}' aa_233_gene_reads_prep_v2.gct | sort -n | uniq
234
$ awk '{print NF}' aa_233_gene_tpm_prep_v2.gct | sort -n | uniq
234

```

### Other key data files

Path(s) on HPC:

- Bush Lab - Covariate data, server: rider.case.edu `/mnt/pan/Data14/metabrain_lasso/rna_seq_norm/AANHW_updated_472_RNA.csv`

```
$ head -1 AANHW_updated_472_RNA.csv
ID,cohort,Sex,APOE,AD_Control,age_of_onset,age_of_exam,SAMPLE
$ wc -l AANHW_updated_472_RNA.csv
475 AANHW_updated_472_RNA.csv

```

- Path(s) to the data on your local cluster where you analyzed the data. For example:
- Bush Lab, `/mnt/pan/Data14/metabrain_lasso/rna_seq_norm/aa_233`

## Links to omics data analysis notebooks

Please list links to the analysis in the order you performed them:

1. Molecular Phenotype Processing: `magenta_aa_eqtl_phenotype_processing.ipynb`
2. Covariate Processing: `magenta_aa_eqtl_covariate_processing.ipynb`
3. Genotype Processing: `magenta_aa_eqtl_genotype_processing.ipynb`
4. TensorQTL - cis & trans: `magenta_aa_eqtl_tensorqtl.ipynb`
5. Complete Analysis Protocol: `magenta_aa_eqtl_complete_analysis.ipynb`
