from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://demo.nopcommerce.com')
driver.maximize_window()

###Loactors by linked text and Partial linked text
#driver.find_element(By.LINK_TEXT, 'Register') #locate linked element through Linked text
driver.find_element(By.PARTIAL_LINK_TEXT, 'Reg') #locate linked element through Partial Linked text


driver.find_element(By.CSS_SELECTOR, 'a.ico-register').click() #CSS selector -> tag & class
#driver.find_element(By.CSS_SELECTOR, '.ico-register').click() #CSS selector -> tag & class (tag is optional)




input("Press Enter to exit...")