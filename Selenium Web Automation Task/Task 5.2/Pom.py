import time
from HiringPage import HiringPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://academy.testifyltd.com/courses/test-automation-simplified")
    driver.maximize_window()
    hiring = HiringPage(driver)
    print(hiring.hiring)
    time.sleep(20)


if __name__ == '__main__':
    main()