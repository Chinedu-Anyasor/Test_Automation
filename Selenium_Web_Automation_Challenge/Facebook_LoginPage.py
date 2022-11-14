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
    driver.get("https://www.facebook.com")
    driver.maximize_window()
    send_keys_to_element(driver.find_element(By.ID, "email"), "nedmond@gmail.com")
    send_keys_to_element(driver.find_element(By.ID, "pass"), "08033698427")
    form = driver.find_element(By.TAG_NAME, "form")
    form.find_element(By.TAG_NAME, "button").click()
    time.sleep(5)


if __name__ == '__main__':
    main()
