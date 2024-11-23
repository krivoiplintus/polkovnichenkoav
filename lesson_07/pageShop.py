from selenium.webdriver.common.by import By


class PageShop:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.maximize_window()

    def authorization(self, user_name, password):
        self._driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys(user_name)
        self._driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
        self._driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    def add_to_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

    def get_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container').click()

    def push_checkout(self):
        self._driver.find_element(By.CSS_SELECTOR, '#checkout').click()

    def fill_out_the_form(self, first_name, last_name, postal_code):
        self._driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(first_name)
        self._driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(last_name)
        self._driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(postal_code)

    def push_continue(self):
        self._driver.find_element(By.CSS_SELECTOR, '#continue').click()

    def read_total(self):
        return self._driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text
