#!/bin/bash
PATH=$PATH:/usr/texbin:/usr/local/bin

cd "$TM_PROJECT_DIRECTORY"/book
pandoc -o book.pdf book.md  --latex-engine=xelatex  -V geometry:margin=1in -V lang=german
