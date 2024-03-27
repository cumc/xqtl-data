# xQTL summary statistics file schema

This file includes description of column contents in the summary statisitcs files. Summary statisics using the xqtl-pipeline should share the same column contents as shown below, but adjustments are welcome.

## Contact

Hao Sun

## TensorQTL Nominal cis Associations (txt file)

- chromosome : GRCh38 chromosome name of the variant (e.g. 1,2,3 ...,X).
- position : GRCh38 position of the variant.
- ref : GRCh38 reference allele.
- alt : GRCh38 alternative allele.
- variant : The variant ID (chromosome_position_ref_alt) e.g. chr19_226776_C_T. Based on GRCh38 coordinates and reference genome, with 'chr' prefix added to the chromosome number.
- beta : Regression coefficient from the linear model.
- se : Standard error of the beta.
- pvalue : Nominal P-value from linear regression
- TSS D : Distance of the SNP to the gene transcription start site (TSS)
- maf : minor allele frequency
- n : Total number of samples without missing data.
- ma samples : Number of samples carrying at least one copy of the minor allele.
- ac : Count of the alternative allele. 
- molecular trait id : ID of the molecular trait used for QTL mapping. Depending on the quantification method used, this can be either a gene id, exon id, transcript id or a txrevise promoter, splicing or 3'end event id. Examples: ENST00000356937, ENSG00000008128.  
- molecular trait object id : For phenotypes with multiple correlated alternatives (multiple alternative transcripts or exons within a gene, multple alternative promoters in txrevise, multiple alternative intons in Leafcutter), this defines the level at which the phenotypes were aggregated. Permutation p-values are calculated across this set of alternatives.

## TensorQTL Empirical Summary Statistics (txt file)

- beta shape1 : First parameter value of the fitted beta distribution
- beta shape2 : Second parameter value of the fitted beta distribution
- true df : Effective degrees of freedom the beta distribution approximation
- pval true df : Empirical P-value for the beta distribution approximation
- variant : ID of the top variant (rsid or chr:position:ref:alt)
- tss distance : Distance of the SNP to the gene transcription start site (TSS)
- ma samples : Number of samples carrying the minor allele
- ma count : Total number of minor alleles across individuals
- af : allele frequency of top variant
- ref factor : Flag indicating if the alternative allele is the minor allele in the cohort (1 if AF <= 0.5, -1 if not)
- pval nominal : Nominal P-value from linear regression for top variant
- slope : Slope of the linear regression
- slope se : Standard error of the slope
- p perm : First permutation P-value directly obtained from the permutations with the direct method
- p beta : Second permutation P-value obtained via beta approximation. This is the one to use for downstream analysis
- n traits : number of molecular trait
- molecular trait object id : For phenotypes with multiple correlated alternatives (multiple alternative transcripts or exons within a gene, multple alternative promoters in txrevise, multiple alternative intons in Leafcutter), this defines the level at which the phenotypes were aggregated. Permutation p-values are calculated across this set of alternatives.
- molecular trait id : ID of the molecular trait used for QTL mapping. Depending on the quantification method used, this can be either a gene id, exon id, transcript id or a txrevise promoter, splicing or 3'end event id. Examples: ENST00000356937, ENSG00000008128.  
- n variants : Number of variants in the cis region of that trait
- inflation factor : lambda genomics inflation factor
- q beta : the genome wide Q value for p_beta
- q perm : the genome wide Q value for p_perm
- fdr beta : the genome wide FDR value for p_beta
- fdr perm : the genome wide FDR value for p_perm