import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.wikipedia.org/')
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'lxml')
    p = soup.find_all('p')
    for el in p:
        print(el.text.strip())