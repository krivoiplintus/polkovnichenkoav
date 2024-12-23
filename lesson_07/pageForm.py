from selenium.webdriver.common.by import By


class PageForm:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.maximize_window()

    def data_get_form(self, first_name, last_name, address, e_mail, phone, city, country, job_position, company, zip_code):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys(first_name)
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys(last_name)
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys(address)
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys(e_mail)
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys(phone)
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys(city)
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys(country)
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys(job_position)
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys(company)
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]').send_keys(zip_code)

    def click_submit(self):
        self._driver.find_element(By.CSS_SELECTOR, 'button').click()

    def find_zip_code_class(self):
        return self._driver.find_element(By.CSS_SELECTOR, '#zip-code').get_attribute("class")

    def find_all_element_class(self):
        return len(self._driver.find_elements(By.CSS_SELECTOR, 'div.alert.py-2.alert-success'))
