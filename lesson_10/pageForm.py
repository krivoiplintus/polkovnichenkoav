from selenium.webdriver.common.by import By
import allure


class PageForm:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.maximize_window()

    @allure.step("Заполнить поля формы тестовыми данными")
    def data_get_form(self, first_name=str, last_name=str, address=str, e_mail=str, phone=str, city=str, country=str, job_position=str, company=str, zip_code=str) -> None:
        """
            Этот метод заполняет поля формы тестовыми данными
        """
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

    @allure.step("Нажать кнопку 'submit'")
    def click_submit(self) -> None:
        """
            Этот метод нажимает на кнопку 'submit'
        """
        self._driver.find_element(By.CSS_SELECTOR, 'button').click()

    @allure.step("Считать атрибут 'class' элемента 'zip-code'")
    def find_zip_code_class(self) -> str:
        """
            Этот метод возвращает атрибут 'class' элемента 'zip-code'
        """
        return self._driver.find_element(By.CSS_SELECTOR, '#zip-code').get_attribute("class")

    @allure.step("Получить список остальных элементов с успешно введёнными данными")
    def find_all_element_class(self) -> []:
        """
            Этот метод возвращает список всех остальных элементов с успешно введёнными данными
        """
        return len(self._driver.find_elements(By.CSS_SELECTOR, 'div.alert.py-2.alert-success'))
