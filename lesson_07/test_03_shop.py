from selenium import webdriver
from pageShop import PageShop


def test_shop():
    browser = webdriver.Chrome()
    shop_page = PageShop(browser)
    shop_page.authorization("standard_user", "secret_sauce")
    shop_page.add_to_cart()
    shop_page.get_cart()
    shop_page.push_checkout()
    shop_page.fill_out_the_form("Артём", "Пугачёв", "123456")
    shop_page.push_continue()
    total = shop_page.read_total()
    browser.quit()
    assert total == "Total: $58.29"
