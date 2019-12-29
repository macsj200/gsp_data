from bs4 import BeautifulSoup
import requests

r = requests.get('https://www.elitegsp.com/posts/')
soup = BeautifulSoup(r.text, 'html.parser')
for row in soup.find_all(class_='gsp_posts_row'):
  gsp = int(row.find(class_='gsp_posts_row_gsp').text.replace(',', '').replace(' GSP', ''))
  time_str = row.find(class_='gsp_posts_row_time').text
  print(gsp, time_str)