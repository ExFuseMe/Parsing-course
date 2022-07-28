from django.urls import clear_script_prefix
import requests
from bs4 import BeautifulSoup
response = requests.get('https://www.citilink.ru/catalog/videokarty/')
if response.status_code == 200:
    sp = BeautifulSoup(response.text, 'lxml')
    data = sp.find_all("div", class_='product_data__gtm-js product_data__pageevents-js ProductCardHorizontal js--ProductCardInListing js--ProductCardInWishlist')
    cards = []
    for n,i in enumerate(data):
        title = i.find('a', {'class':'ProductCardHorizontal__title Link js--Link Link_type_default'}).text.strip().split(',')[0]
        price = i.find('span', class_='ProductCardHorizontal__price_current-price js--ProductCardHorizontal__price_current-price').text.strip()
        cards.append({title:price+'₽'})
    print(cards)