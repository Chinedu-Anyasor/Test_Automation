import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    # driver.execute_script("alert('Hello world');")
    driver.execute_script("""
        const forms = document.getElementsByTagName('form');
        for (const form of forms) {
            form.style.backgroundColor = 'red';
        }
    """)
    driver.execute_script("""
            const links = document.getElementsByTagName('a');
            for (const link of links) {
                link.style.color = 'green';
            }
        """)
    time.sleep(10)


if __name__ == '__main__':
    main()
