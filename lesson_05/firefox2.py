from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")
input = driver.find_element(By.CSS_SELECTOR, "input")
input.send_keys("1000")
sleep(5)
input.clear()
input.send_keys("999")
