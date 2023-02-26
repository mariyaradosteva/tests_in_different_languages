from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_button_add_to_basket(browser):
    browser.get(link)
    find = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    time.sleep(30)
    assert len(find) > 0, "Не найдена кнопка добавления в корзину"
    