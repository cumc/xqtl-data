# ROSMAP PCC gene expression 

Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) PCC alternative splicing. 

## Contact 

Frank Grenn

## Study Overview

- Study information: [study_info/ROSMAP.md](../study_info/ROSMAP.md)
- Website&Logo : [https://www.synapse.org/#!Synapse:syn3157322](https://www.synapse.org/#!Synapse:syn3157322)

## Dataset Details

### Raw data

Path(s) on HPC:

- PCC RNASeq data from Zhang Lab, `/restricted/projectnb/casa/skandoi/ROSMAP_PCC_AC`:
```
$ ls -lh rnaseqc_call_PCC/*.bam | head
-rw-r--r-- 1 skandoi casa 4.0G Dec 11 18:27 1000-PCC.bam.Aligned.sortedByCoord.out.md.bam
-rw-r--r-- 1 skandoi casa 3.5G Dec  9 15:22 1000-PCC.bam.Aligned.toTranscriptome.out.bam
-rw-r--r-- 1 skandoi casa 5.5G Dec 11 18:35 1001-PCC.bam.Aligned.sortedByCoord.out.md.bam
-rw-r--r-- 1 skandoi casa 4.1G Dec  9 15:25 1001-PCC.bam.Aligned.toTranscriptome.out.bam
-rw-r--r-- 1 skandoi casa 4.5G Dec 11 18:29 1002-PCC.bam.Aligned.sortedByCoord.out.md.bam
-rw-r--r-- 1 skandoi casa 4.2G Dec  9 15:23 1002-PCC.bam.Aligned.toTranscriptome.out.bam
-rw-r--r-- 1 skandoi casa 5.1G Dec 11 18:33 1003-PCC.bam.Aligned.sortedByCoord.out.md.bam
-rw-r--r-- 1 skandoi casa 1.5G Dec  9 15:22 1003-PCC.bam.Aligned.toTranscriptome.out.bam
-rw-r--r-- 1 skandoi casa 5.5G Dec 11 18:39 1004-PCC.bam.Aligned.sortedByCoord.out.md.bam
-rw-r--r-- 1 skandoi casa 1.1G Dec  9 15:22 1004-PCC.bam.Aligned.toTranscriptome.out.bam
```

### Molecular phenotype matrices

Path(s) on HPC:

- TPM (before QC or normalization filters) `/restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/rnaseqc_call/PCC_samples_list.rnaseqc.gene_tpm.subset.gct.gz`:
1. Columns are sample names and rows are genes.
2. 560 columns (including index) and 60669 rows (including header)

- Counts (before QC or normalization fitlers):`/restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/rnaseqc_call/PCC_samples_list.rnaseqc.gene_readsCount.subset.gct.gz`:
1. Columns are sample names and rows are genes.
2. 560 columns (including index) and 60669 rows (including header)

### Other key data files

- Gene expression matrices after QC and normalization filters from Zhang Lab, `/restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/rnaseqc_call/normalize`:
```
$ ls -lh
total 45M
-rw-r--r-- 1 fgrennjr casa  45M Mar 16 19:25 PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.gz
-rw-r--r-- 1 fgrennjr casa 236K Mar 16 19:25 PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.bed.gz.tbi
-rw-r--r-- 1 fgrennjr casa  330 Mar 16 19:25 PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.stderr
-rw-r--r-- 1 fgrennjr casa  203 Mar 16 19:25 PCC_samples_list.rnaseqc.gene_tpm.low_expression_filtered.outlier_removed.tmm.expression.stdout
```


## Links to omics data analysis notebooks

Analysis notebook generation in progress and will be uploaded to [https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Zhang_BU/PCC_AC](https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Zhang_BU/PCC_AC). Steps will be similar to what is found in [https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Zhang_BU/ROSMAP_DLPFC](https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Zhang_BU/ROSMAP_DLPFC).


