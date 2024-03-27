# ROSMAP DLPFC H3K9ac 

Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) h3k9ac data-set. 

Please refer to [this document](../study_info/ROSMAP.md) for an overview of the ROSMAP project.

## Contact 

- Contact Name : Xuanhe Chen; Hao Sun; Hans Klein
- Contact Email : xuanhechenxhc@163.com; hs3163@cumc.columbia.edu; hk2948@cumc.columbia.edu
- Contact Affiliation : Columbia University
- Contact Role : Xuanhe Chen performed QTL analysis using H3K9ac peaks; Hao Sun performed univariate fine-mapping, Hans Klein performed peak calling


## Study Overview

- Grant number : R01 AG076901 (temporary using Gao's grant number)
- Publication : 
- Acknowledgement : 
- Study name : ROSMAP DLPFC H3K9ac peak calling
- Study Description : Performed peak calling on 669 ROSMAP samples' h3k9ac samples via the ADSP FGC xQTL pipeline. The output format is prepared for haQTL analysis.
- Disease : Alzheimer’s Disease
- Data Citation : ROSMAP WGS data: https://www.synapse.org/#!Synapse:syn10901595. 
- Additional study information : The phenotype data is an improved version (used advanced method and identified more peaks) of this published ROSMAP hak9ac readcounts: https://www.synapse.org/#!Synapse:syn17016212. 

## Dataset Details
### Sample collection （should be added together）
In our haQTL anlaysis, we executed an association study centered on the histone 3 lysine 9 acetylation (H3K9ac) mark, utilizing a cohort of 669 samples from the ROSMAP DLPFC dataset. Subsequent to mapping these samples to Whole Genome Sequencing (WGS) data from the identical dataset, and incorporating an overlap with the ROSMAP joint call, we refined the sample pool to 596 for the ensuing haQTL mapping analysis.

### Raw data （should be added together, but in different sections）
Human brain H3K9ac ChIP-seq: 

Millipore's anti-H3K9ac antibody (catalog # 06–942, lot: 31636) was selected based on its robust validation for ChIP-seq applications, with validation data accessible at `http://www.emdmillipore.com/US/en/product/Anti-acetyl-Histone-H3-Lys9-Antibody,MM_NF-06-942`. Gray matter samples (50 mg) were meticulously dissected on ice from biopsied samples obtained from the dorsolateral prefrontal cortex (DLPFC) of participants within the ROS/MAP cohorts. The dissected tissue was then finely minced and cross-linked using 1% formaldehyde at room temperature for 15 minutes, with subsequent quenching of the cross-linking reaction achieved through the addition of 0.125 M glycine. Following cross-linking, the tissue samples were subjected to homogenization using a tissue lyser equipped with a 5 mm stainless steel bead. Subsequently, nuclei were lysed in cell lysis buffer, and chromatin was sheared through sonication.
For the ChIP assay, samples were incubated overnight at 4°C with 2.5 μl of the anti-H3K9ac antibody, and the final reaction volume was adjusted to 3 ml using ChIP Dilution Buffer. Chromatin fragments bound to the antibody were subsequently purified utilizing protein A Sepharose beads. Following this, we constructed the sequencing library using the extracted DNA, following the manufacturer’s protocol(**catalog?**), which involved essential steps such as end repair, adapter ligation, and gel-based size selection. Single-end reads with a length of 36 bp per read were generated from pooled library on Illumina Hiseq. 

### Molecular phenotype matrices （should be added together, but in different sections）

Data Processing:

**Revised from description from previous Synapse release, changed some parameters found from current script**
The raw data, procured from HiSeq, underwent a quality control process using FastQC and was subsequently aligned to the GRCh38 reference genome utilizing Bowtie2. Following alignment, the resultant BAM files were converted to BED format via bamToBed for further analysis. In the individual sample analysis, a comprehensive set of 92,401 peak regions was discerned using MACS2 with tailored parameters. The analysis engaged the broad peak option, specifically assigning a "broad-cutoff" of 0.1 and implementing a q-value cutoff of 0.05.
After the identification of peaks, a subsequent quality control phase was undertaken to further ensure the reliability and accuracy of the results. Samples not satisfying the ensuing thresholds were omitted: (i) a minimum of 15x10^6 unique reads, (ii) a non-redundant fraction of 0.3 or higher, (iii) a cross-correlation of 0.03 or above, (iv) a fraction of reads in peaks of 0.05 or higher, and (v) at least 6000 peaks. It's noteworthy that pooled genomic DNA served as the negative control library for peak calling, substantiating the precision and specificity of peak region identification.
To define and quantify H3K9ac domains, we parsed BED files for genomic region data and identified H3K9ac marked domains. Quantification for each sample was conducted by counting reads extended towards the 3'-end, ensuring the precision of our methodology.

Read counts:
- Wang Lab: `/mnt/mfs/ctcn/datasets/rosmap/h3k9ac/dlpfcTissue/batch1/values/counts/H3K9acCounts.txt` (185M)

Annotation:
- Wang Lab: `/mnt/mfs/ctcn/datasets/rosmap/h3k9ac/dlpfcTissue/batch1/values/counts/H3K9acDomains.csv` (6.5M)

The H3K9acCounts.txt contains 92401 peaks (rows) from 669 samples (columns). The column names are ROSMAP project IDs (eight digit #) and row names are peak No. (peak_#), sorted by asending chromosome number and start location.

The H3K9acDomains.csv contains peak info summarized as follows: chr, start, end, width (length of peak region), strand, log10p, log10q, foldEnrichment(fold enrichment for this peak summit against random Poisson distribution with local lambda), pileup (pileup height at peak summit), name (peak_#), blacklist (blacklist True/False according to `/mnt/mfs/ctcn/resources/encodeBlacklists/hg38-blacklist.v2.clean.bed.gz`). 


## Links to omics data analysis notebooks

### Peak calling

Peaks were generated via the following workflow: [hak9ac_calling](https://github.com/cumc/xqtl-pipeline/tree/main/code/misc/h3k9ac_calling)

### Exploratory analysis

See notebooks in: 

- https://github.com/cumc/fungen-xqtl-analysis/tree/main/analysis/Wang_Columbia/ROSMAP/haqtl

The notebooks in this folder contain the commands and data wrangling codes for analysis of the h3k9ac data in ROSMAP. (data wrangling exist because not all data are processed using the xqtl-pipeline from the begnning and need to be reformated to fit one intermediate step of the pipeline).

1. [h3k9ac_exploratory_analysis.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/haqtl/h3k9ac_exploratory_analysis.ipynb) provides information about the data source.

2. [annotate_peaks_to_gene.ipynb](https://github.com/cumc/fungen-xqtl-analysis/blob/main/analysis/Wang_Columbia/ROSMAP/haqtl/annotate_peaks_to_gene.ipynb) a record of steps used to annotate each h3k9ac peaks to genes using tabix. Each peak was mapped with multiple genes according to start and end overlap and kept as an reference.