from selenium.webdriver.common.by import By
from pageObjects.checkout_confirmation_page import CheckoutConfirmation

class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.shop_link = (By.CSS_SELECTOR, "a[href*='shop']")
        self.all_products = (By.XPATH, "//div[@class='card h-100']")
        self.checkout_button = (By.XPATH, "//div/ul/li/a")

    def add_product_to_card(self, product_name):
        self.driver.find_element(*self.shop_link).click()
        products = self.driver.find_elements(*self.all_products)
        for product in products:
            prodName = self.driver.find_element(By.XPATH, "//div/h4/a").text
            if prodName == product_name:
                product.find_element(By.XPATH, "div/button").click()

    def go_to_cart(self):
        self.driver.find_element(*self.checkout_button).click()
        return CheckoutConfirmation(self.driver)