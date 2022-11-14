import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def highlight_element2(action, element, limit=50):
    action.move_to_element(element)
    action.move_by_offset(0, 10)
    action.click_and_hold(on_element=None)
    action.move_by_offset(0, limit)
    action.release(on_element=None)
    action.perform()


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    driver.maximize_window()
    action = ActionChains(driver)
    highlight_element2(action, driver.find_element(By.TAG_NAME, "h2"), 50)
    time.sleep(10)


if __name__ == '__main__':
    main()
