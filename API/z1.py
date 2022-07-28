import requests, json

url = "http://ip-api.com/json/"
ip = "105.162.40.51"

req = requests.get(url+ip).json()
country = req['country']
zip_code = req['zip']
timezone = req['timezone']
region = req['region']
print(f'Country: {country};\nZip code: {zip_code};\ntimezone: {timezone};\nregion: {region}')