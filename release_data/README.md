# QTL Analysis Results 

## Overview

This repository contains Quantitative Trait Loci (QTL) analysis results from multiple datasets, focusing on various contexts and biological systems. The data includes expression QTLs (eQTLs), protein QTLs (pQTLs), and splicing QTLs (sQTLs) across different brain regions and cell types.

## Dataset Breakdown

### Single Context Analyses

#### KNIGHT QTLs
- **KNIGHT eQTL**: Brain-specific expression quantitative trait loci  
  - Path: `/data/analysis_result/single_context/KNIGHT_eQTL/export/summary/context_specific/Knight_eQTL_brain.exported.toploci.bed.gz`
- **KNIGHT pQTL**: Brain-specific protein quantitative trait loci  
  - Path: `/data/analysis_result/single_context/KNIGHT_pQTL/export/summary/context_specific/Knight_pQTL_brain.exported.toploci.bed.gz`

#### MSBB QTLs
- **MSBB eQTL**: Expression QTLs across multiple brain regions (BM 10, 22, 36, 44)  
  - Path: `/data/analysis_result/single_context/MSBB_eQTL/export/summary/context_specific/BM_[10|22|36|44]_MSBB_eQTL.exported.toploci.bed.gz`
- **MSBB pQTL**: Protein QTLs for BM36  
  - Path: `/data/analysis_result/single_context/MSBB_pQTL/export/summary/context_specific/MSBB_BM36_pQTL.exported.toploci.bed.gz`

#### MetaBrain
- Brain region-specific QTLs including:
  - Basal Ganglia  
  - Cerebellum  
  - Cortex  
  - Hippocampus  
  - Spinal Cord  
  - Path: `/data/analysis_result/single_context/MetaBrain/export/summary/context_specific/Metabrain_[Basalganglia|Cerebellum|Cortex|Hippocampus|Spinalcord].exported.toploci.bed.gz`

#### MiGA eQTL
- Expression QTLs across:
  - GFM  
  - GTS  
  - SVZ  
  - THA  
  - Path: `/data/analysis_result/single_context/MiGA_eQTL/export/summary/context_specific/MiGA_[GFM|GTS|SVZ|THA]_eQTL.exported.toploci.bed.gz`

#### ROSMAP bulk eQTLs
- Brain region-specific eQTLs including:
  - AC  
  - DLPFC  
  - PCC  
  - Path: `/data/analysis_result/single_context/ROSMAP_eQTL/export/summary/[AC|DLPFC|PCC]_DeJager_eQTL.exported.toploci.bed.gz`

#### ROSMAP pseudobulk eQTLs
- **Cell type–specific QTLs** (from De Jager, Kellis, and combined "mega" datasets):  
  - **Cell types**:  
    - Astrocytes  
    - Excitatory neurons  
    - Inhibitory neurons  
    - Microglia  
    - OPC  
    - Oligodendrocytes  
  - **Path pattern**:  
    `/data/analysis_result/single_context/ROSMAP_eQTL/export/summary/context_specific/[Ast|Exc|Inh|Mic|OPC|Oli]_[DeJager|Kellis|mega]_eQTL.exported.toploci.bed.gz`

- **Subcell type–specific QTLs** (Kellis only):  
  - **Subclusters**:  
    - Astrocyte subcluster 10  
    - Microglia subcluster 12  
    - Microglia subcluster 13  
  - **Path pattern**:  
    `/data/analysis_result/single_context/ROSMAP_eQTL/export/summary/context_specific/[Ast_10|Mic_12|Mic_13]_Kellis_eQTL.exported.toploci.bed.gz`

- **Monocyte**:  
  - Path: `/data/analysis_result/single_context/ROSMAP_pQTL/export/summary/context_specific/monocyte_ROSMAP_eQTL.exported.toploci.bed.gz`

#### ROSMAP pQTLs
- pQTL for DLPFC  
- Adjusted glycoprotein for DLPFC  
- Unadjusted glycoprotein for DLPFC  
  - Path: `/data/analysis_result/single_context/ROSMAP_pQTL/export/summary/context_specific/DLPFC_[Bennett_pQTL|Klein_gpQTL_adjusted|Klein_gpQTL_unadjusted].exported.toploci.bed.gz`

