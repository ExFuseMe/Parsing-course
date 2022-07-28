import requests

data = {'hamnews': '1', 'mail': 'example@examplemail.com', 'weekly': '0', 'dxnews': '0', 'classifieds': '0'}
r = requests.post('https://www.qrz.ru/subscribe/process', data = data)
print(r.text)