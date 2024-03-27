# ROSMAP snRNA-seq pseudo-bulk gene expression 

Religious Orders Study (ROS) or the Rush Memory and Aging Project (MAP) snRNA-seq from different cells in Dorsolateral Prefrontal Cortex (DLPFC). 

Please refer to [this document](../study_info/ROSMAP.md) for an overview of the ROSMAP project.

## Contact

Hao Sun and Masashi Fujita

## Study Overview

- Grant number : R01 AG076901 (temporary using Gao's grant number)
- Publication : 
- Acknowledgement : 
- Study name : ROSMAP snRNA-seq pseudo-bulk gene expression
- Study Description : 
- Disease : Alzheimer’s Disease
- Data Citation : https://www.synapse.org/#!Synapse:syn23650894
- Additional study information : 

## Dataset Description

### Raw data

FIXME: need Masashi's input here

**Biosample:**

Extracted as single cell from dorsolateral prefrontal cortex, pooled at data level.

**Sample processing:**

Dorsolateral Prefrontal Cortex (DLFPC) tissue specimens from 465 unique individuals were received frozen from the Rush Alzheimer’s Disease Center. We observed variability in the morphology of these tissue specimens with differing amounts of gray and white matter and presence of attached meninges. Working on ice throughout, we carefully dissected to remove white matter and meninges, when present. The following steps were also conducted on ice: about 50-100mg of gray matter tissue was transferred into the dounce homogenizer (Sigma Cat No: D8938) with 2mL of NP40 Lysis Buffer (0.1% NP40, 10mM Tris, 146mM NaCl, 1mM CaCl2, 21mM MgCl2, 40U/mL of RNAse inhibitor (Takara: 2313B)). Tissue was gently dounced while on ice 25 times with Pestle A followed by 25 times with Pestle B, then transferred to a 15mL conical tube. 3mL of PBS + 0.01% BSA (NEB B9000S) and 40U/mL of RNAse inhibitor were added for a final volume of 5mL and then immediately centrifuged with a swing bucket rotor at 500g for 5 mins at 4°C. Samples were processed 2 at a time, the supernatant was removed, and the pellets were set on ice to rest while processing the remaining tissues to complete a batch of 8 samples. The nuclei pellets were then resuspended in 500ml of PBS + 0.01% BSA and 40U/mL of RNAse inhibitor. Nuclei were filtered through 20um pre-separation filters (Miltenyi: 130-101-812) and counted using the Nexcelom Cellometer Vision and a 2.5ug/ul DAPI stain at 1:1 dilution with cellometer cell counting chamber (Nexcelom CHT4-SD100-002).

**Platform:**

RNA:NextSeq500 , DNA:Illumina HiSeq X sequencer

### Molecular phenotype matrices

This data contains already normalized log2cpm with 425 samples as columns and 14426 gene ids as rows.

- Wang Lab: `/mnt/mfs/statgen/snuc_pseudo_bulk/data/phenotype_data_all/ALL.log2cpm.tsv` (115M)

The number of samples in each of the tissues is as followed (only the eight tissues with > 400 samples are used in the eQTL analysis in Gao Wang's Lab).

```
cd /mnt/mfs/statgen/snuc_pseudo_bulk/data/phenotype_data_all
for i in `ls /mnt/mfs/ctcn/team/masashi/snuc-eqtl/v20211109.celltypes/`; do echo $i;  head -1 ../phenotype_data_all/$i.log2cpm.tsv | wc -l ; done
```

| Tissue      | # samples |
| -----------| ----------- |
| ALL        | 425         |
| Ast        | 425         |
| End        | 362         |
| Exc        | 425         |
| Fib        | 118         |
| Inh        | 425         |
| Mac        | 52          |
| Mic        | 425         |
| NFOL       | 259         |
| OPC        | 424         |
| Oli        | 425         |
| Peri       | 94          |
| SMC        | 22          |

Cell type-specific expression data:

- De Jager Lab: `/mnt/mfs/ctcn/team/masashi/snuc-eqtl/v20211109.celltypes`

Here, I use astrocytes as an example. But all other cell types have the same folder structure.

- Gene expression matrix of astrocyte, De Jager Lab：`/mnt/mfs/ctcn/team/masashi/snuc-eqtl/v20211109.celltypes/Ast/Ast.log2cpm.tsv`

### Other key data files

Annotations used by De Jager Lab analysis

- Transcription start sites (TSS) of genes in GRCh38, De Jager Lab: `/mnt/mfs/ctcn/team/masashi/snuc-eqtl/transcriptome/get-tss-pos.tsv`
- GTF file used to generate the TSS file, De Jager Lab: `/mnt/mfs/ctcn/team/masashi/snuc-eqtl/transcriptome/genes.gtf`