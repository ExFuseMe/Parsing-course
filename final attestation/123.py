from xml.etree import ElementTree as et
import requests
from bs4 import BeautifulSoup

res = requests.get('https://book24.ru/')
if res.status_code == 200:
    soup = BeautifulSoup(res.text, 'lxml')
    print(soup.text)