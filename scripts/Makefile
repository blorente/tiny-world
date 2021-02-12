SHELL := /bin/bash

content_root = tiny-world
style_file = $(content_root)/water.css
concept_map = "$(content_root)/concept_map.yaml"

outdir = _out
md_out = $(outdir)/processed_md
html_out = $(outdir)/html

scripts = scripts
html_template = $(scripts)/template.html

all: $(html_out)/index.html
clean:
	rm -r $(outdir)

$(outdir):
	mkdir -p $(outdir)

$(md_out): $(outdir)
	mkdir -p $(md_out)
	find $(content_root) -type d | xargs -I XX mkdir -p $(md_out)/XX 
	find $(content_root) -type f -name "*.md" | parallel "./scripts/process_file.py $(concept_map) {} > $(md_out)/{}"

$(html_out): $(md_out)
	mkdir -p $(html_out)
	find $(md_out) -type d | sed 's:$(md_out)::' | xargs -I XX mkdir -p $(html_out)/XX
	cp $(style_file) $(html_out)/$(content_root)
	find $(md_out) -type f -name "*.md" | sed 's:$(md_out)/::'| parallel "./scripts/md_to_html.sh $(md_out) $(html_out) $(style_file) $(html_template) {}" \;

$(html_out)/index.html: $(html_out)
	(cd $(html_out) && tree -H '.' --noreport --charset utf-8 -P "*.html" > index.html)
	 
