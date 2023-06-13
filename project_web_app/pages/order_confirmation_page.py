from pages.test_page import TestPage
from pages.locators import OrderSummaryLocators


class OrderConfirmationPage(TestPage):
    """
    Order Confirmation page
    """
    def get_message_your_confirm_order(self):
        """
        Your message when you confirm the order
        """
        get_message = self.driver.find_element(*OrderSummaryLocators.GET_MESSAGE_ORDER)
        return get_message.text
