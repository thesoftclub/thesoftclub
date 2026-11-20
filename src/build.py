"""Builds index.html from src/template.html. Run: python3 src/build.py"""
import re, os
here = os.path.dirname(os.path.abspath(__file__))
B = 'https://d2ol7oe51mr4n9.cloudfront.net/user_3HxvueFH5LSEJSkO70SiWH9SURm/'
IMG = {
 'hero':'703a8bfc-f0ec-434e-b319-f5260e687261','social':'9bbec3aa-69cd-4044-80f1-b571f05770e5',
 'golf':'c3f1e00d-d672-4ec1-a399-8d7979fc5765','padel':'ee1917ca-5123-4c08-9e1d-46ea76273859',
 'matcha':'1ac09717-535d-4327-b089-ec72f58e6cb9','pottery':'a22b8012-e4f8-4645-bfbb-bc2e05c4a147',
 'picnic':'bb635668-3026-4b86-b4e8-d899e6b1ebeb','dinnerhill':'066bfb4d-d70e-4c3d-8dd4-90e353467508',
 'people1':'7af16128-54ab-4933-bfc5-d8cca7c65a6e','people2':'63c5e01e-d024-450f-85eb-921a3a4b818e',
 'people3':'fce59173-9b35-4234-961f-546ba5faaf6a','drinks':'d1e5f0f0-4714-485f-9095-96daae3d2e05',
}
s = open(os.path.join(here,'template.html')).read()
s = re.sub(r'\{\{(\w+)\}\}', lambda m: B + IMG[m.group(1)] + '.jpg', s)
s = s.replace('<!--JS-->', open(os.path.join(here,'shared.js')).read())
parts = s.split('<img ')
s = parts[0] + '<img ' + parts[1] + ''.join('<img loading="lazy" ' + p for p in parts[2:])
assert '{{' not in s
open(os.path.join(here,'..','index.html'),'w').write(s)
print('index.html written,', len(s), 'bytes')
