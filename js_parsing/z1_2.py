from selenium import webdriver
from selenium.webdriver.chrome.options import Options

dir = 'D:/chromedriver/chromedriver'


chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=dir,options=chrome_options)
driver.get('https://yandex.ru/search/?text=python&lr=11127')

url = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[1]/div[1]/ul/li[1]/div/div[1]/a').get_attribute("href")
driver.get(url)
data = driver.find_element_by_xpath('/html').text
print('data=',data)
driver.close()