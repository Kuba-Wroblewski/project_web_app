from pages.test_page import TestPage
from pages.locators import AddressesPageLocators
from pages.shipping_page import ShippingPage


class AddressesPage(TestPage):
    """
    Addresses page
    """
    def proceed_to_checkout(self):
        """
        Button proceed to checkout
        """
        click_button = self.driver.find_element(*AddressesPageLocators.BTN_PROCEED_TO_CHECKOUT)
        click_button.click()
        return ShippingPage(self.driver)