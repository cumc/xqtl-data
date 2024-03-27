# STARNET genotype data

STARNET is an RNA expression study of various disease-relevant tissues obtained from living patients with cardiovascular disease (CVD). The inclusion criterion for patients was eligibility for coronary artery by-pass graft (CABG) surgery. 

## Contact

Travyse Edwards

## Data Descriptions

### Raw Data

The pre-imputation genotype data was received in HG19. We used an internal pipeline to carry out the imputation process using the TOPMED imputation server. We used the TOPMED-r2 reference panel (all populations). Pre- and Post-Imputation Quality Control measures (a part of the internal pipeline, detailed below), were carried out before the use of the xQTL pipeline. The output of the TOPMED Imputation server is in HG38, so liftover was handled as a part of the imputation process.

Pre-Imputation Quality Control
- Hardy-Weinberg Equilibrium Cutoff of 1e-6
- Variant level missingness cutoff of 0.1
- Subject level missingness cutoff of 0.1

Post-Imputation Quality Control
- MAF cutoff between common and rare of 0.005
- Rsquared for use with common variants of 0.3

I began analysis on the post-imputation genotype data. The path to this file on the Minerva cluster at ISMMS is below:
`/sc/arion/projects/load/data-int/STARNET/raw`

File size:
```
$ ls -lh
total 450M
-rwxr-x---+ 1 edwart10 LOAD  40M May 24  2022 plink.bim
-rwxr-x---+ 1 edwart10 LOAD  25K May 24  2022 plink.fam
-rwxr-x---+ 1 edwart10 LOAD 410M May 24  2022 plink.bed
```

### Other Key Files

TBD


## Links to omics data analysis notebooks

1. [Genotype Preprocessing](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Marcora_MSSM/STARNET/genotype_preprocessing.ipynb)
2. [Phenotype Preprocessing](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Marcora_MSSM/STARNET/phenotype_preprocessing.ipynb)
3. [Covariate Preprocessing](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Marcora_MSSM/STARNET/covariate_preprocessing.ipynb)
4. [Association Scan](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Marcora_MSSM/STARNET/STARNET_association_scan.clean.ipynb)
5. [Imputation Overview & Association Scan Overview](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Marcora_MSSM/STARNET/STARNET_Analysis_Complete.ipynb)
