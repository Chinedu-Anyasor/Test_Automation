from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

serv_obj = Service(ChromeDriverManager().install())
url = "https://demo.nopcommerce.com/"

driver = webdriver.Chrome(service=serv_obj)
driver.get(url)
driver.maximize_window()
driver.find_element(By.ID, "small-searchterms").send_keys("Electronics")
driver.find_element(By.XPATH, '//*[@id="small-search-box-form"]/button').click()
actual_url = driver.current_url
expected_url = "https://demo.nopcommerce.com/search?q=Electronics"
if actual_url == expected_url:
    print("Test Passed")
else:
    print("Test Failed")

driver.find_element(By.NAME, "q").send_keys("Apple MacBook Pro 13-inch")
driver.find_element(By.XPATH, '//*[@id="small-search-box-form"]/button').click()
actual_url = driver.current_url
expected_url = "https://demo.nopcommerce.com/search?q=Apple+MacBook+Pro+13-inch"
if actual_url == expected_url:
    print("Test 2 Passed")
else:
    print("Test 2 Failed")

driver.close()
