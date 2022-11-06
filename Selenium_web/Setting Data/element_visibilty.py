import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def scroll_by_offset(action, delta_y):
    action.scroll_by_amount(0, delta_y).perform()


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    form = driver.find_element(By.TAG_NAME, 'form')
    print("Form State:", form.is_displayed(), form.is_enabled())
    submit_button = form.find_element(By.TAG_NAME, 'button')
    driver.maximize_window()
    action = ActionChains(driver)
    scroll_by_offset(action, 250)
    time.sleep(2)
    scroll_by_offset(action, 250)
    time.sleep(2)
    scroll_by_offset(action, 150)
    print("Submit Button State:", submit_button.is_displayed(), submit_button.is_enabled())
    if submit_button.is_displayed():
        print("submit button is displayed")
        submit_button.click()


if __name__ == '__main__':
    main()