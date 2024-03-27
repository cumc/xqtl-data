# Non-Hispanic White Linkage Disequilibrium Reference Panel
Correlation matrices were calculated between SNPs within 1361 LD blocks which were obtained from [this Github page](https://github.com/jmacdon/LDblocks_GRCh38/) (generated from 1000 Genomes EUR samples). Actual correlations values were calculated from whole genome sequencing data from 16571 non-Hispanic white individuals obtained from the Genome Center for Alzheimer's Disease (GCAD).

## Contact
Oluwatosin Olayinka

## Output Format
Each LD block contains two files of interest:
- an xz-compressed file containing the correlation values, suffixed by `.cor.xz`
    - this file is a compressed file where the matrix is encoded in a space-separated format 
    - the data is stored in the upper triangle of the matrix
- a [Plink `.bim`](https://www.cog-genomics.org/plink/1.9/formats#bim) file suffixed by `.cor.xz.bim` containing unique IDs for each variant

```{r}
ld_block_ref_file = "/path/to/matrix.cor.xz"
var_names = read.table(paste0(ld_block_ref_file, ".bim"), header = F)$V2
ld <- scan(xzfile(ld_block_ref_file))
ld <- matrix(ld, ncol = sqrt(length(ld)), byrow = TRUE)
ld <- ld + t(ld)
diag(ld) = 1
rownames(ld) = var_names
colnames(ld) = var_names
```

## Data Availability
The generated files can be found on [Synapse](https://www.synapse.org/#!Synapse:syn53171227).

## Analysis Notebook Link
1. Generating LD Reference Panel: https://github.com/cumc/xqtl-pipeline/blob/main/code/reference_data/ld_reference_generation.ipynb
