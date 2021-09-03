from jinja2 import Template
from docxtpl import DocxTemplate
from yaml import load

file_name = 'Report'
version = '1.0'

def render_list(lst):
    return '\n\r\n\r'.join(['({}) {}'.format(chr(ord('a') + i), item) for i, item in enumerate(lst)])

def apply(item):
    if isinstance(item, list):
        return render_list(item)
    if isinstance(item, dict):
        return {key: apply(item[key]) for key in item}
    return item

doc = DocxTemplate(f'{file_name}.docx')
#md = Template(open('syllabus-template.md', 'rt').read())
context = apply(load(open(f'{file_name}-{version}.yaml')))
context['version'] = version

# save .md
#with open('{}.md'.format(file_name), 'wt') as file:
#	file.write(md.render(context))

# then .docx
doc.render(context)
doc.save(f'{file_name}-{version}.docx')
