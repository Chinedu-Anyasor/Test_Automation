import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# Challenge 5
# Using any browser, navigate to any Youtube video of your choice, allow your script to wait for the comments to load
# then get the first two comments, and print them in the terminal.
def scroll_by_offset(action, delta_y):
    action.scroll_by_amount(0, delta_y).perform()


def youtube_test(driver):
    driver.get("https://www.youtube.com/watch?v=sXE5298aDPw")
    action = ActionChains(driver)
    driver.maximize_window()
    # time.sleep(60)
    scroll_by_offset(action, 450)
    web_driver_wait = WebDriverWait(driver, 60)
    web_driver_wait.until(EC.visibility_of_element_located((By.ID, "sections")))
    comments = driver.find_elements(By.ID, 'sections')
    for comment1 in comments:
        comment1_content = comment1.find_element(By.XPATH, '//*[@id="contents"]/ytd-comment-thread-renderer[1]')
        print(comment1_content.text)

    for comment2 in comments:
        comment2_content = comment2.find_element((By.XPATH, '//*[@id="contents"]/ytd-comment-thread-renderer[2]'))
        print(comment2_content.text)


def main():
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    gecko_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    youtube_test(chrome_driver)
    sweet_test(gecko_driver)
    time.sleep(15)


if __name__ == '__main__':
    main()