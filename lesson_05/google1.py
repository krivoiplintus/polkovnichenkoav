from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
button = driver.find_element(By.CSS_SELECTOR, "button")
for x in range(1, 6):
    button.click()

print(len(driver.find_elements(By.CSS_SELECTOR, "button.added-manually")))
