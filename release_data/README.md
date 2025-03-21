
# Variant-Level Fine-Mapping Results

This document describes the structure and interpretation of a fine-mapping results table containing variant-level posterior probabilities and credible set assignments across multiple contexts and genes.

## Table Summary
- Each row represents a single variant associated with a gene in a specific context (e.g., tissue or study).

## Column Descriptions

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
| `cs_coverage_0.95`    | integer   | cs index if variant is in 95% credible set, else 0                          |
| `cs_coverage_0.7`     | integer   | cs index if variant is in 70% credible set, else 0                          |
| `cs_coverage_0.5`     | integer   | cs index if variant is in 50% credible set, else 0                          |
| `PIP`                 | double    | Posterior inclusion probability for causality                               |
| `conditional_effect`  | double    | Effect size from conditional model                                          |
| `lfsr`                | double    | Only in multi conetxt or multi gene results. Local False Sign Rate: the probability that the estimated effect has the wrong sign. Lower values indicate higher confidence in the direction of the effect. Variants without an lfsr value (i.e., NA) did not pass the filtering threshold in multi-context fine-mapping and are retained for reference only |                            |


## Notes

- This table may include results from multi-context or multi-gene analyses.
- Rows with missing `event_ID` indicate variants from multi-context analyses that did not pass the LFSR filtering threshold.
- The `cs_coverage_*` columns indicate membership in posterior credible sets of varying coverage (95%, 70%, 50%).


## Usage Tips

- Filter rows by `cs_coverage_0.95` or `PIP` to prioritize candidate causal variants.
- Restrict to rows with non-missing `event_ID` for significance-filtered analysis.
- For visualization, group by `context` and `gene_ID` to examine gene-level credible sets across studies.
