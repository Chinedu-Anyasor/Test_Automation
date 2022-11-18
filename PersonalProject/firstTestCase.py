# Test case
#------------
# 1. Open Web browser(Chrome,Firefox)
# 2. Open Url
# 3. Enter Username (Admin)
# 4. Enter Password (admin123)
# 5. Click on login
# 6. Capture title of the homepage(Actual title)
# 7. Verify title of the page OrangeHRM (Expected title)
# 8. Close Browser


from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# 1:
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# 2:
driver.get("https://opensourse-demo.orangehrmlive.com/")
# 3:
driver.find_element(By.NAME, "txtUsername").send_keys("Admin")
# 4:
driver.find_element(By.ID, "divPassword").send_keys("admin123")
# 5:
driver.find_element(By.ID, "btnLogin").click()
# 6:
actual_title = driver.title
expected_title = "OrangeHRM"
# 7:
if actual_title == expected_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")
# 8:
driver.close()