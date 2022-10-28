
from selenium import webdriver
import chromedriver_autoinstaller


def main():
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    driver.close()


main()
