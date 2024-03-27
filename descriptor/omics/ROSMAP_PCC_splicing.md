# ROSMAP PCC alternative splicing 

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

- Leafcutter ratio output`/restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/leafcutter_output/batch_all/batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz`:
1. Columns are sample names and rows are introns. Contains each type of intron usage ratio under each sample (#particular intron in a sample / #total introns classified in the same cluster in a sample).
2. 535 columns (including index) and 389332 rows (including header)

- Leafcutter counts output`/restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/leafcutter_output/batch_all/batch_all_bam_no_ext_no_outlier_intron_usage_perind_numers.counts.gz`:
1. Columns are sample names and rows are introns. Contains each type of intron usage count under each sample (#particular intron in a sample).
2. 535 columns (including index) and 389332 rows (including header)

### Other key data files

- PCC splicing data from Zhang Lab, `/restricted/projectnb/casa/frank/xqtl_project/ROSMAP_PCC/`:
```
$ ls -lh leafcutter_output
total 1.4G
drwxr-sr-x 2 fgrennjr casa 256K Mar  6 14:17 batch_all
-rw-r--r-- 1 fgrennjr casa 2.0M Mar  6 17:36 batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz.leafcutter.clusters_to_genes.txt
-rw-r--r-- 1 fgrennjr casa 1.3G Mar  8 14:14 batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.gz
-rw-r--r-- 1 fgrennjr casa 232K Mar  8 14:15 batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.gz.tbi
-rw-r--r-- 1 fgrennjr casa 2.5K Mar  6 17:41 batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.stderr
-rw-r--r-- 1 fgrennjr casa  272 Mar  8 14:16 batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.formated.bed.stdout
-rw-r--r-- 1 fgrennjr casa  19M Mar  8 14:16 batch_all_bam_no_ext_no_outlier_intron_usage_perind.counts.gz_raw_data.qqnorm.phenotype_group.txt
drwxr-sr-x 2 fgrennjr casa 4.0K Mar  5 11:43 normalize
```


## Links to omics data analysis notebooks

Analysis notebook generation in progress and will be uploaded to [https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Zhang_BU/PCC_AC](https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Zhang_BU/PCC_AC). Steps will be similar to what is found in [https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Zhang_BU/ROSMAP_DLPFC](https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Zhang_BU/ROSMAP_DLPFC).



