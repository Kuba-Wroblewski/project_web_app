from pages.test_page import TestPage
from pages.locators import AuthenticationPageLocators
from pages.create_an_account_page import CreateAnAccountPage


class AuthenticationPage(TestPage):
    '''
    authentication page object
    '''

    def create_account_with_email(self, email):
        '''
        creates an account page and return acreateanaccount instance
        '''
        enter_email = self.driver.find_element(*AuthenticationPageLocators.CREATE_AN_ACCOUNT_EMAIL)
        enter_email.send_keys(email)
        button_create = self.driver.find_element(*AuthenticationPageLocators.BUTTON_CREATE_AN_ACCOUNT)
        button_create.click()
        # return create an account page instance
        return CreateAnAccountPage(self.driver)

    def log_in(self, email, password):
        pass

    def input_email_in_create_account(self, email):
        pass

    def click_create_an_account(self):
        pass

    def _verify_page(self):
        '''
        verifications authentication page
        '''
        pass
