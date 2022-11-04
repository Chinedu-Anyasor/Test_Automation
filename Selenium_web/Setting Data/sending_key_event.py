import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def send_keys_to_element(element, *keys):
    element.send_keys(keys)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    driver.maximize_window()
    time.sleep(5)
    send_keys_to_element(driver.find_element(By.NAME, "firstname"), "Chinedu")
    send_keys_to_element(driver.find_element(By.NAME, "lastname"), "Anyasor")
    send_keys_to_element(driver.find_element(By.NAME, "email"), "nedmond@gmail.com")
    send_keys_to_element(driver.find_element(By.NAME, "phone"), "08033698427")
    send_keys_to_element(driver.find_element(By.NAME, "message"), "Testcodecamp school for stst and tas")
    time.sleep(10)


if __name__ == '__main__':
    main()
