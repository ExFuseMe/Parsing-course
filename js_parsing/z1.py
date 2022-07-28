# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time
url = 'D:/chromedriver/chromedriver'
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# driver = webdriver.Chrome(executable_path='D:/chromedriver/chromedriver', options=chrome_options)
# driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
# time.sleep(3)
# print(driver.find_element_by_id('content').text)
# driver.close()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# driver = webdriver.Chrome(executable_path=url, options=chrome_options)
# driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
# try:
#     element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'loadedButton')))
# finally:
#     print(driver.find_element_by_id('content').text)
#     # print(driver.find_element(By.ID, 'content').text)
#     driver.close()


from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException
import time
def waitForLoad(driver):
    elem = driver.find_element_by_tag_name('html')
    count = 0
    while True:
        count += 1
        if count > 20:
            print('Ожидаем 10 сек')
            return time.sleep(.5)
        try:
            elem =  driver.find_element_by_tag_name('html')
        except StaleElementReferenceException:
            return
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=url, options=chrome_options)
driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
waitForLoad(driver)
driver.close()