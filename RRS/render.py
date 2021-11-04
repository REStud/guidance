from jinja2 import Template
from docxtpl import DocxTemplate
from yaml import load

version = '1.0'

def render_list(lst):
    return ' \n| | |'.join(['({}) {}'.format(chr(ord('a') + i), item) for i, item in enumerate(lst)])

def apply(item):
    if isinstance(item, list):
        return render_list(item)
    if isinstance(item, dict):
        return {key: apply(item[key]) for key in item}
    return item

file_name = 'Reproducible-Research-Standard'
#doc = DocxTemplate(f'{file_name}.docx')
md = Template(open(f'{file_name}.md', 'rt').read())
codebook = load(open(f'codebook.yaml'))
content = apply(load(open(f'content.yaml')))
content['version'] = version

payload = dict(content=content, codebook=codebook)

# save .md
with open(f'{file_name}-{version}.md', 'wt') as file:
    file.write(md.render(payload))

# then .docx
#doc.render(context)
#doc.save(f'{file_name}-{version}.docx')
