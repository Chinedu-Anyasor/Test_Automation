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

# Import all the webdriver modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Specify the browser location
serv_obj = Service(ChromeDriverManager().install())
# Specify the Url

url = "https://opensourse-demo.orangehrmlive.com/auth/login/"

# 1: Create the Webdriver Object
driver = webdriver.Chrome(service=serv_obj)

# 2: Open Url
driver.get(url)

# 3: Enter Username
# clear the value in the field and enter username
driver.find_element(By.NAME, "txtUsername").clear()
driver.find_element(By.NAME, "txtUsername").send_keys("admin")

# 4: Enter Password
# clear the value in the field and enter password
driver.find_element(By.ID, "txtPassword").clear()
driver.find_element(By.ID, "txtPassword").send_keys("admin123")

# 5: Click on login
driver.find_element(By.ID, "btnLogin").click()

# 6: Capture the title of the homepage
actual_title = driver.title
expected_title = "OrangeHRM"

# 7: Verify the title of the page
if actual_title == expected_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

# 8: Close browser
driver.close()