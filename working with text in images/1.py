from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
chrome_options = Options()
chrome_options.add_argument('--headless')
dir = 'D:/chromedriver/chromedriver'
driver = webdriver.Chrome(executable_path=dir, options=chrome_options)
driver.get('https://obrazovaka.ru/')
print(driver.get_cookies())
driver.close()