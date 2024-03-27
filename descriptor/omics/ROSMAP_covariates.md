# ROSMAP Covariates data

Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) covariates data

## Data Descriptions
There are couple of versions of covariates files been used for QTL calling, which may lead to inconsistency of data production and downstream integration analysis. 

The following are the files that haven been used:
1. For pQTL: FTP: `/ftp_fgc_xqtl/ref-data/ROSMAP_covariates/dataset_707_basic_02-08-2022.clean.txt`(CU: `/mnt/mfs/ctcn/datasets/rosmap/phenotypes/2022Feb08/dataset_707_basic_02-08-2022.clean.txt`)

This should be the complete covariates file, which have 3000+ samples and more covariates, other than sex, death and pmi, than we need for our QTL calling. To accomendate our QTL pipeline, formatting and processing is needed before using. 

2. For sQTL: FTP: `ftp.lisanwanglab.org/ftp_fgc_xqtl/projects/rna-seq/BU/ROSMAP_DLPFC/covariate_file/ROSMAP_xqtl_covariates_sex_death_pmi_study.tsv`(CU: `/mnt/vast/hpc/csg/rf2872/data/ROSMAP_xqtl_covariates_sex_death_pmi_study.tsv`)

This should be the file that have been processed for sQTL calling, which has 853 samples and only have covariates we needed(sex, pmi, death). This file was accomendated to our pipeline. 

3. CU: `/mnt/vast/hpc/csg/molecular_phenotype_calling/ROSMAP_shared_metadata/ROSMAP_xqtl_complete_samples_covariates_sex_death_pmi_study.tsv`

This is the one that Hao updated on May, which has 1161 samples. This file has complete covariates information for all samples that in genotype. And this is already formatted to accomendate our pipeline. S0, using this as covariates file is suggested for all QTL calling. 