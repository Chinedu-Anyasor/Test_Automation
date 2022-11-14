from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def locate_by_tag_name(driver):
    first_input = driver.find_element(By.TAG_NAME, "input")
    print("Firstname element:", first_input)
    div_elements = driver.find_elements(By.TAG_NAME, "div")
    print("Total divs:", len(div_elements))
    for div_element in div_elements:
        print("Div Element:", div_element)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    locate_by_tag_name(driver)


if __name__ == '__main__':
    main()
