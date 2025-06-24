import json

import pytest

import time
from pageObjects.login_page import LoginPage
test_data_path = './data/e2e_test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data['data']

@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browser_instance, test_list_item):
    driver = browser_instance
    login_page = LoginPage(driver)
    shop_page = login_page.login(test_list_item["user_email"], test_list_item["user_password"])
    shop_page.add_product_to_card(test_list_item["product_name"])
    checkout_page = shop_page.go_to_cart()
    checkout_page.checkout()
    checkout_page.enter_delivery_address()
    checkout_page.validate_order()

    time.sleep(5)
    driver.close() 





