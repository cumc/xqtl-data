# (file name and title see naming convention under https://github.com/cumc/fungen-xqtl-analysis/tree/main/data/descriptor/integration and follow this convention)

A brief overview of cohorts and QTL/GWAS studies used in this analysis, and the methods used.

## Contact

The lead analysts of the data and also the persons responsible for maintaining this document.

## Resource integrated

Links to **each** data descriptor of QTL/GWAS data used, eg:

- https://github.com/cumc/fungen-xqtl-analysis/blob/main/data/descriptor/qtl/ROSMAP_DLPFC_expression_qtl.md
- https://github.com/cumc/fungen-xqtl-analysis/blob/main/data/descriptor/qtl/ROSMAP_PCC_expression_qtl.md
- https://github.com/cumc/fungen-xqtl-analysis/blob/main/data/descriptor/qtl/ROSMAP_AC_expression_qtl.md

## List of methods used

For example,

- MASH
- mvSuSiE

## Dataset Details

### Path(s) to integration results

Here please document the results 

- Path(s) to the results on your local cluster where you analyzed the data. For example:
- Zhang Lab, `/restricted/projectnb/casa/skandoi/ROSMAP/ROSMAP_MASH/`
- This section may contain multiple locations in which case you can use bullet points to separate them. 
- If the lead analysts are from different institutes please include all the paths. 

A summary of the data including size. We suggest using `ls -lh` command to show them. For example:

```
$ ls -lh *.{bim,bed,fam}
-rw-rw-r-- 1 gw gw  2.7M Apr  5  2017 ROSMAP_MASH.strong.rds
-rw-rw-r-- 1 gw gw  2.7M Apr  5  2017 ROSMAP_MASH.flash_model.rds
```

## Links to integration analysis notebooks

Please list the links to analysis notebooks in the order you executed our pipeline:

1. ...
2. ...

Alternatively you can also use a somewhat free style as long as it is clear from your write-up where the notebooks are on github and what they are.