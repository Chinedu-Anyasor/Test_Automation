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
    driver.get("https://weather.com/")
    driver.maximize_window()
    reports = driver.find_elements(By.XPATH, '//*[@id="WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034'
                                             '"]/div/section/div/div[2]/div[1]/div[1]/span')
    for report in reports:
        current_temperature = report.find_element(By.XPATH, '//*[@id="WxuCurrentConditions-main-b3094163-ef75-4558'
                                                            '-8d9a-e35e6b9b1034"]/div/section/div/div[2]/div[1]/div['
                                                            '1]/span')
        print(current_temperature.text)

    temperatures = driver. find_elements(By.XPATH, '//*[@id="WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76'
                                                   '-7aea8e98520a"]/section')
    for temperature in temperatures:
        all_temperature = temperature.find_element(By.XPATH, '//*[@id="WxuTodayWeatherCard-main-486ce56c-74e0-4152'
                                                             '-bd76-7aea8e98520a"]/section/div/ul')
        print(all_temperature.text)


if __name__ == '__main__':
    main()