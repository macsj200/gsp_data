import json
from soup_helpers import get_soup_for_url

def fetch_name_for_id(id):
  url = 'https://www.elitegsp.com/posts/?id={}'.format(id)
  soup = get_soup_for_url(url)
  title = soup.find(id='posts_title')
  if title:
    character_name = title.text.split("'")[0]
  return character_name

name_to_id = {}
id_to_name = {}

main_soup = get_soup_for_url('https://www.elitegsp.com/posts/')
for option in main_soup.find(id='posts_dropbox').find_all('option'):
  if option.text == 'All Posts':
    continue
  id = option['value'].split('=')[1]
  name = fetch_name_for_id(id)
  name_to_id[name] = id
  id_to_name[id] = name

with open('mappings/name_to_id.json', 'w') as f:
  f.write(json.dumps(name_to_id))

with open('mappings/id_to_name.json', 'w') as f:
  f.write(json.dumps(id_to_name))