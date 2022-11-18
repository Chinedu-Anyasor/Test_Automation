import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

serv_obj = Service(ChromeDriverManager().install())
url = "https://web.facebook.com/"

driver = webdriver.Chrome(service=serv_obj)
driver.get(url)
driver.maximize_window()

# tag & ID
# driver.find_element(By.CSS_SELECTOR, "input#email").clear()
# driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("nedmond99@gmail.com)
# --------OR--------
# Tag(input) could be optional
# driver.find_element(By.CSS_SELECTOR, "#email").send_keys("nedmond99@gmail.com")

# tag & class combination
# driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("nedmond99@gmail.com")

# --------OR--------
# Tag(input) could be optional
# driver.find_element(By.CSS_SELECTOR, ".inputtext").send_keys("nedmond99@gmail.com")


# tag & attribute
# driver.find_element(By.CSS_SELECTOR, "input[id=email]").send_keys("nedmond99@gmail.com")

# --------OR--------
# Tag(input) could be optional
driver.find_element(By.CSS_SELECTOR, "[id=email]").send_keys("nedmond99@gmail.com")