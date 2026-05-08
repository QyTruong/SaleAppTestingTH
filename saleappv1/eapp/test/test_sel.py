import time

import pytest
from selenium.webdriver.common.by import By

from eapp.test.pages.HomePage import HomePage
from eapp.test.test_base import driver
import time


def test_search_product(driver):
    kw = 'iPhone'
    home = HomePage(driver=driver)
    home.open_page()
    home.search(kw)

    time.sleep(1)

    results = driver.find_elements(By.CSS_SELECTOR, '.container .card-title')
    assert all(kw in r.text for r in results)



def test_add_to_cart(driver):
    home = HomePage(driver=driver)
    home.open_page()

    home.add_to_cart()

    driver.implicitly_wait(1)

    count = driver.find_element(By.CLASS_NAME, 'cart-counter')
    assert int(count.text) == 3