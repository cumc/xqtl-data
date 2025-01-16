# ROSMAP DLPFC methylation QTL

Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) DLPFC methylation data-set. 

Please refer to [this document](../study_info/ROSMAP.md) for an overview of the ROSMAP project.

## Contact

Alexandre Pelletier

## Links to QTL analysis notebooks

See notebooks in: 

- https://github.com/cumc/xqtl-analysis/tree/main/analysis/TCW_BU/ROSMAP/mqtl

The notebooks in this folder contain the commands and data wrangling codes for analysis of the methylation data in KnightADRC. (data wrangling exist because not all data are processed using the xqtl-pipeline from the beginning and need to be reformatted to fit one intermediate step of the pipeline).

### Association data preprocessing

[Genotype_preprocessing](https://github.com/cumc/xqtl-analysis/blob/main/analysis/TCW_BU/ROSMAP/mqtl/02-Genotype_Preprocessing.ipynb) provides steps for PCA analysis for genotype data.
[Phenotype_preprocessing](https://github.com/cumc/xqtl-analysis/blob/main/analysis/TCW_BU/ROSMAP/mqtl/01-Phenotype_Preprocessing.ipynb) shows the commands used for the phenotype data processing and preparation steps.
[Covariates_preprocessing](https://github.com/cumc/xqtl-analysis/blob/main/analysis/TCW_BU/ROSMAP/mqtl/03-Covariates_Preprocessing.ipynb) shows the commands used for the covariate data processing and preparation steps.
details please see https://github.com/cumc/xqtl-analysis/tree/main/analysis/TCW_BU/ROSMAP/mqtl/scripts
  
### Association scan using TensorQTL and summary statistics standardization


- [TensorQTL.ipynb](https://github.com/cumc/xqtl-protocol/blob/main/code/association_scan/TensorQTL/TensorQTL.ipynb) provides the pipeline to generate TensorQTL cis association results for all QTLs. 
- [Knight_mQTL_commands](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/cis_association/ROSMAP_mQTL/command_generator.ipynb) provides information about the input files for TensorQTL cis association in the base_params variable in [generate_command_1].

### Path(s) to cis-QTL association testing

**output of TensorQTL.ipynb**

- `s3://statfungen/ftp_fgc_xqtl/analysis_result/cis_association/ROSMAP/mQTL/DLPFC/`