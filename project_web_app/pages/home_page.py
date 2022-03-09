from pages.test_page import TestPage
from pages.locators import HomePageLocators
from pages.authentication_page import AuthenticationPage


class HomePage(TestPage):
    '''
    landing page object and returns authenticationPage instance
    '''
    def click_sign_in(self):
        '''
        clicks sign in
        '''
        # zlokalizuj sign in
        # print('typ', type(*HomePageLocators.SIGN_IN_LINK))
        sign_in = self.driver.find_element(*HomePageLocators.SIGN_IN_LINK)
        # kliknij
        sign_in.click()
        # zwroc kolejna stronę (authentication page)
        return AuthenticationPage(self.driver)

    def _verify_page(self):
        '''
        verifies home page
        '''
        pass
