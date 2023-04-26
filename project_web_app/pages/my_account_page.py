from pages.test_page import TestPage
from pages.locators import MyAccountPageLocators


class MyAccountPage(TestPage):
    """
    My Account page
    """
    def back_to_home_page(self):
        """
        Back to Home page
        """
        button_home = self.driver.find_element(*MyAccountPageLocators.BTN_HOME).click()
