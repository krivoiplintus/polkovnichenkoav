from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
driver.find_element(By.CSS_SELECTOR, '#delay').clear()
driver.find_element(By.CSS_SELECTOR, '#delay').send_keys("45")
spans = driver.find_elements(By.CSS_SELECTOR, 'span')
spans[2].click()
spans[5].click()
spans[3].click()
spans[16].click()
waiter = WebDriverWait(driver, 50)
waiter.until(
    EC.invisibility_of_element((By.CSS_SELECTOR, '#spinner'))
)
res = driver.find_element(By.CSS_SELECTOR, 'div.screen').text
result = "15"
assert res == result

driver.quit()
