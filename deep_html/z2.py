import requests
from bs4 import BeautifulSoup

url = 'https://www.pythonscraping.com/pages/page1.html'
response = requests.get(url)
if response.status_code==200:
    soup = BeautifulSoup(response.text, 'lxml')
    divs = soup.find('div').text
    with open(file='text.txt', mode='w') as file:
        file.write(divs)