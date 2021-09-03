from jinja2 import Template
from docxtpl import DocxTemplate
from yaml import load

version = '1.0'

def render_list(lst):
    return ' '.join(['({}) {}'.format(chr(ord('a') + i), item) for i, item in enumerate(lst)])

def apply(item):
    if isinstance(item, list):
        return render_list(item)
    if isinstance(item, dict):
        return {key: apply(item[key]) for key in item}
    return item

for file_name in ['Report', 'Share']:
    doc = DocxTemplate(f'{file_name}.docx')
    md = Template(open(f'{file_name}.md', 'rt').read())
    context = apply(load(open(f'{file_name}-{version}.yaml')))
    context['version'] = version

    # save .md
    with open(f'{file_name}-{version}.md', 'wt') as file:
    	file.write(md.render(context))

    # then .docx
    doc.render(context)
    doc.save(f'{file_name}-{version}.docx')
