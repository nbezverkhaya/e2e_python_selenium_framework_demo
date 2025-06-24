from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class CheckoutConfirmation:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_btn = (By.XPATH, "//button[@class='btn btn-success']")
        self.country_input = (By.XPATH, "//input[@id='country']")
        self.country_option = (By.LINK_TEXT, "Germany")
        self.checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.confirm_btn = (By.CSS_SELECTOR, "[type='submit']")
        self.success_message = (By.CLASS_NAME, "alert-success")

    def checkout(self):
        self.driver.find_element(*self.checkout_btn).click()

    def enter_delivery_address(self):
        self.driver.find_element(*self.country_input).send_keys("ge")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_all_elements_located(self.country_option))
        self.driver.find_element(*self.country_option).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.confirm_btn).click()

    def validate_order(self):
        success_text = self.driver.find_element(*self.success_message).text
        assert "Thank you! Your order will be delivered in next few weeks :-)." in success_text



