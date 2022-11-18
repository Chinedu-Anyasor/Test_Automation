import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

serv_obj = Service(ChromeDriverManager().install())
url = "https://demo.nopcommerce.com/"

driver = webdriver.Chrome(service=serv_obj)
driver.get(url)
driver.maximize_window()
# To print out total number of sliders
sliders = driver.find_elements(By.CLASS_NAME, "nivo-imageLink")
print(len(sliders))

# To print out total number of links in the url page
links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))

time.sleep(5)