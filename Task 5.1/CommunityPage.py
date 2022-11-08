
from selenium.webdriver.common.by import By


class CommunityPage:

    def __init__(self, driver):
        driver.get("https://www.testifyltd.com/community")
        self.join_our_slack_button = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div/div[1]/div[1]').find_element(By.TAG_NAME, 'button')
