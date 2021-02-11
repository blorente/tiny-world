#!/bin/bash
md_out=$1
html_out=$2
md=$3
filename=$(echo $md | sed 's:.md::')
pandoc "${md_out}/${md}" > "${html_out}/${filename}.html"