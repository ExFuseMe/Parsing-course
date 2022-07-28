from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument("user-agent=Macintosh")
dir = 'D:/chromedriver/chromedriver'
driver = webdriver.Chrome(executable_path=dir, options=chrome_options)
driver.get('https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending')
agent = driver.execute_script("return navigator.userAgent")
print(agent)
driver.close()
