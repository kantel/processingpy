#!/bin/bash
PATH=$PATH:/usr/texbin:/usr/local/bin

cd "$TM_PROJECT_DIRECTORY"/book
pandoc --latex-engine=xelatex -o book.pdf book.md -s --chapters --toc --template eisvogel --listings -V lang=de
