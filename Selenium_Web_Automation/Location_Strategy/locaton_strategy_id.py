from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def locate_by_id(driver):
    email_element = driver.find_element(By.ID, "email")
    print("Email element", email_element)
    password_element = driver.find_element(By.ID, "pass")
    print("Password element", password_element)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.facebook.com")
    locate_by_id(driver)


if __name__ == '__main__':
    main()
