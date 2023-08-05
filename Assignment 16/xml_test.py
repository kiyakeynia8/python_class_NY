import xml.etree.ElementTree as ET

tree = ET.parse('test.xml')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)

print(root[0][1].text)

parser = ET.XMLPullParser(['start', 'end'])
parser.feed('<mytag>sometext')

list(parser.read_events())
parser.feed(' more text</mytag>')

for event, elem in parser.read_events():
    print(event)
    print(elem.tag, 'text=', elem.text)

for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)

for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1
    rank.text = str(new_rank)
    rank.set('updated', 'yes')

tree.write('output.xml')

element = root.find('foo')

if element is None:
    print("element not found")