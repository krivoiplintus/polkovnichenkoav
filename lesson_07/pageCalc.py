from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageCalc:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.maximize_window()

    def get_dilay(self, dilay):
        self._driver.find_element(By.CSS_SELECTOR, '#delay').clear()
        self._driver.find_element(By.CSS_SELECTOR, '#delay').send_keys(dilay)

    def get_numbers(self):
        spans = self._driver.find_elements(By.CSS_SELECTOR, 'span')
        spans[2].click()
        spans[5].click()
        spans[3].click()
        spans[16].click()

    def wait_result(self, wait_time):
        waiter = WebDriverWait(self._driver, wait_time)
        waiter.until(
            EC.invisibility_of_element((By.CSS_SELECTOR, '#spinner'))
            )

    def read_result(self):
        return self._driver.find_element(By.CSS_SELECTOR, 'div.screen').text
