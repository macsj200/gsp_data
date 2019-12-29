from bs4 import BeautifulSoup
import requests
import json

i = 1
name_to_id = {}
id_to_name = {}
while True:
  url = 'https://www.elitegsp.com/posts/?id={}'.format(i)
  print('Fetch', url)
  r = requests.get(url)
  soup = BeautifulSoup(r.text, 'html.parser')
  title = soup.find(id='posts_title')
  if title:
    character_name = title.text.split("'")[0]
    name_to_id[character_name] = i
    id_to_name[i] = character_name
    i = i + 1
  else:
    break

with open('mappings/name_to_id.json', 'w') as f:
  f.write(json.dumps(name_to_id))

with open('mappings/id_to_name.json', 'w') as f:
  f.write(json.dumps(id_to_name))