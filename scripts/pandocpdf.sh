#!/bin/bash
PATH=$PATH:/usr/texbin:/usr/local/bin

cd "$TM_PROJECT_DIRECTORY"/book
pandoc -o book.pdf book.md -s  --chapters --toc --latex-engine=xelatex  -V geometry=a5paper,left=3cm,right=2cm,bottom=2cm,top=2cm  -V lang=german -H myheader.tex -V fontsize=10pt
