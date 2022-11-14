import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager




def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://academy.testifyltd.com")
    driver.maximize_window()
    time.sleep(10)
    buttons = driver.find_elements(By.NAME, "EXPLORE COURSES")
    print("Button size:", len(buttons), "button")
    for button in buttons:
        print("Button:", button)


if __name__ == '__main__':
    main()
