from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

source = urlopen('https://en.wikipedia.org/wiki/Escape_from_Tarkov').read()
soup = BeautifulSoup(source,'lxml')
paras = []
for paragraph in soup.find_all('p'):
    paras.append(str(paragraph.text))
heads = []
for head in soup.find_all('span', attrs={'mw-headline'}):
    heads.append(str(head.text))
text = [val for pair in zip(paras, heads) for val in pair]
text = ' '.join(text)
text = re.sub(r"\[.*?\]+", '', text)
text = text.replace('\n', '')[1:-15]
with open('text.txt', 'w') as f:
    f.write(text)