import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def highlight_element(action, element, limit=50):
    action.drag_and_drop_by_offset(element, 0, limit)
    action.perform()


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    driver.maximize_window()
    action = ActionChains(driver)
    highlight_element(action, driver.find_element(By.TAG_NAME, "h2"), 50)
    time.sleep(10)


if __name__ == '__main__':
    main()
