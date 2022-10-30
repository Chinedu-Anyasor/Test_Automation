from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def locate_by_class_name(driver):
    rr_first_element = driver.find_element(By.CLASS_NAME, "react-reveal")
    print("React Reveal First element", rr_first_element)
    rr_elements = driver.find_elements(By.CLASS_NAME, "react-reveal")
    for rr_element in rr_elements:
        print("React Reveal first element", rr_element)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    locate_by_class_name(driver)


if __name__ == '__main__':
    main()
