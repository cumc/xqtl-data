# MiGA genotype data

Microglia Genomic Atlas from the Netherlands Brain Bank (NBB) and the Neuropathology Brain Bank and Research CoRE at Mount Sinai Hospital. The permission to collect human brain material was obtained from the Ethical Committee of the VU University Medical Center, Amsterdam, The Netherlands, and the Mount Sinai Institutional Review Board. For the Netherlands Brain bank, informed consent for autopsy, the use of brain tissue and accompanied clinical information for research purposes was obtained per donor ante-mortem.

## Contact

Travyse Edwards

## Data Descriptions

### Raw Data

The samples were genotyped using the Illumina Infinium Global Screening Array (GSA). Genotype imputation was performed through the Michigan Imputation Server v1.4.1 (Minimac 4) using the 1000 Genomes (Phase 3) v5 (GRCh37) European panel and Eagle v2.4 phasing in quality control and imputation mode with rsq filter set to 0.3. Following imputation, variants were lifted over to the GRCh38 reference to match the RNA-seq data using Picard liftoverVCF and the “b37ToHg38.over.chain.gz” liftover chain file.

Further method information can be found:
- [MiGA NIAGADS entry](https://dss.niagads.org/datasets/ng00105/)
- [Biorxiv Paper](https://www.biorxiv.org/content/10.1101/2020.10.27.356113v1.full)

I began analysis on the post-imputation/QC VCF file provided by the Towfique lab. The path to this file on the Minerva cluster at ISMMS is below:
`/sc/arion/projects/load/data-int/MiGA/raw/raj_microglia_anno.MAF.vcf.gz`

File size:
```
$ ls -lh
-rw-r----- 1 edwart10 LOAD 322M Jul 29  2022 /sc/arion/projects/load/data-int/MiGA/raw/raj_microglia_anno.MAF.vcf.gz
```

### Other Key Files

TBD


## Links to omics data analysis notebooks

1. EDA: https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Marcora_MSSM/MiGA/data_overview.ipynb
2. [Molecular Phenotype Calling](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Marcora_MSSM/MiGA/molecular-phenotype-calling.ipynb)
3. [Genotype Preprocessing](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Marcora_MSSM/MiGA/genotype-preprocessing.ipynb)
4. [Phenotype Preprocessing](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Marcora_MSSM/MiGA/phenotype-preprocessing.ipynb)
5. [Covariate Preprocessing](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Marcora_MSSM/MiGA/covariate-preprocessing-age_sex.ipynb)
6. [Association Scan](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Marcora_MSSM/MiGA/association-scan-preprocessing-template-age_sex.ipynb)
