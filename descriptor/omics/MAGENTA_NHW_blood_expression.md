#  MAGENTA Non-Hispanic White blood gene expression

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

- Bush Lab - Raw Genotypes, server: aneris-dev.case.edu `/storage2/BushLab/transfer/miami/NonHispanicWhite`
- Bush Lab - Imputed Genotypes, server: aneris-dev.case.edu `/storage2/BushLab/transfer/resources/mea_eqtl/post_imp/vcf/dose/nhw`
- Bush Lab - Analysis, server: rider.case.edu `/mnt/pan/Data14/metabrain_lasso/rna_seq_norm/nhw_239`

Summary of Raw Genotypes: 

```
$ ls -lh
total 55M
-rw-r--r-- 1 wsb36 users 1.9K Oct 19 07:39 all_NHW_plink.txt
-rw-r--r-- 1 wsb36 users  894 Oct 19 07:39 case_NHW_plink.txt
-rw-r--r-- 1 wsb36 users 1018 Oct 19 07:39 con_NHW_plink.txt
-rw-r--r-- 1 wsb36 users  37M Oct 19 07:39 nhw_all.bed
-rw-r--r-- 1 wsb36 users  19M Oct 19 07:39 nhw_all.bim
-rw-r--r-- 1 wsb36 users 3.8K Oct 19 07:39 nhw_all.fam


```

Summary of Imputed Genotypes:

```
$ ls -lh
total 279G
-rw-r--r-- 1 wsb36 users  147 Jul 14  2022 gunzip_it.py
-rw-r--r-- 1 wsb36 users  14G Jul 14  2022 nhw_chr10.dose.vcf
-rw-r--r-- 1 wsb36 users  14G Jul 14  2022 nhw_chr11.dose.vcf
-rw-r--r-- 1 wsb36 users  14G Jul 14  2022 nhw_chr12.dose.vcf
-rw-r--r-- 1 wsb36 users 9.9G Jul 14  2022 nhw_chr13.dose.vcf
-rw-r--r-- 1 wsb36 users 8.8G Jul 14  2022 nhw_chr14.dose.vcf
-rw-r--r-- 1 wsb36 users 8.5G Jul 14  2022 nhw_chr15.dose.vcf
-rw-r--r-- 1 wsb36 users 9.6G Jul 14  2022 nhw_chr16.dose.vcf
-rw-r--r-- 1 wsb36 users 8.5G Jul 14  2022 nhw_chr17.dose.vcf
-rw-r--r-- 1 wsb36 users 8.0G Jul 14  2022 nhw_chr18.dose.vcf
-rw-r--r-- 1 wsb36 users 6.7G Jul 14  2022 nhw_chr19.dose.vcf
-rw-r--r-- 1 wsb36 users  23G Jul 14  2022 nhw_chr1.dose.vcf
-rw-r--r-- 1 wsb36 users 6.6G Jul 14  2022 nhw_chr20.dose.vcf
-rw-r--r-- 1 wsb36 users 4.0G Jul 14  2022 nhw_chr21.dose.vcf
-rw-r--r-- 1 wsb36 users 4.3G Jul 14  2022 nhw_chr22.dose.vcf
-rw-r--r-- 1 wsb36 users  24G Jul 14  2022 nhw_chr2.dose.vcf
-rw-r--r-- 1 wsb36 users  20G Jul 14  2022 nhw_chr3.dose.vcf
-rw-r--r-- 1 wsb36 users  20G Jul 14  2022 nhw_chr4.dose.vcf
-rw-r--r-- 1 wsb36 users  19G Jul 14  2022 nhw_chr5.dose.vcf
-rw-r--r-- 1 wsb36 users  17G Jul 14  2022 nhw_chr6.dose.vcf
-rw-r--r-- 1 wsb36 users  17G Jul 14  2022 nhw_chr7.dose.vcf
-rw-r--r-- 1 wsb36 users  16G Jul 14  2022 nhw_chr8.dose.vcf
-rw-r--r-- 1 wsb36 users  13G Jul 14  2022 nhw_chr9.dose.vcf


```

### Molecular phenotype matrices

Path(s) on HPC:

- Bush Lab - Raw Gene Reads/TPMs, server: aneris-dev.case.edu `/storage2/BushLab/transfer/miami/TPMs/revised_01_12_23/nhw`
- Bush Lab - Analysis, server: rider.case.edu `/mnt/pan/Data14/metabrain_lasso/rna_seq_norm/nhw_239/mol_phe`

A description of these matrices:

- Raw Gene Reads/TPMs: 1st row is version (e.g., #1.2), 2nd row dimensions of file in terms of # genes x # samples (e.g., 60668   233), 3rd row Column Names (e.g., Name  Description   SAMPLE...), 4th+ row gene values (e.g., ENSG00000223972 DDX11L1 0 ...)

- Analysis Reads/TPMs: see `magenta_nhw_eqtl_phenotype_processing.ipynb` for processing of raw gene reads/TPMs into analysis ready reads/TPMs; format: columns (e.g., gene_ID, SAMPLE...), rows (e.g., ENSG00000223972 0...)

```
$ cd /mnt/pan/Data14/metabrain_lasso/rna_seq_norm/nhw_239/mol_phe

# Number of rows: 
$ wc -l nhw_gene_reads_prep_v2.gct
60669 nhw_gene_reads_prep_v2.gct
$ wc -l nhw_gene_tpm_prep_v2.gct
60669 nhw_gene_tpm_prep_v2.gct

# Number of columns:
$ awk '{print NF}' nhw_gene_reads_prep_v2.gct | sort -n | uniq
240
$ awk '{print NF}' nhw_gene_tpm_prep_v2.gct | sort -n | uniq
240

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
- Bush Lab, `/mnt/pan/Data14/metabrain_lasso/rna_seq_norm/nhw_239`

## Links to omics data analysis notebooks

Please list links to the analysis in the order you performed them:

1. Molecular Phenotype Processing: `magenta_nhw_eqtl_phenotype_processing.ipynb`
2. Covariate Processing: `magenta_nhw_eqtl_covariate_processing.ipynb`
3. Genotype Processing: `magenta_nhw_eqtl_genotype_processing.ipynb`
4. TensorQTL - cis & trans: `magenta_nhw_eqtl_tensorqtl.ipynb`
5. Complete Analysis Protocol: `magenta_nhw_eqtl_complete_analysis.ipynb`
