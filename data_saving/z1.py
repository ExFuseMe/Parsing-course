import requests
from bs4 import BeautifulSoup

res = requests.get('http://python.org')
if res.status_code == 200:
    soup = BeautifulSoup(res.text, 'lxml')
    urls = soup.find('img', class_='python-logo')['src']
    s= 'https://www.python.org/'+urls
    req = requests.get(s)
    file = open('file.jpg', 'wb')
    file.write(req.content)
    file.close()

