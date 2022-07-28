from bs4 import BeautifulSoup
import requests, codecs

class WebSite:
    def __init__(self,url) -> None:
        self.url = url
    def get_content(self):
        self.response = requests.get(self.url)
        self.bs = BeautifulSoup(self.response.text, 'lxml')
        data = self.bs.find_all('a')
        for n,i in enumerate(data, start=1):
            spans =  i.find_all('span')
            for j,k in enumerate(spans, start=1):
                if 'unittest' in k.text:
                    new_url = i.get('href')
                    req = requests.get(f'https://docs.python.org/3/library/{new_url}')
                    print(f'https://docs.python.org/3/library/{new_url}')
                    bs = BeautifulSoup(req.text, 'lxml', ).text.strip()
                    f = codecs.open('websites.txt', 'a', 'utf-8')
                    f.write(bs)
                    f.write('____________')
site = WebSite('https://docs.python.org/3/library/index.html')
site.get_content()
