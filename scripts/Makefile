SHELL := /bin/bash

outdir = _out
md_out = $(outdir)/processed_md
html_out = $(outdir)/html
content_root = content
concept_map = example_map.yaml

all: $(md_out) $(html_out)
clean:
	rm -r $(outdir)

$(outdir):
	mkdir -p $(outdir)

$(md_out): $(outdir)
	mkdir -p $(md_out)
	find $(content_root) -type d | xargs -I XX mkdir -p $(md_out)/XX 
	find $(content_root) -type f -name "*.md" | parallel "./process_file.py $(concept_map) {} > $(md_out)/{}"

$(html_out): $(md_out)
	mkdir -p $(html_out)
	find $(md_out) -type d | sed 's:$(md_out)::' | xargs -I XX mkdir -p $(html_out)/XX
	find $(md_out) -type f -name "*.md" | sed 's:$(md_out)/::'| parallel "./md_to_html.sh $(md_out) $(html_out) {}" \;
