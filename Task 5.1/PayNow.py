
from selenium.webdriver.common.by import By


class PayNow:

    def __init__(self, driver):
        driver.get("https://academy.testifyltd.com/courses/test-automation-simplified")
        self.pay_now_button = driver.find_element(By.XPATH, '//*[@id="enrol"]/div/div/div[2]/div/div[1]').find_element(By.XPATH, '//*[@id="enrol"]/div/div/div[2]/div/div[1]/div/a')
