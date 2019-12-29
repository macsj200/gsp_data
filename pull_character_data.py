from bs4 import BeautifulSoup
import requests
import json
from soup_helpers import get_soup_for_url

with open('mappings/id_to_name.json', 'r') as f:
  id_to_name = json.loads(f.read()) 
  for id, name in id_to_name.items():
    data_rows = []
    url = 'https://www.elitegsp.com/posts/?id={}'.format(id)
    soup = get_soup_for_url(url)
    for row in soup.find_all(class_='gsp_posts_row'):
      gsp = row.find(class_='gsp_posts_row_gsp').text.replace(',', '').replace(' GSP', '')
      time_str = row.find(class_='gsp_posts_row_time').text
      id = row.find(class_='gsp_posts_row_flair_img')['src'].split('/')[-1].replace('-min.png', '')
      data_rows.append([gsp, id, time_str])

    with open('data/{}.csv'.format(id), 'w') as f:
      for data_row in data_rows:
        f.write(','.join(data_row) + '\n')