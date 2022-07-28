import requests
from bs4 import BeautifulSoup

class Website:
        def __init__(self, url, title, body) -> None:
            self.url = url
            self.title = title
            self.body = body

def ParseHabr(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    titles = soup.find_all('h1')
    lines = soup.find_all('div', {'class':'article-formatted-body article-formatted-body_version-2'})
    content = '\n'.join([line.text for line in lines])
    title = '\n'.join([line.text for line in titles])

    
    
    return Website(url, title, content)

url = 'https://habr.com/ru/post/656447/'
data = ParseHabr(url)
print('Title: \n', data.title, '\n', 'Content: \n', data.body, '\n')