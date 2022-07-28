import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org/'
response = requests.get(url)
soup = BeautifulSoup(response.text)
htmls = soup.find_all('html')
for i in range(len(htmls)):
    print(htmls[i].text)