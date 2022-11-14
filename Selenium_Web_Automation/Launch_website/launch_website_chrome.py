
from selenium import webdriver


def main():
    driver = webdriver.Chrome(executable_path="/Users/zacky/Documents/Testing App/Chrome driver/chromedriver 2")
    driver.get("https://fcbarcelona.com")
    driver.close()


main()
