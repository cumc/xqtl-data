# ROSMAP DLPFC protein expression

Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) DLPFC protein expression. 

Please refer to [this document](../study_info/ROSMAP.md) for an overview of the ROSMAP project.

## Contact 

- Contact Name: Zining Qi
- Contact Email: zq2209@cumc.columbia.edu
- Contact Affiliation : Columbia University
- Contact Role : Zining Qi performed QTL analysis by using ROSMAP proteomics

## Study Overview

- Grant number : R01 AG076901 (temporary using Gao's grant number)
- Publication : 
- Acknowledgement : 
- Study name : ROSMAP DLPFC protein expression
- Study Description : Performed on 596 ROSMAP proteomics samples via the ADSP FGC xQTL pipeline. The output format is prepared for pQTL analysis.
- Disease : Alzheimer’s Disease
- Data Citation : ROSMAP WGS data: https://www.synapseorg#!Synapse:syn17015098

## Dataset Description

### Raw data
The data released in [this article](https://www.nature.com/articles/s41591-020-0815-6#Abs1) were processed after sampling, quantification, and normalization. We will use the protein abundance data from ROSMAP DLPFC subjects generated via tandem mass tag isobaric labeling mass spectrometry methods for protein identification and quantification [Tandem Mass Tag (TMT) Discovery Proteomics (50 batches)](https://www.synapse.org/#!Synapse:syn21449447) as phenotype for our proteomics analysis.

According to the article, this data was normalized with following steps:
- Batch randomization: The ROSMAP DLPFC samples were randomized into 50 batches (8 samples per batch) based on age at death, sex, PMI and diagnosis.
- Controlling for batch-specific variance: A two-way abundance-sample data table are implemented a median polish algorithm for removing technical variance. The detail of the algorithm is [here](https://github.com/edammer/TAMPOR). For ROS/MAP 50-batch TMT protein abundances, two pooled channels in each TMT batch and 400 individual case samples were used as algorithm paramenters.
- Regression of covariates: Nonparametric bootstrap regression was performed separately in each cohort by subtracting the trait of interest (age at death, sex or PMI) times the median estimated coefficient from 1,000 iterations of fitting for each protein in the cohort-specific log2(abundance) matrix. Ages at death used for regression were uncensored. Case status/diagnosis was also explicitly modeled (protected) in each regression. 
- Log2 transformed with median centered near zero.

And Quality Control includes:
- Parameters dutring protein quantification: Percolator was used to filter peptide spectral matches and peptides to an FDR <1%. Following spectral assignment, peptides were assembled into proteins and were further filtered based on the combined probabilities of their constituent peptides to a final FDR of 1%.
- Outlier removal and ambiguous status case exclusion (FIXME: confirm the details of this step)
- Proteins with ≥50% missing values are removed before regression.

### Molecular phenotype matrices

Quantitative proteomics:
- Wang Lab: `/mnt/mfs/ctcn/datasets/rosmap/tmt/dlpfcTissue/round_1_2_harmonized/combine_r1andr2_protein.reg_cov_cog.uniq.proj.csv`

The phenotype raw data contains 8425 genes from 596 samples. The data were processed after sampling, quantification, and normalization with NAs, each column as a sample and each row as a gene. The raw data was processed by using ADSP FGC xQTL pipeline. There are about 7712 genes and 416 samples for final QTL analysis. 

## Links to omics data analysis notebooks

See notebooks in: 

- https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/pqtl/

The notebooks in this folder contain the commands and data wrangling codes for analysis of the proteomics data in ROSMAP. (data wrangling exist because not all data are processed using the xqtl-pipeline from the begnning and need to be reformated to fit one intermediate step of the pipeline).

### Phenotype Preprocessing

Phenotype data were processed via the following workflow: [phenotype_preprocessing](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/pqtl/phenotype_preprocessing.ipynb)

### Genotype Preprocessing

[genotype_preprocessing.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/pqtl/genotype_preprocessing.ipynb) provides information about the steps.

### Association - TensorQTL

1. [cis_pqtl_association.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/pqtl/cis_pqtl_association.ipynb) provides information and result of cis-QTL analysis.
2. [trans_pqtl_association.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/pqtl/trans_pqtl_association.ipynb) provides information and result of AD genes trans-QTL analysis.


### Other key data files

Annotation:

- Wang Lab: `/mnt/mfs/ctcn/datasets/rosmap/wgs/ampad/qualityControl/sampleSheetAfterQc.csv`

It contains sample ID information for project ID of each sample. 

Other reference files created via [Reference_data_notebook](https://github.com/cumc/xqtl-pipeline/blob/main/code/data_preprocessing/reference_data.ipynb): 

- Wang Lab: `/mnt/vast/hpc/csg/snuc_pseudo_bulk/data/reference_data/00-All.add_chr.variants.gz`, `/mnt/vast/hpc/csg/snuc_pseudo_bulk/data/reference_data/GRCh38_full_analysis_set_plus_decoy_hla.noALT_noHLA_noDecoy_ERCC.fasta`

Age at death, sex and pmi covariates will be extract from ROSMAP raw data: 

- Wang Lab: `/mnt/mfs/ctcn/datasets/rosmap/phenotypes/2022Feb08/dataset_707_basic_02-08-2022.clean.txt`



### Other procedures / files
1. [TADB window list](https://github.com/cumc/fungen-xqtl-analysis/blob/main/resource/extended_cis_before_winsorize.tsv)
2. [AD gene list](https://github.com/cumc/fungen-xqtl-analysis/blob/main/resource/combined_AD_genes.csv) includes 76 AD genes for trans-QTL analysis.