import csv
from xml.etree import ElementTree as et
import requests
from bs4 import BeautifulSoup

class Book:
    def __init__(self, i) -> None:
        self.title = i.find('a', class_='product-card__name smartLink').text
        try:
            self.author = i.find('div', class_='author-list product-card__authors-holder').text
        except AttributeError:
            self.author = 'Автор не указан'


res = requests.get('https://book24.ru/')
csv_data = []
variant = int(input("1.Get all books' data\n2.Get current book's data "))

if res.status_code == 200:
    soup = BeautifulSoup(res.text, 'lxml')
    data = soup.find_all('div', class_='embla-slide-product shelf-products__item')
    tree = et.Element('Shop storage')
else:
    print(res.status_code)
    quit()

if variant == 1:
    for n,i in enumerate(data, start=1):
        # create book from Book class
        book = Book(i)
        # insert data to xml file's main tree
        product = et.SubElement(tree, f'Product_id: {n}')
        author = et.SubElement(product, f'Author: {book.author}')
        title = et.SubElement(product, f'Title {book.title}')
        # append ' ' to create xml file smarter
        et.indent(tree, ' ')
        et.ElementTree(tree).write('book24.xml',encoding="UTF-8", xml_declaration=True)
        
        fieldnames = ['Product_id', 'Author', 'Title']
        csv_data.append({
            fieldnames[0]: n,
            fieldnames[1]: book.author,
            fieldnames[2]: book.title
        })
    with open('book24.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(csv_data)
elif variant == 2:
    number = int(input("Write book's number(from 1 to 54) "))
    for n,i in enumerate(data, start=1):
        if n == number:
            # create book from Book class
            book = Book(i)
            # insert data to xml file's main tree
            product = et.SubElement(tree, f'Product_id: {n}')
            author = et.SubElement(product, f'Author: {book.author}')
            title = et.SubElement(product, f'Title {book.title}')
            # append ' ' to create xml file smarter
            et.indent(tree, ' ')
            et.ElementTree(tree).write('book24.xml',encoding="UTF-8", xml_declaration=True)
            
            fieldnames = ['Product_id', 'Author', 'Title']
            csv_data.append({
                fieldnames[0]: n,
                fieldnames[1]: book.author,
                fieldnames[2]: book.title
            })

            with open('book24.csv', 'w', encoding='UTF8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(csv_data)
else:
    print("Unkown command")