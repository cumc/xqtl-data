# Alzheimer's Disease GWAS Summary Data (Kunkle)

The SNP-level association testing summary statistics for Alzheimer's disease from Kunkle et al 2019 Nature Genetics. Position values were converted from hg19 to hg38 using liftOver.

## Contact

Oluwatosin Olayinka


## Path(s) to summary statistics
- NIAGADS FTP, `/ftp_fgc_xqtl/projects/ADGWAS_Kunkle_2019_hg38_liftover/kunkle_sumstat_hg38_qc.chr*`
- CU
    - original data (in GRCh37)
        - stage 1: `/mnt/vast/hpc/csg/data_public/GWAS_sumstats/20231011_Kunkle/'Kunkle_etal_Stage1_results.txt?file=1'`
        - stage 2: `/mnt/vast/hpc/csg/data_public/GWAS_sumstats/20231011_Kunkle/'Kunkle_etal_Stage2_results.txt?file=1'`
    - liftover data (in GRCh38): 
        - stage 1: `/mnt/vast/hpc/csg/data_public/GWAS_sumstats/20231011_Kunkle/Kunkle_etal_Stage1_results.txt_file_1_hg38.txt`
        - stage 2: `/mnt/vast/hpc/csg/data_public/GWAS_sumstats/20231011_Kunkle/Kunkle_etal_Stage2_results.txt_file_1_hg38.txt`     

## Path to SuSiE RSS Fine-mapping Objects
- Li-San Wang FTP: `/ftp_fgc_xqtl/projects/GWAS_Finemapping_Results/Kunkle/`
 
## Download source
This data is derived from summary statistics from the [Kunkle et al.](http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST007001-GCST008000/GCST007511/Kunkle_etal_Stage1_results.txt) Nature Genetics paper.

## File Schema
- `chromosome`: chromosome ID
- `position`: hg38 position (converted from hg19 with liftOver)
- `variant`: variant ID in the form `chr${chromosome}_${position}_${ref}_${alt}`
- `alt`: alternative effect allele
- `ref`: reference allele
- `beta`: SNP effect size
- `se`: standard error of `beta`
- `pvalue`: p-value of `beta`

## Links to GWAS data analysis notebooks
1. Summary statistics preprocessing: https://github.com/floutt/brain-xqtl-analysis/blob/main/analysis/Zhang_BU/susie_rss/summary_stat_qc_all.nb.html


## Cohorts included in this study

- 46 case-control studies: 21,982 cases + 41,944 controls

- final sample:
94,437 individuals = 35,274 clinical and autopsy-documented AD cases + 59,163 controls

- 4 consortia (46 case-control studies in Suppl. Table 2) non-Hispanic Whites (NHW):
 - ADGC: Alzheimer Disease Genetics Consortium 
 - CHARGE: Cohorts for Heart and Aging Research in Genomic Epidemiology Consortium
 - EADI: The European Alzheimer's Disease Initiative
 - GERAD/PERADES: Genetic and Environmental Risk in AD/Defining Genetic, Polygenic and Environmental Risk for Alzheimer's Disease Consortium"

*Supplementary Table 1. Description of the consortium data sets used for Stage 1 discovery, Stage 2 and Stage 3.*
**Discovery**
|     |         | Alzheimer’s disease cases || Controls       |||
| -------------- | ------- | ------------------------- | -------------- |------ |------ |------ |
| Consortium     | N       | Percent female            | Mean AAO (s.d) | N | Percent female | Mean AAE (s.d) |
| ADGC           | 14,428  | 59.3                      | 71.1 (17.3)    | 14,562 | 59.3 | 76.2 (9.9) |
| CHARGE         | 2,137   | 67.3                      | 82.6 (12)      | 13,474 | 55.8 | 76.7 (8.2) |
| EADI           | 2,240   | 65                        | 75.4 (9.1)     | 6,631 | 60.6 | 78.9 (7.0) |
| GERAD          | 3,177   | 64                        | 73.0 (0.2)     | 7,277 | 51.8 | 51.0 (0.1) |
| N              | 21,982  |                           |                | 41,944 |  |  |

