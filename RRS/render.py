from csv import DictReader
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

def render_rules(rules, items, topics):
    items_covered = []
    topics_covered = []
    output = ''
    for rule in rules:
        item = rule['item']
        topic = items[tuple([item])]['topic'] 
        if item not in items_covered:
            if topic not in topics_covered:
                output += f'**{topics[tuple([topic])]["title"]}** | | |\n'
                topics_covered.append(topic)
            output += f'{items[tuple([item])]["title"]} | {item} |'
            items_covered.append(item)
        else:
            output += '| | |'
        output += f' {subitem_or_empty(rule["subitem"])}{rule["rule"]}| |\n'
    return output
    
def main(journal=''):
    items = read_into_dictionary('item.csv', 'item')
    topics = read_into_dictionary('topic.csv', 'topic')
    with open('rule.csv', 'rt') as f:
        rules = list(DictReader(f))
    print('''---
papersize: a4
geometry:
- top=20mm
- left=20mm
- right=20mm
- bottom=20mm
- heightrounded
---
# Reproducible Research Standard v1.0
## What to include in the replication package and in the README document

| | Item No | Rule | Policy |
|---|-|-------|-|''')
    print(render_rules(rules, items, topics))
    print('''
All participating journals value all rules, but the levels of enforcement may vary. For each rule, journal policy may be **Verified**, **Required** or **Recommended**.
''')

main()