# STARNET macrophage gene expression QTL

STARNET is an RNA expression study of various disease-relevant tissues obtained from living patients with cardiovascular disease (CVD). The inclusion criterion for patients was eligibility for coronary artery by-pass graft (CABG) surgery.

Please refer to [this document](https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Marcora_MSSM/STARNET) for an overview of the STARNET project.

## Contact

- Contact Name: Travyse Edwards
- Contact Email: travyse.edwards@icahn.mssm.edu
- Contact Affiliation: Icahn School of Medicine at Mount Sinai
- Contact Role: Travyse performed QC & QTL analysis

## Study Overview

- Grant Number: TBD
- Publication: TBD
- Acknowledgement: TBD
- Study Name: STARNET Macrophage RNA-Seq Quantification
- Study Description: TBD
- Disease: Alzheimer's Disease
- Data Citation:
  - Local Path: `/sc/arion/projects/load/data-int/STARNET/raw`
- Additional Study Information: This data is not okay to use outside of the xQTL group.

Information to fix:

- Sample information: `STARNET/STARNET_macrophage_sample_attributes.csv`.
- Lab protocol: `STARNET/STARNET_macrophage_lab_protocol.csv`.
- Computational protocol: `STARNET/STARNET_macrophage_computational_protocol.csv`.
- QTL summary statistics output: `####/####.qtl_results.csv`.
- Fine-mapping results individual level data model: `####/####.susie.csv`.
- Fine-mapping results summary statistics model: `####/####.susie_rss.csv`.

## Dataset Description

### Raw Data

Macrophage RNA-Seq:

RNA was purified from whole blood with the RNeasy Mini kit (Qiagen, Hilden, Germany). For tissue biopsies, RNA was isolated as described (36, 37). DNA was isolated from whole blood with the QIAmp DNA Blood Midi kit (Qiagen). DNA and RNA qualities were assessed with the Agilent 2100 Bioanalyzer system (Agilent Technologies, Palo Alto, CA). Samples RIN scores of >7 were accepted for RNA-seq.Sequencing libraries were prepared with the Illumina TruSeq stranded mRNA kit, the Ribo-Zero method, and Illumina TruSeq nonstranded mRNA kit with poly(A)+ selection. Samples were sequenced using the Human OmniExpressExome-8v1 bead chip via the Illumina Infinium Assay.

- STARNET macrophage dataset on MSSM cluster:  `/sc/arion/projects/load/data-int/STARNET/raw`
  
### Molecular Phenotype Matrices

Data Processing:

The STARNET FASTQ files (paired-end, 50 - 100 bp) were processed using the ADGC FGC xQTL pipeline. In brief, the FASTQ files had their adaptors removed using fastp. These trimmed FASTQ files were aligned with the GRCh38 human reference genome using STAR with default parameters. Picard was then used to identify duplicate reads. RNA-SeQC was used to carry out post-alignment QC and RNA quantification, again using default parameters. RSEM was used to generate the expression matrix from the STAR output. 

- Processing files no longer on Minerva. Regenerate?

Sample level RNA-seq quality control

- `/sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Molecular_Phenotypes/Sample-Level-RNA-Seq-QC/output/STARNET_ribo0_fastq.rnaseqc.low_expression_filtered.outlier_removed.geneCount.gct.gz`
  - Contains 24669 genes (rows) from 479 samples (columns). The column names are the STARNET sample ids, the row names are the ensemble ids, and the values are the TPM counts. 
- `/sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Molecular_Phenotypes/Sample-Level-RNA-Seq-QC/output/STARNET_ribo0_fastq.rnaseqc.low_expression_filtered.outlier_removed.tpm.gct.gz`
  - Contains 24669 genes (rows) from 479 samples (columns). The column names are the STARNET sample ids and the row names are the ensemble ids, and the values are the TPM counts.

Bulk RNA-seq Counts Normalization

- `/sc/arion/projects/load/users/edwart10/projects/xQTL-STARNET-Analysis-05-24-2022/Molecular_Phenotypes/Bulk-RNA-Seq-Counts-Normalization/output/STARNET_ribo0_fastq.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.gz`
  - Contains 20751 genes (rows) from 479 samples (columns). The column names are the STARNET sample ids. The rows are organized by increasing chromosome number, start position, end position, and ensemble id.


## Links to QTL analysis notebooks

The notebooks in [this folder](https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Marcora_MSSM/STARNET), contain the commands and some of the results visualizations produced by the pipeline when analyzing the STARNET macrophage RNA-seq expression data.

- `STARNET_Analysis_Complete.ipynb` provides information about the imputation of genotype, summary from other preprocessing steps, and a look into the cisQTL association scan.
- `genotype_preprocessing.ipynb` shows the commands used for genotype processing and preparation steps.
  - Mostly contains the commands used to run the pipeline, but includes some pre-pipeline data wrangling.
  - This includes QC, PCA, and GRM steps
- `phenotype_preprocessing.ipynb` shows the commands used for the phenotype data processing and preparation steps.
  - As above, it mostly contains the commands used to run the pipeline, but includes some pre-pipeline data wrangling.
  - This includes quantification steps, QC, annotation, and residual expression steps
- `covariate_preprocessing.ipynb` shows the commands used for the covariate data processing and preparation steps.
  - This includes factor analysis steps
- `association_scan_cis.ipynb` provides information about the TensorQTL cis association scan.
