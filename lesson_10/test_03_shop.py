from selenium import webdriver
from pageShop import PageShop
import allure


@allure.title("Интернет магазин")
@allure.description("Добавить товары в корзину и проверить, что их итоговая стоимость расчитывается правильно")
@allure.feature("Корзина")
@allure.severity("critical")
def test_shop():
    with allure.step("Открыть Chrome"):
        browser = webdriver.Chrome()
    with allure.step("Перейти на сайт магазина"):
        shop_page = PageShop(browser)
    shop_page.authorization("standard_user", "secret_sauce")
    shop_page.add_to_cart()
    shop_page.get_cart()
    shop_page.push_checkout()
    shop_page.fill_out_the_form("Артём", "Пугачёв", "123456")
    shop_page.push_continue()
    total = shop_page.read_total()
    with allure.step("Проверить итоговую сумму заказа"):
        assert total == "Total: $58.29"
    with allure.step("Закрыть Chrome"):
        browser.quit()
