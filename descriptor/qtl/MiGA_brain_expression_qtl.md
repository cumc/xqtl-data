# MiGA multi-brain region gene expression QTL

A genetic and transcriptomic resource comprised of 255 primary human microglia samples isolated ex vivo from four different brain regions of 100 human subjects with neurodegenerative, neurological, or neuropsychiatric disorders, as well as unaffected controls.

Microglia Genomic Atlas from the Netherlands Brain Bank (NBB) and the Neuropathology Brain Bank and Research CoRE at Mount Sinai Hospital. The permission to collect human brain material was obtained from the Ethical Committee of the VU University Medical Center, Amsterdam, The Netherlands, and the Mount Sinai Institutional Review Board. For the Netherlands Brain bank, informed consent for autopsy, the use of brain tissue and accompanied clinical information for research purposes was obtained per donor ante-mortem.

Please refer to [this document](https://github.com/cumc/xqtl-data/blob/main/descriptor/study_info/MiGA.md) for an overview of the MiGA project.
## Contact

Travyse Edwards

## Study Overview

- Sample information: `MiGA/MiGA_brain_expression_sample_attributes.csv`.
sample size calculated from the phenotype data on cloud
| Cohort | Sample Size |
|--------|-------------|
| GFM    | 74          |
| GTS    | 62          |
| SVZ    | 52          |
| THA    | 60          |

- Lab protocol: `MiGA/MiGA_brain_expression_lab_protocol.csv`.
- Computational protocol: `MiGA/MiGA_brain_expression_computational_protocol.csv`.
- Medial Frontal Gyrus QTL summary statistics output:  
  - Path on Minerva: `/sc/arion/projects/load/users/edwart10/projects/12-19-2022-MiGA-Replication/output/age_sex/12-19-2022/association_scan/GFM/TensorQTL/5N/`.
- Superior Temporal Gyrus QTL summary statistics output:  
  - Path on Minerva: `/sc/arion/projects/load/users/edwart10/projects/12-19-2022-MiGA-Replication/output/age_sex/12-19-2022/association_scan/GTS/TensorQTL/5N/`.
- Thalamus QTL summary statistics output:  
  - Path on Minerva: `/sc/arion/projects/load/users/edwart10/projects/12-19-2022-MiGA-Replication/output/age_sex/12-19-2022/association_scan/THA/TensorQTL/5N/`.
- Subventricular Zone QTL summary statistics output:  
  - Path on Minerva: `/sc/arion/projects/load/users/edwart10/projects/12-19-2022-MiGA-Replication/output/age_sex/12-19-2022/association_scan/SVZ/TensorQTL/5N/`.
- Fine-mapping results individual level data model: TBD.
- Fine-mapping results summary statistics model: TBD.

## Analysis Status
TransQTL association: Need to be performed.

## Dataset Details

### Path(s) to genotype matrix

- Path to genotype list: /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.final.plink_files_list.txt
- Path to genotype directory: /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/

```
lrwxrwxrwx 1 edwart10 LOAD 207 Oct 14 21:05 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.genotype.chr10.bed -> /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/genotype_per_chrom/raj_microglia_anno.MAF.leftnorm.snp.filtered.filtered.for_pca.filtered.no_outlier.filtered.10.bed
lrwxrwxrwx 1 edwart10 LOAD 207 Oct 14 21:05 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.genotype.chr11.bed -> /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/genotype_per_chrom/raj_microglia_anno.MAF.leftnorm.snp.filtered.filtered.for_pca.filtered.no_outlier.filtered.11.bed
lrwxrwxrwx 1 edwart10 LOAD 207 Oct 14 21:05 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.genotype.chr12.bed -> /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/genotype_per_chrom/raj_microglia_anno.MAF.leftnorm.snp.filtered.filtered.for_pca.filtered.no_outlier.filtered.12.bed
lrwxrwxrwx 1 edwart10 LOAD 207 Oct 14 21:05 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.genotype.chr13.bed -> /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/genotype_per_chrom/raj_microglia_anno.MAF.leftnorm.snp.filtered.filtered.for_pca.filtered.no_outlier.filtered.13.bed
lrwxrwxrwx 1 edwart10 LOAD 207 Oct 14 21:05 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.genotype.chr14.bed -> /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/genotype_per_chrom/raj_microglia_anno.MAF.leftnorm.snp.filtered.filtered.for_pca.filtered.no_outlier.filtered.14.bed
lrwxrwxrwx 1 edwart10 LOAD 207 Oct 14 21:05 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.genotype.chr15.bed -> /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/genotype_per_chrom/raj_microglia_anno.MAF.leftnorm.snp.filtered.filtered.for_pca.filtered.no_outlier.filtered.15.bed
lrwxrwxrwx 1 edwart10 LOAD 207 Oct 14 21:05 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.genotype.chr16.bed -> /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/genotype_per_chrom/raj_microglia_anno.MAF.leftnorm.snp.filtered.filtered.for_pca.filtered.no_outlier.filtered.16.bed
lrwxrwxrwx 1 edwart10 LOAD 207 Oct 14 21:05 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.genotype.chr17.bed -> /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/genotype_per_chrom/raj_microglia_anno.MAF.leftnorm.snp.filtered.filtered.for_pca.filtered.no_outlier.filtered.17.bed
lrwxrwxrwx 1 edwart10 LOAD 207 Oct 14 21:05 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.genotype.chr18.bed -> /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/genotype_per_chrom/raj_microglia_anno.MAF.leftnorm.snp.filtered.filtered.for_pca.filtered.no_outlier.filtered.18.bed
lrwxrwxrwx 1 edwart10 LOAD 207 Oct 14 21:05 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.genotype.chr19.bed -> /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/genotype_per_chrom/raj_microglia_anno.MAF.leftnorm.snp.filtered.filtered.for_pca.filtered.no_outlier.filtered.19.bed
lrwxrwxrwx 1 edwart10 LOAD 206 Oct 14 21:05 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.genotype.chr1.bed -> /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/genotype_per_chrom/raj_microglia_anno.MAF.leftnorm.snp.filtered.filtered.for_pca.filtered.no_outlier.filtered.1.bed
lrwxrwxrwx 1 edwart10 LOAD 207 Oct 14 21:05 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.genotype.chr20.bed -> /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/genotype_per_chrom/raj_microglia_anno.MAF.leftnorm.snp.filtered.filtered.for_pca.filtered.no_outlier.filtered.20.bed
lrwxrwxrwx 1 edwart10 LOAD 207 Oct 14 21:05 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.genotype.chr21.bed -> /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/genotype_per_chrom/raj_microglia_anno.MAF.leftnorm.snp.filtered.filtered.for_pca.filtered.no_outlier.filtered.21.bed
lrwxrwxrwx 1 edwart10 LOAD 207 Oct 14 21:05 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.genotype.chr22.bed -> /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/genotype_per_chrom/raj_microglia_anno.MAF.leftnorm.snp.filtered.filtered.for_pca.filtered.no_outlier.filtered.22.bed
lrwxrwxrwx 1 edwart10 LOAD 206 Oct 14 21:05 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.genotype.chr2.bed -> /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/genotype_per_chrom/raj_microglia_anno.MAF.leftnorm.snp.filtered.filtered.for_pca.filtered.no_outlier.filtered.2.bed
lrwxrwxrwx 1 edwart10 LOAD 206 Oct 14 21:05 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.genotype.chr3.bed -> /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/genotype_per_chrom/raj_microglia_anno.MAF.leftnorm.snp.filtered.filtered.for_pca.filtered.no_outlier.filtered.3.bed
lrwxrwxrwx 1 edwart10 LOAD 206 Oct 14 21:05 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.genotype.chr4.bed -> /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/genotype_per_chrom/raj_microglia_anno.MAF.leftnorm.snp.filtered.filtered.for_pca.filtered.no_outlier.filtered.4.bed
lrwxrwxrwx 1 edwart10 LOAD 206 Oct 14 21:05 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.genotype.chr5.bed -> /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/genotype_per_chrom/raj_microglia_anno.MAF.leftnorm.snp.filtered.filtered.for_pca.filtered.no_outlier.filtered.5.bed
lrwxrwxrwx 1 edwart10 LOAD 206 Oct 14 21:05 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.genotype.chr6.bed -> /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/genotype_per_chrom/raj_microglia_anno.MAF.leftnorm.snp.filtered.filtered.for_pca.filtered.no_outlier.filtered.6.bed
lrwxrwxrwx 1 edwart10 LOAD 206 Oct 14 21:05 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.genotype.chr7.bed -> /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/genotype_per_chrom/raj_microglia_anno.MAF.leftnorm.snp.filtered.filtered.for_pca.filtered.no_outlier.filtered.7.bed
lrwxrwxrwx 1 edwart10 LOAD 206 Oct 14 21:05 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.genotype.chr8.bed -> /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/genotype_per_chrom/raj_microglia_anno.MAF.leftnorm.snp.filtered.filtered.for_pca.filtered.no_outlier.filtered.8.bed
lrwxrwxrwx 1 edwart10 LOAD 206 Oct 14 21:05 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.genotype.chr9.bed -> /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/genotype_per_chrom/raj_microglia_anno.MAF.leftnorm.snp.filtered.filtered.for_pca.filtered.no_outlier.filtered.9.bed
```

### Path(s) to omics-data matrix

- Medial Frontal Gyrus
  - Path to Phenotype List File: `/sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.GFM.final.recipe`
  - Path to Phenotype Directory: `/sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/`
- Superior Temporal Gyrus
  - Path to Phenotype List File: `/sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.GTS.final.recipe`
  - Path to Phenotype Directory: `/sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/`
- Thalamus
  - Path to Phenotype List File: `/sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.THA.final.recipe`
  - Path to Phenotype Directory: `/sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/`
- Subventricular Zone
  - Path to Phenotype List File: `/sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.SVZ.final.recipe`
  - Path to Phenotype Directory: `/sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/`

```
-rw-r--r-- 1 edwart10 LOAD 217K Sep 30 11:47 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GFM.chr10.bed.gz
-rw-r--r-- 1 edwart10 LOAD 313K Sep 30 11:47 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GFM.chr11.bed.gz
-rw-r--r-- 1 edwart10 LOAD 288K Sep 30 11:47 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GFM.chr12.bed.gz
-rw-r--r-- 1 edwart10 LOAD 121K Sep 30 11:47 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GFM.chr13.bed.gz
-rw-r--r-- 1 edwart10 LOAD 179K Sep 30 11:47 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GFM.chr14.bed.gz
-rw-r--r-- 1 edwart10 LOAD 187K Sep 30 11:47 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GFM.chr15.bed.gz
-rw-r--r-- 1 edwart10 LOAD 238K Sep 30 11:47 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GFM.chr16.bed.gz
-rw-r--r-- 1 edwart10 LOAD 288K Sep 30 11:47 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GFM.chr17.bed.gz
-rw-r--r-- 1 edwart10 LOAD 105K Sep 30 11:47 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GFM.chr18.bed.gz
-rw-r--r-- 1 edwart10 LOAD 306K Sep 30 11:47 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GFM.chr19.bed.gz
-rw-r--r-- 1 edwart10 LOAD 521K Sep 30 11:47 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GFM.chr1.bed.gz
-rw-r--r-- 1 edwart10 LOAD 131K Sep 30 11:47 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GFM.chr20.bed.gz
-rw-r--r-- 1 edwart10 LOAD  67K Sep 30 11:47 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GFM.chr21.bed.gz
-rw-r--r-- 1 edwart10 LOAD 120K Sep 30 11:47 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GFM.chr22.bed.gz
-rw-r--r-- 1 edwart10 LOAD 365K Sep 30 11:47 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GFM.chr2.bed.gz
-rw-r--r-- 1 edwart10 LOAD 303K Sep 30 11:47 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GFM.chr3.bed.gz
-rw-r--r-- 1 edwart10 LOAD 232K Sep 30 11:47 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GFM.chr4.bed.gz
-rw-r--r-- 1 edwart10 LOAD 263K Sep 30 11:47 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GFM.chr5.bed.gz
-rw-r--r-- 1 edwart10 LOAD 302K Sep 30 11:47 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GFM.chr6.bed.gz
-rw-r--r-- 1 edwart10 LOAD 260K Sep 30 11:47 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GFM.chr7.bed.gz
-rw-r--r-- 1 edwart10 LOAD 216K Sep 30 11:47 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GFM.chr8.bed.gz
-rw-r--r-- 1 edwart10 LOAD 210K Sep 30 11:47 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GFM.chr9.bed.gz
-rw-r--r-- 1 edwart10 LOAD 181K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GTS.chr10.bed.gz
-rw-r--r-- 1 edwart10 LOAD 258K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GTS.chr11.bed.gz
-rw-r--r-- 1 edwart10 LOAD 237K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GTS.chr12.bed.gz
-rw-r--r-- 1 edwart10 LOAD 100K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GTS.chr13.bed.gz
-rw-r--r-- 1 edwart10 LOAD 146K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GTS.chr14.bed.gz
-rw-r--r-- 1 edwart10 LOAD 152K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GTS.chr15.bed.gz
-rw-r--r-- 1 edwart10 LOAD 195K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GTS.chr16.bed.gz
-rw-r--r-- 1 edwart10 LOAD 238K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GTS.chr17.bed.gz
-rw-r--r-- 1 edwart10 LOAD  86K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GTS.chr18.bed.gz
-rw-r--r-- 1 edwart10 LOAD 252K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GTS.chr19.bed.gz
-rw-r--r-- 1 edwart10 LOAD 428K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GTS.chr1.bed.gz
-rw-r--r-- 1 edwart10 LOAD 108K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GTS.chr20.bed.gz
-rw-r--r-- 1 edwart10 LOAD  54K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GTS.chr21.bed.gz
-rw-r--r-- 1 edwart10 LOAD 100K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GTS.chr22.bed.gz
-rw-r--r-- 1 edwart10 LOAD 298K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GTS.chr2.bed.gz
-rw-r--r-- 1 edwart10 LOAD 252K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GTS.chr3.bed.gz
-rw-r--r-- 1 edwart10 LOAD 191K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GTS.chr4.bed.gz
-rw-r--r-- 1 edwart10 LOAD 216K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GTS.chr5.bed.gz
-rw-r--r-- 1 edwart10 LOAD 248K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GTS.chr6.bed.gz
-rw-r--r-- 1 edwart10 LOAD 213K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GTS.chr7.bed.gz
-rw-r--r-- 1 edwart10 LOAD 177K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GTS.chr8.bed.gz
-rw-r--r-- 1 edwart10 LOAD 172K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.GTS.chr9.bed.gz
-rw-r--r-- 1 edwart10 LOAD 136K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.SVZ.chr10.bed.gz
-rw-r--r-- 1 edwart10 LOAD 182K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.SVZ.chr11.bed.gz
-rw-r--r-- 1 edwart10 LOAD 176K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.SVZ.chr12.bed.gz
-rw-r--r-- 1 edwart10 LOAD  71K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.SVZ.chr13.bed.gz
-rw-r--r-- 1 edwart10 LOAD 109K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.SVZ.chr14.bed.gz
-rw-r--r-- 1 edwart10 LOAD 113K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.SVZ.chr15.bed.gz
-rw-r--r-- 1 edwart10 LOAD 147K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.SVZ.chr16.bed.gz
-rw-r--r-- 1 edwart10 LOAD 183K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.SVZ.chr17.bed.gz
-rw-r--r-- 1 edwart10 LOAD  63K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.SVZ.chr18.bed.gz
-rw-r--r-- 1 edwart10 LOAD 191K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.SVZ.chr19.bed.gz
-rw-r--r-- 1 edwart10 LOAD 324K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.SVZ.chr1.bed.gz
-rw-r--r-- 1 edwart10 LOAD  81K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.SVZ.chr20.bed.gz
-rw-r--r-- 1 edwart10 LOAD  39K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.SVZ.chr21.bed.gz
-rw-r--r-- 1 edwart10 LOAD  74K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.SVZ.chr22.bed.gz
-rw-r--r-- 1 edwart10 LOAD 219K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.SVZ.chr2.bed.gz
-rw-r--r-- 1 edwart10 LOAD 187K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.SVZ.chr3.bed.gz
-rw-r--r-- 1 edwart10 LOAD 135K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.SVZ.chr4.bed.gz
-rw-r--r-- 1 edwart10 LOAD 157K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.SVZ.chr5.bed.gz
-rw-r--r-- 1 edwart10 LOAD 184K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.SVZ.chr6.bed.gz
-rw-r--r-- 1 edwart10 LOAD 158K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.SVZ.chr7.bed.gz
-rw-r--r-- 1 edwart10 LOAD 130K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.SVZ.chr8.bed.gz
-rw-r--r-- 1 edwart10 LOAD 125K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.SVZ.chr9.bed.gz
-rw-r--r-- 1 edwart10 LOAD 175K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.THA.chr10.bed.gz
-rw-r--r-- 1 edwart10 LOAD 249K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.THA.chr11.bed.gz
-rw-r--r-- 1 edwart10 LOAD 231K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.THA.chr12.bed.gz
-rw-r--r-- 1 edwart10 LOAD  98K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.THA.chr13.bed.gz
-rw-r--r-- 1 edwart10 LOAD 144K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.THA.chr14.bed.gz
-rw-r--r-- 1 edwart10 LOAD 149K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.THA.chr15.bed.gz
-rw-r--r-- 1 edwart10 LOAD 188K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.THA.chr16.bed.gz
-rw-r--r-- 1 edwart10 LOAD 231K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.THA.chr17.bed.gz
-rw-r--r-- 1 edwart10 LOAD  85K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.THA.chr18.bed.gz
-rw-r--r-- 1 edwart10 LOAD 242K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.THA.chr19.bed.gz
-rw-r--r-- 1 edwart10 LOAD 419K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.THA.chr1.bed.gz
-rw-r--r-- 1 edwart10 LOAD 106K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.THA.chr20.bed.gz
-rw-r--r-- 1 edwart10 LOAD  53K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.THA.chr21.bed.gz
-rw-r--r-- 1 edwart10 LOAD  95K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.THA.chr22.bed.gz
-rw-r--r-- 1 edwart10 LOAD 291K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.THA.chr2.bed.gz
-rw-r--r-- 1 edwart10 LOAD 244K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.THA.chr3.bed.gz
-rw-r--r-- 1 edwart10 LOAD 187K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.THA.chr4.bed.gz
-rw-r--r-- 1 edwart10 LOAD 211K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.THA.chr5.bed.gz
-rw-r--r-- 1 edwart10 LOAD 242K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.THA.chr6.bed.gz
-rw-r--r-- 1 edwart10 LOAD 209K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.THA.chr7.bed.gz
-rw-r--r-- 1 edwart10 LOAD 174K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.THA.chr8.bed.gz
-rw-r--r-- 1 edwart10 LOAD 168K Sep 30 11:48 /sc/arion/projects/load/users/edwart10/projects/09-07-2022-MiGA-Analysis/output/10-14-2022/association_scan/finalized-input-files/miga.phenotype.THA.chr9.bed.gz
```

### Path(s) to covariate data matrix

- Medial Frontal Gyrus
  - Path to Covariate File: `/sc/arion/projects/load/users/edwart10/projects/12-19-2022-MiGA-Replication/output/age_sex/12-19-2022/association_scan/finalized-input-files/miga.GFM.final.PEER.5N.cov.gz`
- Superior Temporal Gyrus
  - Path to Covariate File: `/sc/arion/projects/load/users/edwart10/projects/12-19-2022-MiGA-Replication/output/age_sex/12-19-2022/association_scan/finalized-input-files/miga.GTS.final.PEER.5N.cov.gz`
- Thalamus
  - Path to Covariate File: `/sc/arion/projects/load/users/edwart10/projects/12-19-2022-MiGA-Replication/output/age_sex/12-19-2022/association_scan/finalized-input-files/miga.THA.final.PEER.5N.cov.gz`
- Subventricular Zone
  - Path to Covariate File: `/sc/arion/projects/load/users/edwart10/projects/12-19-2022-MiGA-Replication/output/age_sex/12-19-2022/association_scan/finalized-input-files/miga.SVZ.final.PEER.5N.cov.gz`

```
-rw-r----- 1 edwart10 LOAD  11K Dec 20 14:14 miga.GFM.final.PEER.5N.cov.gz
-rw-r----- 1 edwart10 LOAD 9.3K Dec 20 15:37 miga.GTS.final.PEER.5N.cov.gz
-rw-r----- 1 edwart10 LOAD 8.1K Dec 20 16:00 miga.SVZ.final.PEER.5N.cov.gz
-rw-r----- 1 edwart10 LOAD 9.3K Dec 20 15:50 miga.THA.final.PEER.5N.cov.gz
```

### Path(s) to cis-QTL association testing

**output of TensorQTL.ipynb**

- `s3://statfungen/ftp_fgc_xqtl/analysis_result/cis_association/MiGA/eQTL/`
  
### Path(s) to fine-mapping with SuSiE model

### Path(s) to fine-mapping with SuSiE RSS model

### Path(s) to colocalization with SuSiE-coloc

## Links to QTL analysis notebooks

See notebooks in: 

- https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/KnightADRC/eQTL

The notebooks in this folder contain the commands and data wrangling codes for analysis of the expression data in KnightADRC. (data wrangling exist because not all data are processed using the xqtl-pipeline from the beginning and need to be reformatted to fit one intermediate step of the pipeline).

### Association data preprocessing
#### Genotype data preprocessing


#### Principal component analysis for eQTL mapping


- [genotype_preprocessing.ipynb](no MiGA folder in xqtl-analysis) shows the commands used for genotype processing and preparation steps.

- [phenotype_preprocessing.ipynb]() shows the commands used for the phenotype data processing and preparation steps.

- [covariate_preprocessing.ipynb]() shows the commands used for the covariate data processing and preparation steps.

  
### Association scan using TensorQTL and summary statistics standardization


### Aggregating QTLs across datasets?

- [TensorQTL.ipynb](https://github.com/cumc/xqtl-protocol/blob/main/code/association_scan/TensorQTL/TensorQTL.ipynb) provides the pipeline to generate TensorQTL cis association results for all QTLs. 
- [MiGA_eQTL_commands](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/cis_association/MiGA_eQTL/command_generator.ipynb) provides information about the input files for TensorQTL cis association in the base_params variable in [generate_command_1].

FIXME: Also maybe let's include the within MiGA integrative analysis here (MASH and mvSuSiE) instead of a separate resource? The data-set is small enough to not warrant being complicated with other notebooks ...
