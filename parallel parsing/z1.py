import re, random, _thread
from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_links(thread_name, bs):
    print(f'Подготовка ссылки в потоке {thread_name}')
    return bs.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))
def scrape_article(thread_name, path):
    html = urlopen(f'http://en.wikipedia.org{path}')
    bs = BeautifulSoup(html, 'lxml')
    title = bs.find('h1').get_text()
    print(f'Парсинг {title} в потоке {thread_name}')
    links = get_links(thread_name, bs)
    if len(links) > 0:
        newArticle = links[random.randint(0, len(links) -1)].attrs['href']
        print(newArticle)
        scrape_article(thread_name, newArticle)
try:
    _thread.start_new_thread(scrape_article, ('Thread 1', '/wiki/Tesla_Model_X',))
    _thread.start_new_thread(scrape_article, ('Thread 2', '/wiki/Tesla_Model_S',))
except:print('Ошибка потока')
while 1:
    pass