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
            if '/' in key:
                index = tuple(row[k] for k in key.split('/'))
            else:
                index = row[key]
            output[index] = row
    return output

def render_rules(rules):
    output = dict(rules={}, alternatives={})
    for key in rules:
        item, subitem = key
        short_key = f'{item}{subitem}'
        output['rules'][short_key] = rules[key]['rule']
        output['alternatives'][short_key] = rules[key]['alternatives']
    return output

def main(journal=''):
    items = read_into_dictionary('item.csv', 'item')
    topics = read_into_dictionary('topic.csv', 'topic')
    rules = render_rules(read_into_dictionary('rule.csv', 'item/subitem'))
    doc = DocxTemplate('Reproducible-template.docx')
    doc.render(dict(rule=rules['rules'], 
        alt=rules['alternatives'],
        item={key: items[key]['title'] for key in items}, 
        topic={key: topics[key]['title'] for key in topics}))
    doc.save(f'Reproducible-Research-Standard-{version}.docx')

main()
