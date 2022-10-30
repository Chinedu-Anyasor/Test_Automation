import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def print_element_fields(element):
    print("Text:", element.text)
    print("Size:", element.size)
    print("Location:", element.location)
    print("Tag_Name:", element.tag_name)
    print("Id:", element.id)
    print("Rectangle:", element.rect)
    print("Accessible_Name:", element.accessible_name)
    print("Location_Once_Scrolled_Into_View:", element.location_once_scrolled_into_view)
    print("Aria Role:", element.aria_role)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    driver.maximize_window()
    time.sleep(5)
    element = driver.find_element(By.TAG_NAME, "h2")
    print_element_fields(element)


if __name__ == '__main__':
    main()
