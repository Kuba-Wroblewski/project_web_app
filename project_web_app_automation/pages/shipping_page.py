from pages.test_page import TestPage
from pages.locators import ShippingPageLocators
from pages.your_payment_method_page import YourPaymentMethod


class ShippingPage(TestPage):
    """
    Shipping page
    """
    def proceed_to_checkout(self):
        """
        Button proceed to checkout
        """
        click_button = self.driver.find_element(*ShippingPageLocators.BTN_PROCEED_TO_CHECKOUT)
        click_button.click()
        return YourPaymentMethod(self.driver)

    def agree_to_the_terms_of_service(self):
        """
        Agree checkbox to the terms of service
        """
        check_the_box = self.driver.find_element(*ShippingPageLocators.CHECK_THE_BOX)
        check_the_box.click()
