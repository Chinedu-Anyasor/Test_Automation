import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def scroll_to_element(action, element):
    action.move_to_element(element).perform()


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    driver.maximize_window()
    action = ActionChains(driver)
    scroll_to_element(action, driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[3]'))
    time.sleep(10)


if __name__ == '__main__':
    main()
