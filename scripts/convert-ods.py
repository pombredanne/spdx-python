import tablib
import subprocess
import collections
import os.path
import sys
import json

ver = sys.argv[2]
fn = sys.argv[1]
ofn = os.path.basename(os.path.splitext(sys.argv[1])[0]) + '.csv'

subprocess.call(['soffice', '--headless', '--convert-to', "csv", sys.argv[1]])
data = tablib.Dataset()
with open(ofn, encoding='latin-1') as f:
    data.csv = f.read()

headers = data.headers[:]
want = {
    "Full name of License": "name",
    "License Identifier": "id",
    "Source/url": "sources",
    "Notes": "notes",
    "OSI Approved": "osi_approved",
    "Standard License Header": "header",
    "Template": "template"
}

for i, header in enumerate(headers):
    if header not in want:
        del data[header]
    else:
        data.headers[i] = want[header]

# Add hidden column for special cases
data.headers.append('hidden')

# Delete rubbish lines
del data[-3:]

data = data.dict

# Convert to booleans
for row in data:
    for k, v in row.items():
        if v == '':
            row[k] = None

    row['osi_approved'] = True if row['osi_approved'] == 'YES' else False
    if row['sources'] is not None:
        row['sources'] = row['sources'].strip().split('\n')

o = collections.OrderedDict()
o['version'] = ver
o['licenses'] = data

print(json.dumps(o, indent=2))
