from selenium import webdriver
from pageCalc import PageCalc
import allure


@allure.title("Калькулятор")
@allure.description("Протестировать вычисления калькулятора")
@allure.feature("Калькулятор")
@allure.severity("critical")
def test_calc():
    with allure.step("Открыть Chrome"):
        browser = webdriver.Chrome()
    with allure.step("Перейти на сайт с калькулятором"):
        calc_page = PageCalc(browser)
    calc_page.get_dilay("45")
    calc_page.get_numbers()
    calc_page.wait_result("50")
    result = calc_page.read_result()
    with allure.step("Проверить результат вычислений"):
        assert result == "15"
    with allure.step("Закрыть Chrome"):
        browser.quit()
