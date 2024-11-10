from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
wait = WebDriverWait(driver, 20)
wait.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'p.lead'), "Done!")
)
img = driver.find_element(By.CSS_SELECTOR, '#award')
print(img.get_attribute("src"))
driver.quit()
