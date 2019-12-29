from bs4 import BeautifulSoup
import requests

r = requests.get('https://www.elitegsp.com/posts/')
soup = BeautifulSoup(r.text, 'html.parser')
data_rows = []
for row in soup.find_all(class_='gsp_posts_row'):
  gsp = row.find(class_='gsp_posts_row_gsp').text.replace(',', '').replace(' GSP', '')
  time_str = row.find(class_='gsp_posts_row_time').text
  id = row.find(class_='gsp_posts_row_flair_img')['src'].split('/')[-1].replace('-min.png', '')
  data_rows.append([gsp, id, time_str])

with open('data/main.csv', 'w') as f:
  for data_row in data_rows:
    f.write(','.join(data_row) + '\n')