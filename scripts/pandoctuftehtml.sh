#!/bin/bash
PATH=$PATH:/usr/texbin:/usr/local/bin

cd "$TM_PROJECT_DIRECTORY"/book
pandoc -s -o book.html book.md  --css=css/tufte.css --css=css/user.css --to=html5
