
from selenium.webdriver.common.by import By


class HiringPage:

    def __init__(self, driver):
        driver.get("https://academy.testifyltd.com/courses/switch-to-software-testing")
        self.hiring = driver.find_element(By.XPATH, '//*[@id="__next"]/section/div/div[1]/div[2]/div/div[1]/ul/li[2]/a').click()
