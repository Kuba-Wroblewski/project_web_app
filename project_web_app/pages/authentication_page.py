from pages.test_page import TestPage
from pages.locators import AuthenticationPageLocators
from pages.create_an_account_page import CreateAnAccountPage


class AuthenticationPage(TestPage):
    '''
    authentication page object
    '''
    def create_account_with_email(self, email):
        '''
        creates an account page and return a create an account instance
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
        '''
        click create an account
        '''
        self.driver.find_element(*AuthenticationPageLocators.BUTTON_CREATE_AN_ACCOUNT).click()

    def get_errors_messages(self):
        '''
        returns all user errors
        '''
        errors = self.driver.find_elements(*AuthenticationPageLocators.ERROR_MESSAGES)
        errors_message = []
        for e in errors:
            errors_message.append(e.text)
        return errors_message

    def _verify_page(self):
        '''
        verifications authentication page
        '''
        pass
