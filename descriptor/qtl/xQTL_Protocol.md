# xQTL protocol data

A toy data-set consisting of 49 de-identified samples from ROSMAP project, used to illustrates the computational protocols we developed for the detection and analysis of molecular QTLs (xQTLs). 


## Contact

Hao Sun

## Location

The input data and some of the intermediate output data can be download from [this Synapse folder](https://www.synapse.org/#!Synapse:syn36416601). To download the files, a synapse account and synapse clients are both needed. To setup a synapse client, please follow [this post](https://help.synapse.org/docs/Installing-Synapse-API-Clients.1985249668.html).


## How the data was prepared

### Source files

The samples that we use are 49 samples of [ROSMAP dataset](https://www.synapse.org/#!Synapse:syn4164376). The data used in this protocol paper after we processed and de-identified can be found at [here]()


```bash
cd /mnt/vast/hpc/csg/xqtl_workflow_testing/finalizing/ROSMAP_data/bam
```


```bash
for i in `cat 50_samples_synapse_id`; do 
synapse get $i;
done
```


```bash
The Genotype data are downloaded using:
```


```bash
wget https://www.ebi.ac.uk/arrayexpress/files/E-GEUV-1/GEUVADIS.chr21.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes.vcf.gz \
     https://www.ebi.ac.uk/arrayexpress/files/E-GEUV-1/GEUVADIS.chr22.PH1PH2_465.IMPFRQFILT_BIALLELIC_PH.annotv2.genotypes.vcf.gz
```


```bash
cd ../../
```


Since we are using the fastq files as starting point of our RNASeq calling pipeline, the phenotype of xqtl protocol data required some preprocessing . 



### Generating the input phenotype data
Command 1 take only the chromosome 21 and 22 from each of the bam file in the desinated diretory, then command 2 changes them into fastq file. Doing so keeps our xqtl protocol data into a managable size


```bash
sos run pipeline/phenotype_formatting.ipynb bam_subsetting  \
    --phenoFile `ls ROSMAP_data/RNASeq/*.bam` \
    --cwd ROSMAP_data/RNASeq/subsetted  \
    --container containers/rna_quantification.sif 
```


```bash
sos run pipeline/phenotype_formatting.ipynb bam_to_fastq  \
    --phenoFile `ls ROSMAP_data/RNASeq/subsetted/*.bam` \
    --cwd ROSMAP_data/RNASeq/fastq  \
    --container containers/rna_quantification.sif 
```

### Creation of sample name mapper and masks
To match and de-identified the samples in both Genotype/phenotype, a index file was created with the following codes


```bash
echo -e "fq1\tfq2" > xqtl_protocol_data_sample_list
paste <(ls *.1.fastq) <(ls *.2.fastq) >> xqtl_protocol_data_sample_list
```

***Following codes are ran in python.***


```bash
import pandas as pd
a = pd.read_csv("xqtl_protocol_data_sample_list","\t")
sample_id = [x.split(".")[0] for x in a.fq1 ]
b = pd.read_csv("filtered_sample_index","\t")
c = pd.read_csv("ROSMAP_assay_rnaSeq_metadata.csv",",")
a["rnaseq_id"] = sample_id
a.merge(b, on = "rnaseq_id")
abc = ab.merge(c, left_on = "rnaseq_id", right_on = "specimenID")
abc.to_csv("../../comprehensive_xqtl_protocol_sample_index.tsv","\t",index = False)
```

`ROSMAP_assay_rnaSeq_metadata.csv` can be downloaded from [ROSMAP metadata](https://www.synapse.org/#!Synapse:syn21088596) wherease `filtered_sample_index` is an internal file we used to determined which samples to used. For the purpose of deidentifying this file will not be released to the public.

### De-identifing the input phenotype data
In compliance to HIPAA and the regulation on ROSMAP, we need to de-identify the data before releasing them to publics


```bash
readarray -t array1 <  <(tail -49 ../../comprehensive_xqtl_protocol_sample_index.tsv | cut -f5)
readarray -t array2 <  <(tail -49 ../../comprehensive_xqtl_protocol_sample_index.tsv | cut -f3)
```


```bash
for i in ${!array1[*]} ; do mv ${array1[$i]}.subsetted.1.fastq Sample_${array2[$i]}.subsetted.1.fastq   ;done
for i in ${!array1[*]} ; do mv ${array1[$i]}.subsetted.2.fastq Sample_${array2[$i]}.subsetted.2.fastq   ;done
for i in ${!array1[*]} ; do mv ${array1[$i]}.subsetted.1.stderr Sample_${array2[$i]}.subsetted.1.stderr   ;done
for i in ${!array1[*]} ; do mv ${array1[$i]}.subsetted.1.stdout Sample_${array2[$i]}.subsetted.1.stdout   ;done
```

### Generating the input fastq list
The input of our RNA calling section requirs a list of following format, it was generated manually. We allows 2 optional columns: strand and read_length so that user can specify different stand and read length for each of the samples. However, it is not necessary to include them. Our pipeline can detect the strand based on the output of STAR Alignment.

***Following codes are ran in python.***


```bash
import pandas as pd
abc = pd.read_csv("comprehensive_xqtl_protocol_sample_index.tsv","\t",index = False)
abc = abc[["sample_id","fq1","fq2","strand","readLength"]]
abc["fq1"] =  [".".join([x] + y.split(".")[1:])  for x,y in  zip( abc.sample_id, abc.fq1) ]
abc["fq2"] =  [".".join([x] + y.split(".")[1:])  for x,y in  zip( abc.sample_id, abc.fq2) ]
abc.colums = ["ID","fq1","fq2","strand","read_length"]
abc.to_csv("xqtl_protocol_data.fastqlist","\t",index = False)
```

### Subsetting and Indexing the genotypes
Since we only use 49 samples, we extract 49 samples from the genotype data to save memory and time


```bash
cd ../
echo -e "old_name\tnew_name" > xqtl_protocol_data_sample_list
paste <(cut -f6 ../comprehensive_xqtl_protocol_data_sample_index.tsv ) <(cut -f1 ../comprehensive_xqtl_protocol_data_sample_index.tsv  ) >> xqtl_protocol_data_sample_mask
```


```bash
bcftools view DEJ_11898_B01_GRM_WGS_2017-05-15_21.recalibrated_variants.vcf.gz -S <(cat ../comprehensive_xqtl_protocol_data_sample_index.tsv | cut -f6 | tail -49 ) | \
bcftools reheader --samples xqtl_protocol_data_sample_mask  -Oz -o DEJ_11898_B01_GRM_WGS_2017-05-15_21.recalibrated_variants.xqtl_protocol_data.vcf

bcftools view DEJ_11898_B01_GRM_WGS_2017-05-15_22.recalibrated_variants.vcf.gz -S <(cat ../comprehensive_xqtl_protocol_data_sample_index.tsv | cut -f6 | tail -49 ) | \
bcftools reheader --samples xqtl_protocol_data_sample_mask  -Oz -o  DEJ_11898_B01_GRM_WGS_2017-05-15_22.recalibrated_variants.xqtl_protocol_data.vcf

bgzip DEJ_11898_B01_GRM_WGS_2017-05-15_21.recalibrated_variants.xqtl_protocol_data.vcf
bgzip DEJ_11898_B01_GRM_WGS_2017-05-15_22.recalibrated_variants.xqtl_protocol_data.vcf
tabix DEJ_11898_B01_GRM_WGS_2017-05-15_21.recalibrated_variants.xqtl_protocol_data.vcf.gz
tabix DEJ_11898_B01_GRM_WGS_2017-05-15_22.recalibrated_variants.xqtl_protocol_data.vcf.gz
```