#### ROSMAP sQTLs
- Brain region-specific sQTLs including:
  - AC  
  - DLPFC  
  - PCC  
  - Path: `/data/analysis_result/single_context/ROSMAP_sQTL/export/summary/ROSMAP_[AC|DLPFC|PCC]_sQTL.exported.toploci.bed.gz`

#### STARNET eQTL
- Macrophage-specific expression QTLs  
  - Path: `/data/analysis_result/single_context/STARNET_eQTL/export/summary/context_specific/STARNET_eQTL_Mac.exported.toploci.bed.gz`

### Multi-Context and Advanced Analyses

#### Multi Context
- Integrated QTL analyses for:
  - **MSBB**: `/data/analysis_result/multi_context/MSBB/export/summary/MSBB.exported.toploci.bed.gz`
  - **ROSMAP**: `/data/analysis_result/multi_context/ROSMAP/export/summary/ROSMAP.exported.toploci.bed.gz`

#### Multi Gene
- Gene-specific QTL analyses:

  - **MSBB**:  
    ```
    /data/analysis_result/multi_gene/MSBB/export/summary/context_specific/MSBB_BM_10_eQTL.exported.toploci.bed.gz
    /data/analysis_result/multi_gene/MSBB/export/summary/context_specific/MSBB_BM_22_eQTL.exported.toploci.bed.gz
    /data/analysis_result/multi_gene/MSBB/export/summary/context_specific/MSBB_BM_36_eQTL.exported.toploci.bed.gz
    /data/analysis_result/multi_gene/MSBB/export/summary/context_specific/MSBB_BM_44_eQTL.exported.toploci.bed.gz
    ```

  - **ROSMAP**:  
    ```
    /data/analysis_result/multi_gene/ROSMAP/export/summary/context_specific/ROSMAP_AC_DeJager_eQTL.exported.toploci.bed.gz
    /data/analysis_result/multi_gene/ROSMAP/export/summary/context_specific/ROSMAP_Ast_DeJager_eQTL.exported.toploci.bed.gz
    /data/analysis_result/multi_gene/ROSMAP/export/summary/context_specific/ROSMAP_Ast_mega_eQTL.exported.toploci.bed.gz
    /data/analysis_result/multi_gene/ROSMAP/export/summary/context_specific/ROSMAP_DLPFC_Bennett_pQTL.exported.toploci.bed.gz
    /data/analysis_result/multi_gene/ROSMAP/export/summary/context_specific/ROSMAP_DLPFC_DeJager_eQTL.exported.toploci.bed.gz
    /data/analysis_result/multi_gene/ROSMAP/export/summary/context_specific/ROSMAP_Exc_DeJager_eQTL.exported.toploci.bed.gz
    /data/analysis_result/multi_gene/ROSMAP/export/summary/context_specific/ROSMAP_Exc_mega_eQTL.exported.toploci.bed.gz
    /data/analysis_result/multi_gene/ROSMAP/export/summary/context_specific/ROSMAP_Inh_DeJager_eQTL.exported.toploci.bed.gz
    /data/analysis_result/multi_gene/ROSMAP/export/summary/context_specific/ROSMAP_Inh_mega_eQTL.exported.toploci.bed.gz
    /data/analysis_result/multi_gene/ROSMAP/export/summary/context_specific/ROSMAP_Mic_DeJager_eQTL.exported.toploci.bed.gz
    /data/analysis_result/multi_gene/ROSMAP/export/summary/context_specific/ROSMAP_Mic_mega_eQTL.exported.toploci.bed.gz
    /data/analysis_result/multi_gene/ROSMAP/export/summary/context_specific/ROSMAP_OPC_DeJager_eQTL.exported.toploci.bed.gz
    /data/analysis_result/multi_gene/ROSMAP/export/summary/context_specific/ROSMAP_OPC_mega_eQTL.exported.toploci.bed.gz
    /data/analysis_result/multi_gene/ROSMAP/export/summary/context_specific/ROSMAP_Oli_DeJager_eQTL.exported.toploci.bed.gz
    /data/analysis_result/multi_gene/ROSMAP/export/summary/context_specific/ROSMAP_Oli_mega_eQTL.exported.toploci.bed.gz
    /data/analysis_result/multi_gene/ROSMAP/export/summary/context_specific/ROSMAP_PCC_DeJager_eQTL.exported.toploci.bed.gz
    /data/analysis_result/multi_gene/ROSMAP/export/summary/context_specific/ROSMAP_monocyte_ROSMAP_eQTL.exported.toploci.bed.gz
    ```

