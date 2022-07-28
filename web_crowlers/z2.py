import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.wikipedia.org/')
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find('p').getText()
    print(data)
    with open(file='text.txt', mode='w') as file:
        file.write(data)
    