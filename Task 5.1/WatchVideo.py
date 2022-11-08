
from selenium.webdriver.common.by import By


class WatchVideo:

    def __init__(self, driver):
        driver.get("https://academy.testifyltd.com/courses/test-automation-simplified")
        self.watch_video_button = driver.find_element(By.XPATH, '//*[@id="faq"]/div/div').find_element(By.XPATH, '//*[@id="faq"]/div/div/div[5]/button')
