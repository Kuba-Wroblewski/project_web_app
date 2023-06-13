from pages.test_page import TestPage
from pages.locators import OrderSummaryLocators
from pages.order_confirmation_page import OrderConfirmationPage


class OrderSummaryPage(TestPage):
    """
    Order Summary Page
    """
    def confirm_my_order(self):
        """
        Click button to confirm my order
        """
        click_button = self.driver.find_element(*OrderSummaryLocators.BTN_CONFIRM_MY_ORDER)
        click_button.click()
        return OrderConfirmationPage(self.driver)
