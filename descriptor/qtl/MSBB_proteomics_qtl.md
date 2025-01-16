# MSBB brain proteomics QTL
Please refer to [this document](../study_info/MSBB.md) for an overview of the MSBB project.
## Contact

Minghui Wang

## Links to QTL analysis notebooks

See notebooks in: 

- https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/MSBB/pQTL

The notebooks in this folder contain the commands and data wrangling codes for analysis of the expression data in MSBB. (data wrangling exist because not all data are processed using the xqtl-pipeline from the beginning and need to be reformatted to fit one intermediate step of the pipeline).

### Association data preprocessing

- [genotype_preprocessing.ipynb](https://github.com/cumc/xqtl-analysis/tree/main/analysis/TCW_BU/MSBB/genotype_preprocessing) shows the commands used for genotype processing and preparation steps.
- [phenotype_preprocessing.ipynb](https://github.com/cumc/xqtl-analysis/blob/main/analysis/TCW_BU/MSBB/pqtl/01-phenotype_preprocessing.R) shows the commands used for the phenotype data processing and preparation steps.
- [covariate_preprocessing.ipynb](https://github.com/cumc/xqtl-analysis/blob/main/analysis/TCW_BU/MSBB/mqtl/03-Covariates_Preprocessing.ipynb) shows the commands used for the covariate data processing and preparation steps.
  Genotype data and covariate data are the same for MSBB.
  
### Association scan using TensorQTL and summary statistics standardization

- [TensorQTL.ipynb](https://github.com/cumc/xqtl-protocol/blob/main/code/association_scan/TensorQTL/TensorQTL.ipynb) provides the pipeline to generate TensorQTL cis association results for all QTLs. 
- [MSBB_pQTL](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/cis_association/MSBB_pQTL/command_generator.ipynb) provides information about the input files for TensorQTL cis association in the base_params variable in [generate_command_1].


### Path(s) to cis-QTL association testing

**output of TensorQTL.ipynb**

- `s3://statfungen/ftp_fgc_xqtl/analysis_result/cis_association/MSBB/pQTL/`