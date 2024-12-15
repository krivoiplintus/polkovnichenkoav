from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class PageCalc:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.maximize_window()

    @allure.step("Установить задержку в работе калькулятора")
    def get_dilay(self, dilay=str) -> None:
        """
            Этот метол устанавливает задержку в работе калькулятора
        """
        self._driver.find_element(By.CSS_SELECTOR, '#delay').clear()
        self._driver.find_element(By.CSS_SELECTOR, '#delay').send_keys(dilay)

    @allure.step("Ввести тестовые данные, нажать кнопку равно")
    def get_numbers(self):
        """
            Этот метод вводит тестовые значения на клавиатуре калькулятора и нажимает на кнопку равно
        """
        spans = self._driver.find_elements(By.CSS_SELECTOR, 'span')
        spans[2].click()
        spans[5].click()
        spans[3].click()
        spans[16].click()

    @allure.step("Подождать вывод результата вычислений калькулятора")
    def wait_result(self, wait_time=str) -> None:
        """
        Этот метод нужен для ожидания вывода результата вычисления калькулятора
        """
        waiter = WebDriverWait(self._driver, wait_time)
        waiter.until(
            EC.invisibility_of_element((By.CSS_SELECTOR, '#spinner'))
            )

    @allure.step("Считать результат вычислений")
    def read_result(self) -> str:
        """
            Этот метод получает результат работы калькулятора
        """
        return self._driver.find_element(By.CSS_SELECTOR, 'div.screen').text
