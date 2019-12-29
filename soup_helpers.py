from bs4 import BeautifulSoup
import requests

def get_soup_for_url(url):
  print('Fetch', url)
  r = requests.get(url)
  soup = BeautifulSoup(r.text, 'html.parser')
  return soup