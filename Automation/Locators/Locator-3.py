from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#driver.get('http://automationpractice.com/index.php')
driver.get('https://demo.nopcommerce.com')
driver.maximize_window()

### Locators by class name and tag name
slider = driver.find_elements(By.CLASS_NAME, 'slider-img')
print(len(slider))

tags = driver.find_elements(By.TAG_NAME, 'a')
print(len(tags))

input("Press enter to continue...")