**Stage 2\***
| Country | N                         | Percent female | Mean AAO (s.d) | N | Percent female | Mean AAE (s.d.) |
| -------------- | ------- | ------------------------- | -------------- |--|------ |------ |
| Belgium        | 878     | 66.1                      | 78.8 (8.2)     | 661 | 59.5 | 65.7 (14.3) |
| Finland        | 422     | 68                        | 71.4 (6.9)     | 562 | 59.3 | 69.1 (6.2) |
| Germany        | 972     | 63.9                      | 73.0 (8.6)     | 2,378 | 53.1 | 69.5 (10.1) |
| Greece         | 256     | 63.3                      | 73.1 (7.9)     | 229 | 34.1 | 49.3 (16.4) |
| Hungary        | 125     | 68                        | 78.9 (7.3)     | 100 | 69 | 74.4 (6.5) |
| Italy          | 1,729   | 66.5                      | 71.5 (8.7)     | 720 | 55.7 | 70.0 (10.4) |
| Spain          | 2,121   | 66.3                      | 75.0 (8.3)     | 1,921 | 55.3 | 70.2 (10.8) |
| Sweden         | 797     | 61.7                      | 76.8 (8.1)     | 1,506 | 62.8 | 70.6 (8.7) |
| UK             | 490     | 67.6                      | 74.6 (8.7)     | 1,066 | 29.2 | 73.8 (6.5) |
| USA            | 572     | 61.9                      | 83.5 (7.6)     | 1,340 | 54 | 79.3 (6.8) |
| N              | 8,362   |                           |                | 10,483 |  |  |

**Stage 3\***
| Country | N                         | Percent female | Mean AAO (s.d) | N | Percent female | Mean AAE (s.d.) |
|------ |------ |------ |------ |------ |------ |------ |
| Spain (ACE)    | 932     | 71                        | 77.7 (7.9)     | 1,813 | 68.4 | 54.7 (12.1) |
| UK (Cardiff)   | 1,902   | 64.8                      | 77.1 (7.9)     | 1,047 | 57.8 | 73.9 (12.9) |
| USA (ADC7)     | 514     | 51.3                      | 73.9 (8.3)     | 790 | 63.6 | 72.3 (7.7) |
| Spain (GR@ACE) | 1,582   | 74.6                      | 78.5 (8.0)     | 3,086 | 48 | 54.0 (14.0) |
| N              | 4,930   |                           |                | 6,736 |  |  |

- AAO, age at onset; AAE, age at examination.							
- *Stage 2 and Stage 3 datasets were combined for genotyping of 33 replication variants not present on the 2013 custom chip

*Supplementary Table 2. Demographic description of datasets within each consortium.*