#### Trans Analyses
- Includes trans-fine-mapping across most of the single-context datasets listed above  
- Paths:
```
/data/analysis_result/finemapping_twas_trans/export/summary/context_specific/Knight_eQTL.exported.toploci.bed.gz
/data/analysis_result/finemapping_twas_trans/export/summary/context_specific/Knight_pQTL.exported.toploci.bed.gz
/data/analysis_result/finemapping_twas_trans/export/summary/context_specific/MSBB_eQTL_BM10.exported.toploci.bed.gz
/data/analysis_result/finemapping_twas_trans/export/summary/context_specific/MSBB_eQTL_BM22.exported.toploci.bed.gz
/data/analysis_result/finemapping_twas_trans/export/summary/context_specific/MSBB_eQTL_BM36.exported.toploci.bed.gz
/data/analysis_result/finemapping_twas_trans/export/summary/context_specific/MSBB_eQTL_BM44.exported.toploci.bed.gz
/data/analysis_result/finemapping_twas_trans/export/summary/context_specific/MSBB_pQTL.exported.toploci.bed.gz
/data/analysis_result/finemapping_twas_trans/export/summary/context_specific/MiGA_eQTL_GFM.exported.toploci.bed.gz
/data/analysis_result/finemapping_twas_trans/export/summary/context_specific/MiGA_eQTL_GTS.exported.toploci.bed.gz
/data/analysis_result/finemapping_twas_trans/export/summary/context_specific/MiGA_eQTL_SVZ.exported.toploci.bed.gz
/data/analysis_result/finemapping_twas_trans/export/summary/context_specific/MiGA_eQTL_THA.exported.toploci.bed.gz
/data/analysis_result/finemapping_twas_trans/export/summary/context_specific/ROSMAP_DeJager_AC.exported.toploci.bed.gz
/data/analysis_result/finemapping_twas_trans/export/summary/context_specific/ROSMAP_DeJager_Ast.exported.toploci.bed.gz
/data/analysis_result/finemapping_twas_trans/export/summary/context_specific/ROSMAP_DeJager_DLPFC.exported.toploci.bed.gz
/data/analysis_result/finemapping_twas_trans/export/summary/context_specific/ROSMAP_DeJager_Exc.exported.toploci.bed.gz
/data/analysis_result/finemapping_twas_trans/export/summary/context_specific/ROSMAP_DeJager_Inh.exported.toploci.bed.gz
/data/analysis_result/finemapping_twas_trans/export/summary/context_specific/ROSMAP_DeJager_Mic.exported.toploci.bed.gz
/data/analysis_result/finemapping_twas_trans/export/summary/context_specific/ROSMAP_DeJager_OPC.exported.toploci.bed.gz
/data/analysis_result/finemapping_twas_trans/export/summary/context_specific/ROSMAP_DeJager_Oli.exported.toploci.bed.gz
/data/analysis_result/finemapping_twas_trans/export/summary/context_specific/ROSMAP_DeJager_PCC.exported.toploci.bed.gz
/data/analysis_result/finemapping_twas_trans/export/summary/context_specific/ROSMAP_DeJager_monocyte.exported.toploci.bed.gz
/data/analysis_result/finemapping_twas_trans/export/summary/context_specific/ROSMAP_DeJager_pQTL.exported.toploci.bed.gz
/data/analysis_result/finemapping_twas_trans/export/summary/context_specific/ROSMAP_Kelli_Ast.exported.toploci.bed.gz
/data/analysis_result/finemapping_twas_trans/export/summary/context_specific/ROSMAP_Kelli_Exc.exported.toploci.bed.gz
/data/analysis_result/finemapping_twas_trans/export/summary/context_specific/ROSMAP_Kelli_Inh.exported.toploci.bed.gz
/data/analysis_result/finemapping_twas_trans/export/summary/context_specific/ROSMAP_Kelli_Mic.exported.toploci.bed.gz
/data/analysis_result/finemapping_twas_trans/export/summary/context_specific/ROSMAP_Kelli_OPC.exported.toploci.bed.gz
/data/analysis_result/finemapping_twas_trans/export/summary/context_specific/ROSMAP_Kelli_Oli.exported.toploci.bed.gz
/data/analysis_result/finemapping_twas_trans/export/summary/context_specific/ROSMAP_mega_Ast.exported.toploci.bed.gz
/data/analysis_result/finemapping_twas_trans/export/summary/context_specific/ROSMAP_mega_Exc.exported.toploci.bed.gz
/data/analysis_result/finemapping_twas_trans/export/summary/context_specific/ROSMAP_mega_Inh.exported.toploci.bed.gz
/data/analysis_result/finemapping_twas_trans/export/summary/context_specific/ROSMAP_mega_Mic.exported.toploci.bed.gz
/data/analysis_result/finemapping_twas_trans/export/summary/context_specific/ROSMAP_mega_OPC.exported.toploci.bed.gz
/data/analysis_result/finemapping_twas_trans/export/summary/context_specific/ROSMAP_mega_Oli.exported.toploci.bed.gz
/data/analysis_result/finemapping_twas_trans/export/summary/context_specific/ROSMAP_metabolome.exported.toploci.bed.gz
/data/analysis_result/finemapping_twas_trans/export/summary/context_specific/STARNET_eQTL.exported.toploci.bed.gz
```
## File Naming Convention

