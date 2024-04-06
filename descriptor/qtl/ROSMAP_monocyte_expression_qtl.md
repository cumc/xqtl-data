# ROSMAP RNA-seq monocyte QTL

Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) monocyte data-set. 

Please refer to [this document](../study_info/ROSMAP.md) for an overview of the ROSMAP project.

## Contact

Travyse Edwards

## Data descriptions

The ROSMAP monocyte data on MSSM were downloaded from [syn22024496](https://www.synapse.org/#!Synapse:syn22024496) on July 11th, 2022. (path on MSSM to be added)

- Path on MSSM cluster `/sc/arion/projects/load/data-ext/ROSMAP/raw/rnaseq_monocytes_syn23650893/Gene_Expression-RNA-seq-monocyte`
- Path on S3 Bucket `s3://statfungen/ftp_fgc_xqtl/eQTL/ROSMAP/monocyte/analysis_ready/phenotype_preprocessing/monocyte_sample_fastq.final.rnaseqc.low_expression_filtered.outlier_removed.tmm.expression.bed.gz`

### Preview Monocyte Gene Expression Data

Over all 615 samples in the dataset, 302 samples have diagnosis meta data, 1 sample missing associated sex meta data.

These samplesa ll share the same `library preparation method` and are not `multi-specimen` samples. However, there is variety in `read length`, `sex`, and `platform`. It may be worthwhile to use these as covariates in the downstream analyses. I will remove the two samples that are missing sex information (though I can just impute the sex).

The biospecimen file identifies the individuals that have SNP array data, Whole Genome Sequencing data, or both available. An overlapping check confirmed the monocyte gene expression contains a mix of SNP array and whole genome sequencing data (with a lot of overlap between the two). With in the 614 samples for which we have the expression data for, 246 are overlapped with WGS, 313 are overlapped with SNP array and 239 are overlapped with joint-call WGS.

Among the 613 samples in the bed.gz file, 
1. 56 of the samples are duplicates, there are 557 unique samples in total
2. 237 of the samples are properly mapped to the samples.  320 samples remaining.
3. 154 out of the 320 samples are in the synapse metadata, but only 3 has wgs, whose genotype ID cannot be found
4. 166 out of the 320 is not in any of metadata, nor in any covariates data.
Please see this notebook for details.