| |Consortium         | AD cases|| | Controls     |||
| ------------------ | -------- | ------------ |---- |---- |---- |---- |---- |
||| N                  | % female | Mean AA (SD) | N | % female | Mean AAE (SD) |
| ADGC               | ACT      | 532          | 62.6 | 78.8 (12.7) | 1,571 | 55.6 | 81.7 (5.9) |
| ADGC               | ADC1               | 1,549    | 54.3         | 71.6 (11.0) | 512 | 59.2 | 76.8 (8.8) |
| ADGC               | ADC2               | 727      | 50.8         | 61.4 (29.5) | 156 | 67.9 | 75.8 (7.9) |
| ADGC               | ADC3               | 894      | 54.7         | 58.6 (32.8) | 586 | 63 | 72.8 (17.5) |
| ADGC               | ADC4               | 304      | 55.3         | 73.4 (7.0) | 377 | 63.9 | 75.7 (8.1) |
| ADGC               | ADC5               | 286      | 53.1         | 73.7 (7.0) | 505 | 65.5 | 77.6 (9.0) |
| ADGC               | ADC6               | 213      | 58.2         | 73.9 (7.6) | 338 | 66.6 | 74.6 (9.0) |
| ADGC               | ADNI               | 268      | 42.2         | 75.3 (7.1) | 173 | 40.5 | 78.6 (5.5) |
| ADGC               | BIOCARD            | 6        | 33.3         | 73.8 (6.1) | 112 | 62.5 | 68.0 (5.5) |
| ADGC               | CHAP               | 27       | 63           | 84.8 (7.6) | 144 | 52.8 | 81.8 (6.6) |
| ADGC               | EAS                | 9        | 44.4         | 85.2 (4.9) | 141 | 41.1 | 84.4 (5.2) |
| ADGC               | GenADA             | 666      | 56.9         | 72.8 (13.5) | 712 | 63.9 | 74.2 (7.0) |
|ADGC               |  MAYO               | 658      | 57.4         | 73.6 (4.8) | 1,046 | 51.1 | 72.9 (4.4) |
| ADGC               | MIRAGE             | 491      | 63.3         | 69.9 (11.5) | 738 | 58.8 | 70.8 (12.1) |
| ADGC               | MTC                | 256      | 57           | 73.6 (11.8) | 189 | 61.4 | 70.9 (9.7) |
| ADGC               | NIALOAD            | 1,798    | 65           | 73.1 (9.3) | 1,568 | 60.2 | 73.8 (9.3) |
| ADGC               | NBB                | 80       | 71.3         | 74.5 (7.5) | 48 | 56.3 | 81.5 (9.4) |
| ADGC               | OHSU               | 132      | 62.1         | 85.9 (5.7) | 153 | 54.9 | 83.9 (7.6) |
|ADGC               |  PFIZER             | 696      | 53.7         | 73.7 (5.0) | 762 | 54.1 | 77.2 (4.9) |
| ADGC               | RMAYO              | 13       | 23.1         | 78.5 (9.0) | 233 | 41.6 | 79.2 (5.8) |
| ADGC               | ROSMAP             | 295      | 70.5         | 85.6 (6.2) | 769 | 72 | 82.2 (7.1) |
| ADGC               | ROSMAP2            | 59       | 78           | 81.9 (6.9) | 217 | 76 | 80.8 (7.2) |
| ADGC               | TARC1              | 323      | 61.6         | 74.0 (7.1) | 181 | 65.2 | 73.9 (8.2) |
|ADGC               |  TGEN2              | 668      | 64.8         | 67.2 (22.9) | 365 | 48.5 | 80.0 (8.7) |
| ADGC               | UKS                | 596      | 57.4         | 72.2 (6.6) | 170 | 51.2 | 64.1 (3.0) |
| ADGC               | UMCWRMSSM          | 1,177    | 64.5         | 71.1 (17.4) | 1,126 | 61.3 | 73.5 (10.6) |
|ADGC               |  UPITT              | 1,255    | 62.9         | 66.8 (22.4) | 829 | 63.3 | 75.5 (6.0) |
| ADGC               | WASHU              | 339      | 57.2         | 69.1 (21.5) | 187 | 60.4 | 76.9 (8.4) |
| ADGC               | WASHU2             | 38       | 57.9         | 73.4 (7.3) | 94 | 46.8 | 51.7 (35.2) |
| ADGC               | WHICAP             | 73       | 72.6         | 83.9 (7.8) | 560 | 60.4 | 81.7 (6.7) |
| CHARGE             | AGES     | 95           | 51.6 | 81.5 (0.1) | 2,708 | 59.2 | 75.7 (0.1) |
| CHARGE             |ASPS               | 277      | 57.8         | 76.4 (8.3) | 169 | 58 | 66.4 (10.8) |
| CHARGE             |CHS                | 450      | 66           | 81.9 (5.2) | 1,702 | 60.3 | 81.1 (5.2) |
| CHARGE             |FHS                | 330      | 64           | 86.1 (7.2) | 3,910 | 49 | 74.0 (9.5) |
|CHARGE             | ROTTERDAM          | 985      | 73.2         | 83.5 (6.6) | 4,985 | 57.6 | 78.0 (7.6) |
| EADI               |          | 2,240        | 65 | 75.4 (9.1) | 6,631 | 60.6 | 78.9 (7.0) |
| GERAD              |   MRC    | 1,008        | 70.3 | 80.9 (6.5) | 873 | 61.6 | 75.9 (6.3) |
| GERAD              |   ARUK             | 939      | 61           | 76.6 (9.6) | 82 | 59.8 | 77.9 (7.6) |
|  GERAD              |  BONN             | 551      | 63.7         | 72.9 (8.3) | 37 | 64.9 | 79.5 (3.6) |
|  GERAD              |  WASHU            | 423      | 56           | 82.1 (9.0) | 156 | 65.4 | 78.5 (9.7) |
|  GERAD              |  NIMH             | 127      | 63           | 80.1 (6.1) | \- | \- | \- |
|   GERAD              | UCL:PRION        | 82       | 59.8         | 63.6 (9.9) | \- | \- | \- |
|   GERAD              | UCL:LASER        | 47       | 74.5         | 80.6(7.9) | \- | \- | \- |
|   GERAD              | 1958BC           | \-       | \-           | \- | 5,342 | 49.8 | 45.0 (0.0) |
|  GERAD              |  KORA             | \-       | \-           | \- | 434 | 49.1 | 56.0 (7.2) |
|  GERAD              |  HNR              | \-       | \-           | \- | 353 | 52.9 | 54.6 (5.3) |
|  GERAD              |  MAYO<sup>1</sup> | \-       | \-           | \- | \- | \- | \- |
| TOTALS             |          | 21,982       |  |  | 41,944 |  |  |
