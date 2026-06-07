from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://demo.nopcommerce.com')
driver.maximize_window()

###CSS Selector (4 Types)
#-----------------
# 1) Tag name & ID
# 2) Tag name & Class
# 3) Tag name & Attribute
# 4) Tag name, Class & Attribute
#-----------------
# 1)Tag name & ID
# driver.find_element(By.CSS_SELECTOR, 'input#small-searchterms').send_keys("iPhone") #Syntax-> tagname#ID
# #writing the tag name is optional, i.e., we can use like '#small-searchterms'
# driver.find_element(By.CSS_SELECTOR, 'button.button-1').click() #Syntax-> tagname.classname

# 2) Tag name & Class
# driver.find_element(By.CSS_SELECTOR, 'input.search-box-text').send_keys('MacBook') #Syntax-> tagname.class
# driver.find_element(By.CSS_SELECTOR, '.button-1').click() #Syntax-> tagname.classname (tagname optional)

# 3)Tag name & Attribute
# driver.find_element(By.CSS_SELECTOR, 'input[type=text]').send_keys('Macbook') #Syntax-> tagname[attribute=value]
# driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click() #Syntax-> tagname[attribute=value]

# 4) Tag name, Class & Attribute
driver.find_element(By.CSS_SELECTOR, 'input.search-box-text[type=text]').send_keys("macbook") #syntax -> tagname.class[attribute=value]
driver.find_element(By.CSS_SELECTOR, 'button.button-1').click() #Syntax-> tagname.classname


input("Press enter to continue...")
#driver.quit()