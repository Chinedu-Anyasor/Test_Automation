import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://academy.testifyltd.com/courses/test-automation-simplified")
    driver.maximize_window()
    partner = PartnerPage(driver)
    test_automation = TestAutomation(driver)
    community_page = CommunityPage(driver)
    pay_in_naira = PayNow(driver)
    watch_video = WatchVideo(driver)
    print(partner.partnership)
    print(test_automation.title)
    print(community_page.join_our_slack_button)
    print(pay_in_naira.pay_now_button)
    print(watch_video.watch_video_button)
    time.sleep(20)


if __name__ == '__main__':
    main()