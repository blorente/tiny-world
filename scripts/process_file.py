#!/usr/bin/python3

import sys
import re
import yaml
from pathlib import Path
from typing import Dict

def load_map(mapfile: Path) -> Dict[str, str]:
    return yaml.safe_load(mapfile.open())

def process_links(original: str, concept_map: Dict[str, str]) -> str:
    processed = original
    for (concept, link) in concept_map.items():
        link = link.replace(".md", ".html")
        processed = processed.replace(f"@{concept}", f"[{concept}]({link})")
    return processed


mapfile=Path(sys.argv[1])
infile=Path(sys.argv[2])

concept_map = load_map(mapfile)
# print(concept_map, file=sys.stderr)
print(process_links(infile.read_text(), concept_map))