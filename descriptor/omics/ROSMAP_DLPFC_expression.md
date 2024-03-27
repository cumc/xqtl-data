# ROSMAP DLPFC gene expression

Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) DLPFC gene expression. 

Please refer to [this document](../study_info/ROSMAP.md) for an overview of the ROSMAP project.

**NOTE: we didn't perform the omics data calling here so this descriptor is mostly documentations from the raw data source**

## Contact

Xuanhe Chen (xuanhechenxhc@163.com)

## Study Overview

- Grant number : R01 AG076901 (temporary using Gao's grant number)
- Publication : 
- Acknowledgement : 
- Study name : ROSMAP DLPFC RNA-seq Bulk Brain
- Study Description : Samples were extracted using Qiagen's miRNeasy mini kit (cat. no. 217004) and the RNase free DNase Set (cat. no. 79254), and quantified by Nanodrop and quality was evaluated by Agilent Bioanalyzer.
- Disease : Alzheimer’s Disease
- Data Citation : https://www.synapse.org/#!Synapse:syn3388564
- Additional study information : 

## Dataset Details

**Library Preparation**

Batch 1 (dorsolateral prefrontal cortex): The Broad Institutes's Genomics Platform performed RNA-Seq library preparation using the strand specific dUTP method (REF1 - Levin et al., Nature Methods 2010) with poly-A selection (REF2 - Adiconis et al., Nature Methods 2013). This method begins with poly-A selection followed by first strand specific cDNA synthesis, and then uses dUTP for second strand specific cDNA synthesis followed by fragmentation and Illumina adapter ligation for library construction. We have completed RNA-Seq with 582 of the samples that met quality (Bioanalyzer RNA integrity (RIN) score >5) and quantity thresholds (5ug).

Batch 2 (dorsolateral prefrontal cortex, posterior cingulate cortex, head of caudate nucleus): RNA sequencing libraries were prepared using the KAPA Stranded RNA-Seq Kit with RiboErase (kapabiosystems) in accordance with the manufacturer’s instructions. Briefly, 500ng of total RNA was used for ribosomal depletion and fragmentation. Depleted RNA underwent first and second strand cDNA synthesis. cDNA was then adenylated, ligated to Illumina sequencing adapters, and amplified by PCR. Final libraries were evaluated using fluorescent-based assays including PicoGreen (Life Technologies) or Qubit Fluorometer (invitrogen) and Fragment Analyzer (Advanced Analytics) or BioAnalyzer (Agilent 2100).

Batch 3 (dorsolateral prefrontal cortex, posterior cingulate cortex): 50mgs of frozen brain tissue was dissected and homogenized in DNA/RNA shield buffer (Zymo, R1100) with 3mm beads using a bead homogenizer. RNA was subsequently extracted using Chemagic RNA tissue kit (Perkin Elmer, CMG-1212) on a Chemagic 360 instrument. RNA was concentrated (Zymo, R1080) and RQN values calculated with a Fragment Analyzer total RNA assay (Agilent, DNF-471). RNA concentration was determined using Qubit broad range RNA assay (Invitrogen, Q10211) according to the manufacturer’s instructions. 500ng total RNA was used as input for sequencing library generation and rRNA was depleted with RiboGold (Illumina, 20020599). A Zephyr G3 NGS workstation (Perkin Elmer) was utilized to generate TruSeq stranded sequencing libraries (Illumina, 20020599) with custom unique dual indexes (IDT) according to the manufacturer’s instructions with the following modifications. RNA was fragmented for 4 minutes at 85°C. First strand synthesis was extended to 50 minutes. Size selection post adapter ligation was modified to select for larger fragments. Library size and concentrations were determined using an NGS fragment assay (Agilent, DNF-473) and Qubit ds DNA assay (Invitrogen, Q10211) respectively, according to the manufacturer’s instructions. The modified protocol yielded libraries with an average insert size of around 330-370bp.

 
**Sequencing**

Batch 1 (dorsolateral prefrontal cortex): Sequencing was performed on the Illumina HiSeq with 101bp paired-end reads and achieved coverage of 150M reads of the first 12 samples. These 12 samples will serve as a deep coverage reference and included 2 males and 2 females of non-impaired, mild cognitive impaired, and Alzheimer's cases. This is batch "0". The remaining samples were sequenced with coverage of 50M reads. The libraries were constructed and pooled according to the RIN scores such that similar RIN scores would be pooled together. Varying RIN scores results in a larger spread of insert sizes during library construction and leads to uneven coverage distribution throughout the pool. In our sample set, we noticed that samples with lower RIN scores between 5 and 6 had more adapter contamination. An additional 57 samples were submitted at a later date to the platform and run on an updated protocol requiring only 250ng of input RNA. This protocol is a modification of Illumina's TruSeq protocol to include long insert sizes and also be strand specific. These late samples were sequenced in batch 2 on plates 7 and 8.
Batch 2 (dorsolateral prefrontal cortex, posterior cingulate cortex, head of caudate nucleus): Sequencing was done on Illumina NovaSeq6000 sequence using 2 x 100bp cycles targeting 30 million reads per sample.
Batch 3 (dorsolateral prefrontal cortex, posterior cingulate cortex): Libraries were normalized for molarity and sequenced on a NovaSeq 6000 (Illumina) at 40-50M reads, 2x150bp paired end.

 
**Data processing**: Then RNA-Seq data were processed by our parallelized and automatic pipeline. These pipeline include trimming the beginning and ending bases from each read, identifying and trimming adapter sequences from reads, detecting and removing rRNA reads, aligning reads to reference genome. We used the non-gapped aligner Bowtie to align reads to transcriptome reference and then applied RSEM to estimate expression levels for all transcripts. The FPKM values were the outcome of our data RNA-Seq pipeline. We applied quantile normalization method to FPKM first and then used combat package to remove potential batch effect.

 
**Notes regarding sample naming**:

Sequencing samples that were sequenced more than once include the sequencing batch number as the last 2 digits of the id. For example, sample 123_456789_02 is sample "123_456789", from batch 2. The sample IDs are otherwise randomly-assigned identifiers. Some samples were re-sequenced due to poor quality or low output, they may have "redo" in the sample identifier.
 
**Notes regarding sample processing**

1.All Expression data, gene, and isoform level data are estimated with RSEM
2.Gene annotation used in RSEM estimation and alignment is gencode v14 in hg19 human genome reference
3."un-normalized" files indicate the pre-normalization expression data, which is FPKM calls from RSEM.
4."normalized" files indicates the post-normalization expression data, which were normalized by applied quantile normalization and then followed by Combat to remove batch effect. Only "Batch" covariate was used in Combat step.

### Raw data

ROSMAP DLPFC Gene Expression (RNA seq - bulk brain): 

- https://www.synapse.org/#!Synapse:syn3388564

| Brain      | Description |
| -----------| ----------- |
| Batch 1    | 638         |
| Batch 2    | 252 (117 for PolyA selection & 135 for rRNA depletion)        |
| Batch 3    | 251         |
| Total      | 1141        |

**NOTE: These data was once downloaded to BU cluster for QTL analysis phenotype preprocessing and then deleted to release storage.**

## Links to omics data analysis notebooks

1. Exploratory anlaysis on ROSMAP DLPFC sample information: https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Zhang_BU/ROSMAP_DLPFC