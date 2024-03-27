# Alzheimer's Disease GWAS Summary Data (Wightman)

The SNP-level association testing summary statistics for Alzheimer's disease from Wightman et al 2021 Nature Genetics. This file contains the meta-analyzed summary statistics of three cohorts: all individuals, all individuals excluding 23andMe, all individuals excluding 23andMe and UKBB.

## Contact

Oluwatosin Olayinka


## Path(s) to summary statistics
- NIAGADS FTP
    - meta results `/ftp_fgc_xqtl/projects/ADGWAS_Wightman_2021_hg38_liftover_meta/wightman_meta_sumstat_hg38_qc.chr*`
    - only 23andMe`/ftp_fgc_xqtl/projects/ADGWAS_Wightman_2021_hg38_liftover_23andme/wightman_sumstat_hg38_qc.chr*`
 
- CU
    - original data (in GRCh37)
        - all individuals: `/mnt/vast/hpc/csg/data_public/GWAS_sumstats/20230530_Wightman/sum.stat.all/PGCALZ2full.txt`
        - all individuals excluding 23andMe: `/mnt/vast/hpc/csg/data_public/GWAS_sumstats/20230530_Wightman/sum.stat.excluding.23andme/PGCALZ2sumstatsExcluding23andMe.txt`
        - all individuals excluding 23andMe and UKBB: `/mnt/vast/hpc/csg/data_public/GWAS_sumstats/20230530_Wightman/sum.stat.excluding.23andme/PGCALZ2ExcludingUKBand23andME_METALInverseVariance_MetaAnalysis.txt`
        - only 23andMe individuals
            - `/mnt/vast/hpc/csg/data_public/GWAS_sumstats/20230530_Wightman/23andme/alzheimers_matched.dat.gz`
            - `/mnt/vast/hpc/csg/data_public/GWAS_sumstats/20230530_Wightman/23andme/v8.2_european_bundle-001.tar` (decompressed into `all_snp_info.txt`, `gt_snp_stat.txt`, `im_snp_stat.txt`
            - after formatting: `/mnt/vast/hpc/csg/data_public/GWAS_sumstats/20230530_Wightman/23andme/alzheimers_matched.dat_no_NA.formatted.tsv`
    - liftover data (in hg38)
        - all individuals: `/mnt/vast/hpc/csg/data_public/GWAS_sumstats/20230530_Wightman/sum.stat.all/PGCALZ2full.hg38.txt`
        - all individuals excluding 23andMe: `/mnt/vast/hpc/csg/data_public/GWAS_sumstats/20230530_Wightman/sum.stat.excluding.23andme/PGCALZ2sumstatsExcluding23andMe.hg38.txt`
        - all individuals excluding 23andMe and UKBB: `/mnt/vast/hpc/csg/data_public/GWAS_sumstats/20230530_Wightman/sum.stat.excluding.23andme/PGCALZ2ExcludingUKBand23andME_METALInverseVariance_MetaAnalysis.hg38.txt`
        - only 23andMe individuals: `/mnt/vast/hpc/csg/data_public/GWAS_sumstats/20230530_Wightman/23andme/all_snp_info.hg38.txt`
        
## Path to SuSiE RSS Fine-mapping Objects
- Li-San Wang FTP: `/ftp_fgc_xqtl/projects/GWAS_Finemapping_Results/Wightman/`
 
## Download source
Download source not publicly available

## File Schema
- `chromosome`: chromosome ID
- `position`: hg38 position (converted from hg19 with liftOver)
- `variant`: variant ID in the form `chr${chromosome}_${position}_${ref}_${alt}`
- `alt`: alternative effect allele
- `ref`: reference allele
- `z` - z-score of the SNP effect size
- `pvalue`: p-value of `beta`
- `N`:

## Links to GWAS data analysis notebooks
1. Summary statistics preprocessing: https://github.com/floutt/brain-xqtl-analysis/blob/main/analysis/Zhang_BU/susie_rss/summary_stat_qc_all.nb.html

## Cohorts included in this study

- 1,126,563 individuals = 90,338 (46,613 proxy) cases + 1,036,225 (318,246 proxy) controls
 - 77,779 cases + 554,893 controls from Jansen et al.
 - 12,559 cases + 481,332 controls not from Jansen et al: Finngen, GRACE, HUNT, BioVU, 23andme, Gothenburg H70 Birth Cohort Studies and Clinical AD from Sweden (Gothenburg), ANMerge.
- Population: US & Europe, UK, Norway, Sweden, Iceland, Finland, Spain, Norway, US, EUR

*Supplementary Table 1: A list of the datasets included in the meta-analysis. The UKB data was generated with a continous phenotype so the case-control values are estimates where the number of individuals with phenotype values <1 are controls and >=1 are cases.*

| Dataset                                                                      | Population  | Cases  | Controls  | Imputation panel                 |
| ---------------------------------------------------------------------------- | ----------- | ------ | --------- | -------------------------------- |
| Included in Jansen et al. (2019)        ｜  ｜  ｜              ｜                       |
| IGAP\*                                                                       | US & Europe | 21982  | 41944     | 1000G phase 1                    |
| UKB (Proxy)                                                                  | UK          | 46613  | 318246    | HRC, 1000G, UK10k                |
| DemGene                                                                      | Norway      | 1638   | 6059      | HRC                              |
| TwinGene                                                                     | Sweden      | 224    | 6321      | HRC                              |
| STSA                                                                         | Sweden      | 320    | 750       | HRC                              |
| deCODE (partially included)                                                  | Iceland     | 7002   | 181573    | deCODE                           |
| Total                                                                        | \-          | 77779  | 554893    | \-                               |
| Not included in Jansen et al. (2019)                                         |
| Finngen\*                                                                    | Finland     | 1798   | 72206     | SISu v3                          |
| GR@CE                                                                        | Spain       | 4120   | 3289      | HRC                              |
| HUNT                                                                         | Norway      | 1156   | 7157      | HRC+HUNT                         |
| BioVU                                                                        | US          | 600    | 36059     | HRC                              |
| 23andMe                                                                      | US          | 3807   | 359839    | 1000 Genomes Phase 3, UK10K, HRC |
| Gothenburg H70 Birth Cohort Studies and Clinical AD from Sweden (Gothenburg) | Sweden      | 712    | 2523      | HRC                              |
| ANMerge                                                                      | EUR         | 366    | 259       | HRC                              |
| Total                                                                        | \-          | 12559  | 481332    | \-                               |
| Grand total                                                                  | \-          | 90,338 | 1,036,225 |                                  |
| \*=publically available                                                      |             |        |           |                                  |


