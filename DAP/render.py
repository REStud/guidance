from jinja2 import Template
from docxtpl import DocxTemplate
from yaml import load

file_name = 'Report'
version = '1.0'

doc = DocxTemplate(f'{file_name}.docx')
#md = Template(open('syllabus-template.md', 'rt').read())
context = load(open(f'{file_name}-{version}.yaml'))

# save .md
#with open('{}.md'.format(file_name), 'wt') as file:
#	file.write(md.render(context))

# then .docx
doc.render(context)
doc.save(f'{file_name}-{version}.docx')
