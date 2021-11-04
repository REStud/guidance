---
papersize: a4
geometry:
- top=20mm
- left=20mm
- right=20mm
- bottom=20mm
- heightrounded
---
# Reproducible Research Standard v{{ content.version }}
## What to include in the replication package and in the README document

{% set count = namespace(value=0) %}
| | Item No | Rule | Policy |
|---|-|-------|-|{% for group in codebook.root %}
| **{{ codebook['root'][group] }}** |{% for topic in codebook[group] %}{% set count.value = count.value + 1 %}
| {{ codebook[group][topic] }} | {{ count.value }} | {{ content[group][topic] }} | | {% endfor %}{% endfor %}

All participating journals value all rules, but the levels of enforcement may vary. For each rule, journal policy may be "Verified", "Required" or "Recommended."