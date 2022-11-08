from selenium.webdriver.common.by import By


class PartnerPage:

    def __init__(self, driver):
        driver.get("https://www.testifyltd.com/partner")
        self.partnership = driver.find_element(By.TAG_NAME,'h2')