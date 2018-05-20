#!/bin/bash
PATH=$PATH:/usr/texbin:/usr/local/bin

cd "$TM_PROJECT_DIRECTORY"/book
pandoc --latex-engine=xelatex book.md -o book.tex --chapters --toc -V geometry=a4paper,left=3cm,right=2cm,bottom=2cm,top=2cm  -V lang=german -H myheader.tex -V fontsize=12pt


