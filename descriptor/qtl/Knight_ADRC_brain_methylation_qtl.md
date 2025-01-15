# Knight ADRC brain methylation QTL

## Contact

Alexandre Pelletier

## Links to QTL analysis notebooks

See notebooks in: 

- https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/KnightADRC/mQTL

The notebooks in this folder contain the commands and data wrangling codes for analysis of the methylation data in KnightADRC. (data wrangling exist because not all data are processed using the xqtl-pipeline from the beginning and need to be reformatted to fit one intermediate step of the pipeline).

### Association data preprocessing
- [KnightADRC_mQTL_Preprocessing_Analysis.ipynb](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/KnightADRC/mQTL/KnightADRC_mQTL_Preprocessing_Analysis.ipynb) shows the commands used for genotype/phenotype/covariate processing and preparation steps.
  
### Association scan using TensorQTL and summary statistics standardization


- [TensorQTL.ipynb](https://github.com/cumc/xqtl-protocol/blob/main/code/association_scan/TensorQTL/TensorQTL.ipynb) provides the pipeline to generate TensorQTL cis association results for all QTLs. 
- [Knight_mQTL_commands](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/cis_association/Knight_mQTL/command_generator.ipynb) provides information about the input files for TensorQTL cis association in the base_params variable in [generate_command_1].

### Path(s) to cis-QTL association testing

**output of TensorQTL.ipynb**

- `s3://statfungen/ftp_fgc_xqtl/analysis_result/cis_association/KNIGHT/mQTL/Brain/`