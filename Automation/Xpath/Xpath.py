from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()

#Absolute/Full Xpath
#----------------
# driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[2]/div[2]/form/input").send_keys('Macbook')
# driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[2]/div[2]/form/button").click()

#Relative/Partial Xpath
driver.find_element(By.XPATH, "//*[@id='small-searchterms']").send_keys('Macbook')
driver.find_element(By.XPATH, "//*[@id='small-search-box-form']/button").click()

#Write xpath manually...
# driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[2]/div[2]/form/input").send_keys("Macbook")
# driver.find_element(By.XPATH, "//*[@class='button-1 search-box-button'/button]").click()

#and & or methods
#------------------
# driver.find_element(By.XPATH, "//*[@class='search-box-text ui-autocomplete-input' or @id='small-searchterms']").send_keys("Macbook")
# driver.find_element(By.XPATH, "//*[@class='button-1 search-box-button' and @type='submit']").click()

#contains() and start-with() methods
#------------------
# driver.find_element(By.XPATH, "//*[contains(@class, 'ui-autocomplete-input')]").send_keys("Macbook")
# driver.find_element(By.XPATH, "//*[starts-with(@class, 'button-1')]").click()


#text() methods...
#-----------
# driver.find_element(By.XPATH, "//*[contains(@class, 'ui-autocomplete-input')]").send_keys("Macbook")
# driver.find_element(By.XPATH, "//button[text()='Search']").click()


input("Press enter to continue...")