Files are typically named with the following pattern:  
`[Dataset]_[CellType/Region]_[QTLType].exported.toploci.bed.gz`

- **Datasets**: KNIGHT, MSBB, MetaBrain, MiGA, ROSMAP, STARNET  
- **Cell Types/Regions**: AC, DLPFC, Ast, Exc, Inh, Mic, OPC, Oli, etc.  
- **QTL Types**: eQTL, pQTL, sQTL

## Usage Notes

1. All files are compressed (`.gz`) BED format  
2. Represents top loci from respective QTL analyses  
3. Suitable for downstream genomic and transcriptomic research  
4. For context definitions in each top loci table, see below: 

### Table Summary
- Each row represents a single variant associated with a gene in a specific context (e.g., tissue or study).

### Column Descriptions

| Column Name           | Type      | Description                                                                 |
|-----------------------|-----------|-----------------------------------------------------------------------------|
| `chr`                 | integer   | Chromosome number                                                           |
| `start`               | integer    | Genomic start coordinate (0-based)                                          |
| `end`                 | integer   | Genomic end coordinate (1-based)                                            |
| `a1`                  | character | Effect allele                                                               |
| `a2`                  | character | Reference allele                                                            |
| `variant_ID`          | character | Unique variant ID in format `chr:pos:ref:alt`                               |
| `gene_ID`             | character | Ensembl gene ID                                                             |
| `event_ID`            | character | Unique event ID for QTL signal (context + gene). Only present if lfsr passed |
| `cs_coverage_0.95`    | integer   | cs index if variant is in 95% credible set with minimum correlation purity > 0.8, else 0                          |
| `cs_coverage_0.7`     | integer   | cs index if variant is in 70% credible set with minimum correlation purity > 0.8, else 0                          |
| `cs_coverage_0.5`     | integer   | cs index if variant is in 50% credible set with minimum correlation purity > 0.8, else 0                          |
| `cs_coverage_0.95_purity0.5`    | integer   | When available, the CS index if the variant is in the 95% credible set with minimum correlation purity > 0.5; else 0 |
| `cs_coverage_0.7_purity0.5`    | integer   | When available, the CS index if the variant is in the 70% credible set with minimum correlation purity > 0.5; else 0 |
| `cs_coverage_0.5_purity0.5`    | integer   | When available, the CS index if the variant is in the 50% credible set with minimum correlation purity > 0.5; else 0 |
| `PIP`                 | double    | Posterior inclusion probability for causality                               |
| `conditional_effect`  | double    | Effect size from conditional model                                          |
| `lfsr`                | double    | Only in multi conetxt or multi gene results. Local False Sign Rate: the probability that the estimated effect has the wrong sign. Lower values indicate higher confidence in the direction of the effect. Variants without an lfsr value (i.e., NA) did not pass the filtering threshold in multi-context fine-mapping and are retained for reference only |                            |


### Notes

- This table may include results from multi-context or multi-gene analyses.
- Rows with missing `event_ID` indicate variants from multi-context analyses that did not pass the LFSR filtering threshold.
- The `cs_coverage_*` columns indicate membership in posterior credible sets of varying coverage (95%, 70%, 50%).


### Usage Tips

- Filter rows by `cs_coverage_0.95` or `PIP` to prioritize candidate causal variants.
- Restrict to rows with non-missing `event_ID` for significance-filtered analysis.
- For visualization, group by `context` and `gene_ID` to examine gene-level credible sets across studies.
