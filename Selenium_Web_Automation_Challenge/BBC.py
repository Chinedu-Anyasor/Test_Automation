import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.bbc.com/")
    driver.maximize_window()
    headlines = driver.find_elements(By.XPATH, '//*[@id="page"]')
    for headline in headlines:
        top_10_news = headline.find_element(By.XPATH, '//*[@id="page"]/section[3]')
        print(top_10_news.text)

    topics = driver.find_elements(By.XPATH, '//*[@id="page"]/section[4]')
    for topic in topics:
        news = topic.find_element(By.XPATH, '//*[@id="page"]/section[4]/div/div/div[2]/div/section[1]')
        print(news.text)


if __name__ == '__main__':
    main()