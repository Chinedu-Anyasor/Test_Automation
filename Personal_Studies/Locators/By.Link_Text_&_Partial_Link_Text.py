from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

serv_obj = Service(ChromeDriverManager().install())
url = "https://demo.nopcommerce.com/"

driver = webdriver.Chrome(service=serv_obj)
driver.get(url)
driver.maximize_window()
#driver.find_element(By.LINK_TEXT, "Register").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Regi").click()

driver.close()