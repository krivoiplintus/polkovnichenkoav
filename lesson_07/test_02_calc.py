from selenium import webdriver
from pageCalc import PageCalc


def test_calc():
    browser = webdriver.Chrome()
    calc_page = PageCalc(browser)
    calc_page.get_dilay("45")
    calc_page.get_numbers()
    calc_page.wait_result("50")
    result = calc_page.read_result()
    assert result == "15"
    browser.quit()
