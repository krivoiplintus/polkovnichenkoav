from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("http://uitestingplayground.com/ajax")
driver.find_element(By.CSS_SELECTOR, '#ajaxButton').click()
print(driver.find_element(By.CSS_SELECTOR, 'p.bg-success').text)
driver.quit()
