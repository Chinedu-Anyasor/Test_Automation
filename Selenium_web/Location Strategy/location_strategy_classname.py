from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def locate_by_name(driver):
    firstname_element = driver.find_element(By.NAME, "firstname")
    print("Firstname element", firstname_element)
    lastname_element = driver.find_element(By.NAME, "lastname")
    print("Lastname element", lastname_element)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    locate_by_name(driver)


if __name__ == '__main__':
    main()
