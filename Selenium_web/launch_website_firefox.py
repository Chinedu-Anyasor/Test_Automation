
from selenium import webdriver


def main():
    driver = webdriver.Firefox(executable_path="/Users/zacky/Documents/Testing App/firefox driver/geckodriver")
    driver.get("https://fcbarcelona.com")
    driver.close()


main()
