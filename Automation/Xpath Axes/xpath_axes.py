from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

#self
# text = driver.find_element(By.XPATH, "//a[contains(text(), 'Neuland Laborat')]/self::a").text
# print(text) #Neuland Laborat

#Parent
# parent = driver.find_element(By.XPATH, "//a[contains(text(), 'Neuland Laborat')]/parent::td").text
# print(parent) #Neuland Laborat

#Child
# child = driver.find_elements(By.XPATH, "//a[contains(text(), 'Neuland Laborat')]/ancestor::tr/child::td")
# print(len(child)) #6

#Ancestor
# ancestor = driver.find_element(By.XPATH, "//a[contains(text(), 'Neuland Laborat')]/ancestor::tr").text
# print(ancestor) #Neuland Laborat A 15,374.40 16,190.00 + 5.30 Buy  |  Sell

#Descendant
# descendant = driver.find_elements(By.XPATH, "//a[contains(text(), 'Neuland Laborat')]/ancestor::tr/descendant::*")
# print(len(descendant)) #10

#following
# following = driver.find_elements(By.XPATH, "//a[contains(text(), 'Neuland Laborat')]/ancestor::tr/following::*")
# print(len(following)) #3074

#following-sibling
# followingsibling = driver.find_elements(By.XPATH, "//a[contains(text(), 'Neuland Laborat')]/ancestor::tr/following-sibling::*")
# print(len(followingsibling)) #261

#preceding
# preceding = driver.find_elements(By.XPATH, "//a[contains(text(), 'Neuland Laborat')]/ancestor::tr/preceding::*")
# print(len(preceding)) #269

#preceding-sibling
precedingsibling = driver.find_elements(By.XPATH, "//a[contains(text(), 'Neuland Laborat')]/ancestor::tr/preceding-sibling::*")
print(len(precedingsibling)) #7

input("Press enter to continue...")
