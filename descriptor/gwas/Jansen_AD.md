# Alzheimer's Disease GWAS Summary Data (Jansen)

The SNP-level association testing summary statistics for Alzheimer's disease from Jansen et al 2021 Nature Genetics. This study uses proxy AD individuals from UK Biobank.

## Contact
Oluwatosin Olayinka

## Download source

This data is derived from summary statistics from the [Jansen et al.](https://ctg.cncr.nl/documents/p1651/AD_sumstats_Jansenetal_2019sept.txt.gz) Nature Genetics paper. 

## Path(s) to summary statistics
- Li-San Wang FTP: `/ftp_fgc_xqtl/projects/ADGWAS_Jansen_2019_hg38_liftover/jansen_sumstat_hg38_qc.chr*`
- CU
    - original data: `/mnt/vast/hpc/csg/data_public/GWAS_sumstats/20230620_Jansen/AD_sumstats_Jansenetal_2019sept.txt` (GRCh37)
    - liftover to hg38: `/mnt/vast/hpc/csg/data_public/GWAS_sumstats/20230620_Jansen/AD_sumstats_Jansenetal_2019sept.hg38.txt` (hg38)

## Path to SuSiE RSS Fine-mapping Objects
- Li-San Wang FTP: `/ftp_fgc_xqtl/projects/GWAS_Finemapping_Results/Jansen/`

## File Schema

- `chromosome`: chromosome ID
- `position`: hg38 position (converted from hg19 with liftOver)
- `variant`: variant ID in the form `chr${chromosome}_${position}_${ref}_${alt}`
- `alt`: alternative effect allele
- `ref`: reference allele
- `beta`: SNP effect size
- `se`: standard error of `beta`
- `pvalue`: p-value of `beta`
- `Neff`: effecting sample size

## Links to GWAS data analysis notebooks

1. Summary statistics preprocessing: https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Zhang_BU/summary_stat_qc_all.nb.html



## Cohorts included in this study

- 455,258 individuals of European ancestry = 71,880 (proxy) cases + 383,378 (proxy) controls
- Phase 1: 79,145 individuals (Nsum; Neff=72,500) = 24,087 clinically diagnosed LOAD cases + paired with 55,058 controls.
- Phase 2: 376,113 individuals of European ancestry from UKB with parental AD status = 47,793 proxy cases + 328,320 proxy controls"	"79145 from phase 1:
  1. Alzheimer’s disease working group of the Psychiatric Genomics Consortium (PGC-ALZ) -- 17477
  2. the International Genomics of Alzheimer’s Project (IGAP) -- 54162
  3. the Alzheimer’s Disease Sequencing Project (ADSP) -- 7506 individuals = 4343 cases + 3163 controls
 

*Supplementary Table 1. Overview of cohorts for meta-analysis*

- Note: AD = Alzheimer's disease; GWAS = genome-wide genotype data; WES = whole exome sequencing data; 1000G = Thousand Genomes; HRC = Haplotype Reference Consortium. * The PGC-ALZ summary statistic have been meta-analyzed with the other 3 main cohorts, but PGC-ALZ sub-cohort specific demographics are also displayed. The 'age of onset' and 'age of last contact' of the UKB samples, refers to the age of the UKB participants (so not of the parents). For the controls of the DemGene cohort, mean age was based on 2382 individuals for which this information was available. Proxy cases and controls only refers to the UKB cohort, all other cohorts are clinical case-control cohorts.											


| Cohort        | Sub-cohort  | Geographic origin | N      | cases:|N             | Age of onset | % female         |  controls:   | N      | Age last contact | % female | Phenotype | Data Type | Imputation Reference |
| :--: |:--: | :--: | :--: | :--:| :--: | :----------: | :--------------: | :--: | :----: | :--------------: |:-------: |:--------: |:--------: |:-------------------: |
| 1\. PGC-ALZ\* | a. DemGene  | Norway            | 9703   |  |2066          | 77.0         | 62.9             |  | 7637   | 58.8             | 48.0 | AD | GWAS | 1000G Phase 3 |
|               | b. TwinGene | Sweden            | 6647   |  |322           | 79.6         | 52.5             |  | 6325   | 64.2             | 52.4 | AD | GWAS | 1000G Phase 3 |
|               | c. STSA     | Sweden            | 1127   |  |348           | 80.5         | 66.4             |  | 779    | 75.5             | 51.1 | AD | GWAS | 1000G Phase 3 |
| 2\. IGAP      |             | Europe/US         | 54162  |  |17008         | 74.2         | 61.3             |  | 37154  | 69.8             | 57.3 | AD | GWAS | 1000G Phase 1 |
| 3\. ADSP      |             | Europe/US         | 7506   | | 4343          | 74.1         | 55.0             |  | 3163   | 86.5             | 59.5 | AD | WES | 1000G Phase 3 |
| 4\. UKB       |             | UK                | 376113 | | 47793         | 59.1         | 56.5             |  | 328320 | 56.4             | 53.6 | by proxy AD | GWAS | HRC |
