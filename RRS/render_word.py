from csv import DictReader
from docxtpl import DocxTemplate, Listing

version = '1.0'

def subitem_or_empty(subitem):
    if subitem:
        return f'({subitem}) '
    else:
        return ''

def read_into_dictionary(fname, key):
    output = {}
    with open(fname, 'rt') as f:
        for row in DictReader(f):
            index = tuple(row[k] for k in key.split('/'))
            output[index] = row
    return output

def render_rules(rules):
    output = {}
    for key in rules:
        item, subitem = key
        rule = rules[key]["rule"]
        if int(item) not in output:
            output[int(item)] = []
        output[int(item)].append(f'{subitem_or_empty(subitem)}{rule}')
    return {item: Listing('\n'.join(output[item])) for item in output}

def main(journal=''):
    rules = render_rules(read_into_dictionary('rule.csv', 'item/subitem'))
    doc = DocxTemplate('Reproducible-template.docx')
    doc.render(dict(rule=rules))
    doc.save(f'Reproducible-Research-Standard-{version}.docx')

main()
