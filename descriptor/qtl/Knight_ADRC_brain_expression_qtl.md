# Knight ADRC brain gene expression QTL

## Contact

Chunming Liu

## Links to QTL analysis notebooks

See notebooks in: 

- https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/KnightADRC/eQTL

The notebooks in this folder contain the commands and data wrangling codes for analysis of the expression data in KnightADRC. (data wrangling exist because not all data are processed using the xqtl-pipeline from the beginning and need to be reformatted to fit one intermediate step of the pipeline).

### Association data preprocessing

- [Knight_data_RNASeq.ipynb](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/KnightADRC/eQTL/Knight_data_RNASeq.ipynb) shows the commands used for phenotype calling.

- [genotype_preprocessing.ipynb](https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/KnightADRC/eQTL/genotype_preprocessing.ipynb) shows the commands used for genotype processing and preparation steps.

- [phenotype_preprocessing.ipynb](https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/KnightADRC/eQTL/phenotype_preprocessing.ipynb) shows the commands used for the phenotype data processing and preparation steps.

- [covariate_preprocessing.ipynb](https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/KnightADRC/eQTL/covariates_preprocessing.ipynb) shows the commands used for the covariate data processing and preparation steps.

  
### Association scan using TensorQTL and summary statistics standardization

- [TensorQTL.ipynb](https://github.com/cumc/xqtl-protocol/blob/main/code/association_scan/TensorQTL/TensorQTL.ipynb) provides the pipeline to generate TensorQTL cis association results for all QTLs. 
- [Knight_eQTL_commands](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/cis_association/Knight_eQTL/command_generator.ipynb) provides information about the input files for TensorQTL cis association in the base_params variable in [generate_command_1].


### Path(s) to cis-QTL association testing

**output of TensorQTL.ipynb**

- `s3://statfungen/ftp_fgc_xqtl/analysis_result/cis_association/KNIGHT/eQTL/Brain/`