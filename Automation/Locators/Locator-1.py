from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#driver.get("https://automationpractice.com")
driver.get('https://demo.nopcommerce.com')
driver.maximize_window()

###Loactors by ID and NAME
#driver.find_element(By.ID, 'small-searchterms').send_keys('Apple MacBook Pro') #By.ID
driver.find_element(By.NAME, 'q').send_keys('Apple MacBook Pro')          #By.NAME
(driver.find_element(By.CSS_SELECTOR, "button.button-1").click()) # CSS selector e tag & class name use korechi -> "tagname.valueofclassname"
#(driver.find_element(By.CSS_SELECTOR, ".button-1").click()) # CSS selector e tag & class name use korechi -> ".valueofclassname" (tagname is optional)





input("Press Enter to exit...")