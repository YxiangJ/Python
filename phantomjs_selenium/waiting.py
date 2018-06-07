# 显式等待
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Ie()
driver.get("http://somedomain/url_that_delays_loading")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement")))
finally:
    driver.quit()


'''
#隐式等待


from selenium import webdriver

driver = webdriver.Ie()
driver.implicitly_wait(10)
driver.get("http://somedomain/url_that_delays_loading") 
myDynamicElement = driver.find_element_by_id("myDynamicElement")
'''