
from selenium.webdriver.common.by import By


class TestAutomation:

    def __init__(self, driver):
        driver.get("https://academy.testifyltd.com/courses/test-automation-simplified")
        self.title = driver.find_element(By.TAG_NAME, 'h1')
