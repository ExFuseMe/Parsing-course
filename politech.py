from bs4 import BeautifulSoup
import requests

url = 'https://new.mospolytech.ru/postupayushchim/priem-v-universitet/rating-abiturientov/?qs=MDAwMDAwMDMxXzAxfDA5LjAzLjAxX8Ll4S3y5fXt7uvu4%2BjofM737eD%2FfMH%2B5Obl8u3g%2FyDu8e3u4uA%3D'
resp = requests.get(url, verify=False)
if resp.status_code == 200:
    soup = BeautifulSoup(resp.text, 'lxml')
    print(soup.find('table', class_='check'))