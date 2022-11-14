import time
from ContactPage import ContactPage
from AboutUsPage import AboutUsPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/")
    contact_page = ContactPage(driver)
    aboutus_page = AboutUsPage(driver)
    print(contact_page.firstname_input, contact_page.lastname_input)
    print(aboutus_page.title)
    time.sleep(20)


if __name__ == '__main__':
    main()