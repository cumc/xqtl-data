# Knight ADRC genotype data

## Contact

Zining Qi

## Data Descriptions

### Raw genotype files
MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.bed, MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.bim (N= 10,641,345), MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.fam (N= 441)were the plink set created by extracting the Washu samples using geno = 0.1 and Maf = 0.0005 filters, Which then was checked for the array duplication.
If there are duplicate samples (by array) in the data they will be filtered basing on their missingness and array frequency information.

Data provided is on GRCH38 genome build. We used TOPMED reference panel for imputation. The IDs in the fam were in the PA_DB_UID format .
Bim file follows Chr:SNP:Ref:Alt format for snp name and the Ref is set to A2 allele in the plink file.
Array information of all the samples was enclosed in the file: ID_Array_info.txt

Detailed QC steps used to process the data can be viewed in file:
Imputation QC protocol.pdf

- Data Location on CU cluster:

```
/mnt/vast/hpc/csg/ftp_lisanwanglab_sync/ftp_fgc_xqtl/projects/SNParrayGeno/knightadrc-washu$ ls -lh
-rw-r--r-- 1 xc2610 root 184K Nov 29 13:35 'Imputation QC protocol.pdf'
-rw-r--r-- 1 xc2610 root 1.2G Nov 29 13:36  MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.bed
-rw-r--r-- 1 xc2610 root 372M Nov 29 13:36  MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.bim
-rw-r--r-- 1 xc2610 root  14K Nov 29 13:36  MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.fam
-rw-r--r-- 1 xc2610 root 1.1K Nov 29 13:36  MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.log
-rw-r--r-- 1 xc2610 root  959 Nov 29 13:36  README.txt
```

- Data Location on FTP:

`ftp_fgc_xqtl/projects/SNParrayGeno/knightadrc-washu/`

### Genotype processed via xQTL pipeline:

For details how the phenotype data is processed please check [genotype_preprocessing](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/knight/pqtl/genotype_preprocessing.ipynb)

- Data Location on CU cluster: `/mnt/mfs/hgrcgrid/homes/zq2209/proteomics/knight/MAP_Brain-xQTL_Gwas_geno_0.1_maf_0.0005.plink_files_list.txt`