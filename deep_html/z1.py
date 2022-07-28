import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.pythonscraping.com/pages/warandpeace.html')
if response.status_code==200:
    soup = BeautifulSoup(response.text, 'lxml')
    col = soup.find_all('div')
    for n, i in enumerate(col, start=1):
        print(i.find('span', class_='red').text.strip())