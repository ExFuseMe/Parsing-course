import requests, csv
from bs4 import BeautifulSoup

url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
response = requests.get(url)
if response.status_code==200:
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find_all('div', class_= 'card', limit=9)
    file = open('text.csv', 'w')
    writer = csv.writer(file)
    try:
        csvRow = []
        for n,i in enumerate(data, start=2):
                name = i.find('h4').text.strip()
                price = i.find('h5').text.strip()
                csvRow.append({name: price})
        writer.writerow(csvRow)

    finally:
        pass
