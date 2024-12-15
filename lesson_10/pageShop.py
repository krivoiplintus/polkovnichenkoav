from selenium.webdriver.common.by import By
import allure


class PageShop:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.maximize_window()

    @allure.step("Авторизоваться на сайте")
    def authorization(self, user_name=str, password=str) -> None:
        """
            Этот метод вводит данные в поля авторизации и нажимает кнопку 'login'
        """
        self._driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys(user_name)
        self._driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
        self._driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    @allure.step("Добавить в корзину товары")
    def add_to_cart(self) -> None:
        """
            Этот метод добавляет в корзину товары выбранные для тестирования
        """
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

    @allure.step("Перейти в корзину")
    def get_cart(self) -> None:
        """
            Переход на страницу корзины
        """
        self._driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container').click()

    @allure.step("Нажать кнопку 'checkout'")
    def push_checkout(self) -> None:
        """
            Этот метод нажимает кнопку 'checkout'
        """
        self._driver.find_element(By.CSS_SELECTOR, '#checkout').click()

    @allure.step("Заполнить форму с данными пользователя")
    def fill_out_the_form(self, first_name=str, last_name=str, postal_code=str) -> None:
        """
            Этот метод заполняет форму тестовыми данными пользователя
        """
        self._driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(first_name)
        self._driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(last_name)
        self._driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(postal_code)

    @allure.step("Нажать кнопку 'continue'")
    def push_continue(self) -> None:
        """
            Этот метод нажимает кнопку 'continue'
        """
        self._driver.find_element(By.CSS_SELECTOR, '#continue').click()

    @allure.step("Получить итоговую сумму заказа")
    def read_total(self) -> str:
        """
            Этот метод получает итоговую сумму заказа
        """
        return self._driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text
