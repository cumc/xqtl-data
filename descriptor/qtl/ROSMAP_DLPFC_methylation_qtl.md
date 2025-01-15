# ROSMAP DLPFC methylation QTL

Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) DLPFC methylation data-set. 

Please refer to [this document](../study_info/ROSMAP.md) for an overview of the ROSMAP project.

## Contact

Alexandre Pelletier

## Links to QTL analysis notebooks

See notebooks in: 

- https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/ROSMAP/mQTL

The notebooks in this folder contain the commands and data wrangling codes for analysis of the methylation data in KnightADRC. (data wrangling exist because not all data are processed using the xqtl-pipeline from the beginning and need to be reformatted to fit one intermediate step of the pipeline).

### Association data preprocessing
#### Genotype data preprocessing


#### Principal component analysis for eQTL mapping

- [mQTL_generation_beta_2.ipynb](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/mQTL/mQTL_generation_beta_2.ipynb)(need to double check) shows the commands used for genotype/phenotype/covariate processing and preparation steps.

  
### Association scan using TensorQTL and summary statistics standardization


### Aggregating QTLs across datasets?

- [TensorQTL.ipynb](https://github.com/cumc/xqtl-protocol/blob/main/code/association_scan/TensorQTL/TensorQTL.ipynb) provides the pipeline to generate TensorQTL cis association results for all QTLs. 
- [Knight_mQTL_commands](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/cis_association/ROSMAP_mQTL/command_generator.ipynb) provides information about the input files for TensorQTL cis association in the base_params variable in [generate_command_1].

### Path(s) to cis-QTL association testing

**output of TensorQTL.ipynb**

- `s3://statfungen/ftp_fgc_xqtl/analysis_result/cis_association/ROSMAP/mQTL/DLPFC/`