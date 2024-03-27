# Knight ADRC brain proteomics
Charles F And Joanne Knight Alzheimer's Disease Research Center (Knight-ADRC)

## Contact
Zining Qi

- Contact Email: zq2209@cumc.columbia.edu
- Contact Affiliation : Columbia University
- Contact Role : Zining Qi performed QTL analysis by using Knight proteomics

## Study Overview

- Grant number : R01 AG076901 (temporary using Gao's grant number)
- Publication : 
- Acknowledgement : 
- Study name : ROSMAP DLPFC proteomics analysis
- Study Description : Performed analysis on 442 Knight proteomics samples via the ADSP FGC xQTL pipeline. The output format is prepared for pQTL analysis.
- Disease : Alzheimer’s Disease
- Data Citation : Knight data: https://www.niagads.org/knight-adrc-collection

## Dataset Description

### Raw data
All brain samples were collected from parietal lobe. Brain tissues (~500mg) were collected from the fresh frozen human parietal lobes. SomaScan 1.3k platform were applied to measure the brain protein. The protein levels were reported as relative units of intensity (RFU or Relative Fluorescence Unit).

### Molecular phenotype matrices
Quality Control:
Data released had some initial quality control:
- Analyst with SF >= 0.5 and CV >= 0.15 removed
- Use IQR to detect outliers and replace outliers with NA

Normalization:
In this notebook, we applied more quality control steps: 
- Log2 transformed with median centered near zero. 
- This normalization make data have approximate normal distribution and more comparable with ROSMAP proteomics data.

Quantitative proteomics:
- Wang Lab: `/mnt/vast/hpc/csg/zq2209/data_production/proteomics/knight/WashU_BrainProt_442samples_matrix.csv`

The phenotype raw data contains 1296 genes(rows) from 442 samples(columns). The data were processed after sampling, quantification, and quality control with NAs.

### Other key data files

Annotation:

- Wang Lab: `/mnt/vast/hpc/csg/ftp_lisanwanglab_sync/ftp_fgc_xqtl/projects/proteomics/knightadrc-washu/WashU_Brain_Somascan1.3k_FEATUREinfo.csv`

It contains gene and protein information of each sample. 

Other reference files created via [Reference_data_notebook](https://github.com/cumc/xqtl-pipeline/blob/main/code/data_preprocessing/reference_data.ipynb): 

- Wang Lab: `/mnt/vast/hpc/csg/snuc_pseudo_bulk/data/reference_data/00-All.add_chr.variants.gz`, `/mnt/vast/hpc/csg/snuc_pseudo_bulk/data/reference_data/GRCh38_full_analysis_set_plus_decoy_hla.noALT_noHLA_noDecoy_ERCC.fasta`

Age at death, sex and pmi covariates will be extract from ROSMAP raw data: 

- Wang Lab: `/mnt/vast/hpc/csg/ftp_lisanwanglab_sync/ftp_fgc_xqtl/projects/proteomics/knightadrc-washu/WashU_MAP_somascan1.3k_Brain_covariates.csv`

## Links to omics data analysis notebooks

See notebooks in: 

- https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/knight/pqtl/

The notebooks in this folder contain the commands and data wrangling codes for analysis of the proteomics data in Knight. (data wrangling exist because not all data are processed using the xqtl-pipeline from the begnning and need to be reformated to fit one intermediate step of the pipeline).

### Phenotype Preprocessing

Phenotype data were processed via the following workflow: [phenotype_preprocessing](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/knight/pqtl/phenotype_preprocessing.ipynb)

### Genotype Preprocessing

[genotype_preprocessing.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/knight/pqtl/genotype_preprocessing.ipynb) provides information about the steps.

### Association - TensorQTL

1. [cis_pqtl_association.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/knight/pqtl/cis_pqtl_association.ipynb) provides information and result of cis-QTL analysis.
2. [trans_pqtl_association.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/knight/pqtl/trans_pqtl_association.ipynb) provides information and result of AD genes trans-QTL analysis.

### Other procedures / files
1. [proteomics_pheno_whole_genome.proteomics_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.PEER.diag.pdf](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/knigt/pqtl/figure/proteomics_pheno_whole_genome.proteomics_cov.ROSMAP_NIA_WGS.leftnorm.filtered.filtered.prune.pca.resid.PEER.diag.pdf) view of PCA result of the pQTL analysis (steps included in `genotype_preprocessing.ipynb`)
2. [AD gene list](https://docs.google.com/spreadsheets/d/166P7ThONaIDyPh2luJHoXDxlnhpsr56a8c_OE_uPQ3w/edit#gid=0) includes 76 AD genes for trans-QTL analysis.
