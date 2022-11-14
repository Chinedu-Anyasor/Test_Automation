from datetime import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC


def send_keys_to_element(element, *keys):
    element.send_keys(keys)


def main():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("https://google.com")
    driver.maximize_window()
    send_keys_to_element(driver.find_element(By.TAG_NAME, "input"), "python")
    form = driver.find_element(By.TAG_NAME, "form")
    form.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]').click()
    web_driver_wait = WebDriverWait(driver, 20)
    web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[7]/div/div[11]/div['
                                                                      '2]/div/div/div[2]')))
    briefs = driver.find_elements(By.XPATH, '/html/body/div[7]/div/div[11]/div[2]/div/div/div[2]/div/div['
                                            '5]/div/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div')
    for brief in briefs:
        wiki_brief = brief.find_element(By.XPATH, '/html/body/div[7]/div/div[11]/div[2]/div/div/div[2]/div/div['
                                                  '5]/div/div/div/div/div[1]/div/div/div/div/div/div/div['
                                                  '1]/div/div/div/span[1]')
        print(wiki_brief.text)


if __name__ == '__main__':
    main()
