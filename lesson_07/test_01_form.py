from selenium import webdriver
from pageForm import PageForm


def test_form():
    browser = webdriver.Chrome()
    form_page = PageForm(browser)
    form_page.data_get_form(
        "Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787", "Москва", "Россия", "QA", "SkyPro", ""
        )
    form_page.click_submit()
    zip_code_class = form_page.find_zip_code_class()
    assert zip_code_class == "alert py-2 alert-danger"
    all_elements = form_page.find_all_element_class()
    assert all_elements == 9
    browser.quit()
