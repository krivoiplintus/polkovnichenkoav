from selenium import webdriver
from pageForm import PageForm
import allure


@allure.title("Форма")
@allure.description("Заполнить форму данными кроме поля 'zip_code', проверить что поле подсвечено красным, а остальные поля зелёным")
@allure.feature("Форма")
@allure.severity("critical")
def test_form():
    with allure.step("Открыть Chrome"):
        browser = webdriver.Chrome()
    with allure.step("Перейти на сайт с формой"):
        form_page = PageForm(browser)
    form_page.data_get_form(
        "Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787", "Москва", "Россия", "QA", "SkyPro", ""
        )
    form_page.click_submit()
    zip_code_class = form_page.find_zip_code_class()
    with allure.step("Проверить что поле 'zip_code' подсвечено красным"):
        assert zip_code_class == "alert py-2 alert-danger"
    all_elements = form_page.find_all_element_class()
    with allure.step("Проверить что остальные поля подсвечены зелёным"):
        assert all_elements == 9
    with allure.step("Закрыть Chrome"):
        browser.quit()
