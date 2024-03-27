SHELL := /bin/bash
toc:
	python3 toc.py descriptor/{gwas,omics,qtl,integration}/*.md -o README.md -t "FunGen-xQTL data catalog" -b "https://github.com/cumc/fungen-xqtl-analysis/tree/main/data/" -c "Lead analysts: "

