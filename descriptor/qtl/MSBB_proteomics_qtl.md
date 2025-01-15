# MSBB brain proteomics QTL
Please refer to [this document](../study_info/MSBB.md) for an overview of the MSBB project.
## Contact

Minghui Wang

## Links to QTL analysis notebooks

See notebooks in: 

- https://github.com/cumc/xqtl-analysis/tree/main/analysis/Wang_Columbia/MSBB/pQTL(no folder)

The notebooks in this folder contain the commands and data wrangling codes for analysis of the expression data in MSBB. (data wrangling exist because not all data are processed using the xqtl-pipeline from the beginning and need to be reformatted to fit one intermediate step of the pipeline).

### Association data preprocessing
#### Genotype data preprocessing

#### Principal component analysis for eQTL mapping

#### Phenotype data preprocessing

#### Covariate data preprocessing
  
### Association scan using TensorQTL and summary statistics standardization

- [TensorQTL.ipynb](https://github.com/cumc/xqtl-protocol/blob/main/code/association_scan/TensorQTL/TensorQTL.ipynb) provides the pipeline to generate TensorQTL cis association results for all QTLs. 
- [MSBB_pQTL](https://github.com/cumc/xqtl-analysis/blob/main/analysis/Wang_Columbia/cis_association/MSBB_pQTL/command_generator.ipynb) provides information about the input files for TensorQTL cis association in the base_params variable in [generate_command_1].


### Path(s) to cis-QTL association testing

**output of TensorQTL.ipynb**

- `s3://statfungen/ftp_fgc_xqtl/analysis_result/cis_association/MSBB/pQTL/`