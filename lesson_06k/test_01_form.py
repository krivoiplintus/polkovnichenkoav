from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys("Иван")
driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys("Петров")
driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys("Ленина, 55-3")
driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys("test@skypro.com")
driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys("+7985899998787")
driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys("Москва")
driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys("Россия")
driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys("QA")
driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys("SkyPro")
driver.find_element(By.CSS_SELECTOR, 'button').click()
green = "rgba(15, 81, 50, 1)"
red = "rgba(132, 32, 41, 1)"
zip_code = driver.find_element(By.CSS_SELECTOR, '#zip-code').value_of_css_property("color")
assert zip_code == red

first_name = driver.find_element(By.CSS_SELECTOR, '#first-name').value_of_css_property("color")
assert first_name == green

last_name = driver.find_element(By.CSS_SELECTOR, '#last-name').value_of_css_property("color")
assert last_name == green

address = driver.find_element(By.CSS_SELECTOR, '#address').value_of_css_property("color")
assert address == green

e_mail = driver.find_element(By.CSS_SELECTOR, '#e-mail').value_of_css_property("color")
assert e_mail == green

phone = driver.find_element(By.CSS_SELECTOR, '#phone').value_of_css_property("color")
assert phone == green

city = driver.find_element(By.CSS_SELECTOR, '#city').value_of_css_property("color")
assert city == green

country = driver.find_element(By.CSS_SELECTOR, '#country').value_of_css_property("color")
assert country == green

job_position = driver.find_element(By.CSS_SELECTOR, '#job-position').value_of_css_property("color")
assert job_position == green

company = driver.find_element(By.CSS_SELECTOR, '#company').value_of_css_property("color")
assert company == green

driver.quit()
