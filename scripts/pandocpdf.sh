#!/bin/bash
PATH=$PATH:/usr/texbin:/usr/local/bin

cd "$TM_PROJECT_DIRECTORY"/book
pandoc --latex-engine=xelatex book.md -o book.pdf --chapters --highlight-style tango --toc -V geometry=a4paper,left=3cm,right=3cm,bottom=3cm,top=3cm  -V lang=german -H myheader.tex -V fontsize=12pt
