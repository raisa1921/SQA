# #Test case
# --------------
# 1) Open Web Browser (Chrome, firefox, Edge)
# 2) Open URL
# 3) Enter username (Ex: Admin)
# 4) Enter password (Ex: admin123)
# 5) Click on Login
# 6) Capture title of the home page (Actual title)
# 7) Verify title of the page: OrangeHRM (Expected)
# 8) Close browser



######1
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome() #Edge() #Chrome() #Firefox
# driver.get('https://opensource-demo.orangehrmlive.com/')
#
# # driver.implicitly_wait(10) #Implicit wait is a global wait that tells Selenium: “Whenever you try to find an element, wait up to X seconds if it’s not immediately available in the DOM (Document Object Model).”
# # driver.find_element(By.NAME, "username").send_keys("Admin")
#
# wait = WebDriverWait(driver, 10)
#
# username_field = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
# username_field.send_keys("Admin")
# driver.find_element(By.NAME, "password").send_keys("admin123")
# driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click() # Correct locator for login button
#
# actual_title = driver.title #for capturing the title of the webpage
# expected_title = "OrangeHRM"
#
# if actual_title == expected_title:
#     print("Login test passed")
# else:
#     print("Login test failed")
# driver.quit()
#
# driver.quit()


######2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome() #Edge() #Chrome() #Firefox
driver.get('https://admin-demo.nopcommerce.com/login')

driver.find_element(By.NAME, 'Email').clear() #to clear the existing placeholder
driver.find_element(By.NAME, 'Email').send_keys('admin@yourstore.com')

driver.find_element(By.ID, "Password").clear()
driver.find_element(By.ID, "Password").send_keys("admin")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click() # Correct locator for login button

actual_title = driver.title #for capturing the title of the webpage
expected_title = "Dashboard / nopCommerce administration"

if actual_title == expected_title:
    print("Login test passed")
else:
    print("Login test failed")
driver.quit()

driver.quit()