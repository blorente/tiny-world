#!/bin/bash
set -xe
md_out=$1
html_out=$2
style_file=$3
template_file=$4
md=$5
filename=$(echo $md | sed 's:.md::')
path_to_style="/$style_file"
pandoc --standalone -f markdown -t html "${md_out}/${md}" -o "${html_out}/${filename}.html" --css="${path_to_style}" --template "${template_file}" --toc --toc-depth=2
