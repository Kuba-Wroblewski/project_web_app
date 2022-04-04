from pages.test_page import TestPage
from pages.locators import HomePageLocators
from pages.authentication_page import AuthenticationPage
from pages.contact_page import ContactPage
from selenium.webdriver import ActionChains
from time import sleep


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

    def click_contact_us(self):
        '''
        clicks contact us
        '''
        contact_us = self.driver.find_element(*HomePageLocators.CONTACT_US)
        contact_us.click()
        # zwróc kolejna stronę (contact us)
        return ContactPage(self.driver)

    def check_all_price_products_on_site(self):
        '''
        check all product price on site
        '''
        lista_price_on_site = []
        find = self.driver.find_elements

        faded = find(*HomePageLocators.FADED)
        blouse = find(*HomePageLocators.BLOUSE)
        printed_dress = find(*HomePageLocators.PRINTED_DRESS)
        printed_dress_2 = find(*HomePageLocators.PRINTED_DRESS_2)
        printed_summer_dress = find(*HomePageLocators.PRINTED_SUMMER_DRESS)
        printed_summer_dress_2 = find(*HomePageLocators.PRINTED_SUMMER_DRESS_2)
        printed_chiffon_dress = find(*HomePageLocators.PRINTED_CHIFFON_DRESS)

        lista_products = (faded + blouse + printed_dress + printed_dress_2 +
                          printed_summer_dress + printed_summer_dress_2 + printed_chiffon_dress)

        for e in lista_products:
            lista_price_on_site.append(e.text)
        return lista_price_on_site

    def mouse_hover_to_products(self):
        '''
        hover the mouse over the products and get the price
        '''
        action = ActionChains(self.driver)
        find = self.driver.find_element

        faded = find(*HomePageLocators.FADED)
        under_faded = find(*HomePageLocators.UNDER_FADED)
        action.move_to_element(faded).move_to_element(under_faded).perform()
        price_under_faded = under_faded.text

        blouse = find(*HomePageLocators.BLOUSE)
        under_blouse = find(*HomePageLocators.UNDER_BLOUSE)
        action.move_to_element(blouse).move_to_element(under_blouse).perform()
        price_under_blouse = under_blouse.text

        printed_dress = find(*HomePageLocators.PRINTED_DRESS)
        under_printed_dress = find(*HomePageLocators.UNDER_PRINTED_DRESS)
        action.move_to_element(printed_dress).move_to_element(under_printed_dress).perform()
        price_under_printed_dress = under_printed_dress.text

        printed_dress_2 = find(*HomePageLocators.PRINTED_DRESS_2)
        under_printed_dress_2 = find(*HomePageLocators.UNDER_PRINTED_DRESS_2)
        action.move_to_element(printed_dress_2).move_to_element(under_printed_dress_2).perform()
        price_under_printed_dress_2 = under_printed_dress_2.text

        printed_summer_dress = find(*HomePageLocators.PRINTED_SUMMER_DRESS)
        under_printed_summer_dress = find(*HomePageLocators.UNDER_PRINTED_SUMMER_DRESS)
        action.move_to_element(printed_summer_dress).move_to_element(under_printed_summer_dress).perform()
        price_under_printed_summer_dress = under_printed_summer_dress.text

        printed_summer_dress_2 = find(*HomePageLocators.PRINTED_SUMMER_DRESS_2)
        under_printed_summer_dress_2 = find(*HomePageLocators.UNDER_PRINTED_SUMMER_DRESS_2)
        action.move_to_element(printed_summer_dress_2).move_to_element(under_printed_summer_dress_2).perform()
        price_under_printed_summer_dress_2 = under_printed_summer_dress_2.text

        printed_chiffon_dress = find(*HomePageLocators.PRINTED_CHIFFON_DRESS)
        under_printed_chiffon_dress = find(*HomePageLocators.UNDER_PRINTED_CHIFFON_DRESS)
        action.move_to_element(printed_chiffon_dress).move_to_element(under_printed_chiffon_dress).perform()
        price_under_printed_chiffon_dress = under_printed_chiffon_dress.text

        lista_price_products_hover_mouse = [price_under_faded, price_under_blouse, price_under_printed_dress,
                                            price_under_printed_dress_2, price_under_printed_summer_dress,
                                            price_under_printed_summer_dress_2, price_under_printed_chiffon_dress]

        return lista_price_products_hover_mouse

    def go_to_quick_view_of_products(self):
        '''
        hover the mouse over the product and enter a quick preview of the product
        '''
        action = ActionChains(self.driver)
        find = self.driver.find_element
        finds = self.driver.find_elements
        lista_price_in_quick_view = []

        faded = find(*HomePageLocators.FADED)
        quick_faded = find(*HomePageLocators.QUICK_FADED)

        a = action.move_to_element(faded).move_to_element(quick_faded).click().perform()
        self.driver.switch_to.frame(a)

        # self.driver.switch_to.frame(action.move_to_element(faded).move_to_element(quick_faded).click().perform())
        # body_window = finds(*HomePageLocators.BODY_WINDOW_QUICK_VIEW)
        tweet = find(*HomePageLocators.TWEET)
        tweet.click()
        # self.driver.switch_to.frame(body_window)


        # in_quick_faded = find(*HomePageLocators.IN_QUICK_FADED)
        # in_quick_faded2 = finds(*HomePageLocators.IN_QUICK_FADED)
        # in_quick_faded2 = finds(*HomePageLocators.IN_QUICK_FADED)


        """
        blouse = find(*HomePageLocators.BLOUSE)
        quick_blouse = find(*HomePageLocators.QUICK_BLOUSE)
        action.move_to_element(blouse).move_to_element(quick_blouse).click().perform()
        # price_under_blouse = under_blouse.text


        
        printed_dress = find(*HomePageLocators.PRINTED_DRESS)
        under_printed_dress = find(*HomePageLocators.UNDER_PRINTED_DRESS)
        action.move_to_element(printed_dress).move_to_element(under_printed_dress).perform()
        price_under_printed_dress = under_printed_dress.text

        printed_dress_2 = find(*HomePageLocators.PRINTED_DRESS_2)
        under_printed_dress_2 = find(*HomePageLocators.UNDER_PRINTED_DRESS_2)
        action.move_to_element(printed_dress_2).move_to_element(under_printed_dress_2).perform()
        price_under_printed_dress_2 = under_printed_dress_2.text

        printed_summer_dress = find(*HomePageLocators.PRINTED_SUMMER_DRESS)
        under_printed_summer_dress = find(*HomePageLocators.UNDER_PRINTED_SUMMER_DRESS)
        action.move_to_element(printed_summer_dress).move_to_element(under_printed_summer_dress).perform()
        price_under_printed_summer_dress = under_printed_summer_dress.text

        printed_summer_dress_2 = find(*HomePageLocators.PRINTED_SUMMER_DRESS_2)
        under_printed_summer_dress_2 = find(*HomePageLocators.UNDER_PRINTED_SUMMER_DRESS_2)
        action.move_to_element(printed_summer_dress_2).move_to_element(under_printed_summer_dress_2).perform()
        price_under_printed_summer_dress_2 = under_printed_summer_dress_2.text

        printed_chiffon_dress = find(*HomePageLocators.PRINTED_CHIFFON_DRESS)
        under_printed_chiffon_dress = find(*HomePageLocators.UNDER_PRINTED_CHIFFON_DRESS)
        action.move_to_element(printed_chiffon_dress).move_to_element(under_printed_chiffon_dress).perform()
        price_under_printed_chiffon_dress = under_printed_chiffon_dress.text

        lista_price_products_quick_view = [price_under_faded, price_under_blouse, price_under_printed_dress,
                                           price_under_printed_dress_2, price_under_printed_summer_dress,
                                           price_under_printed_summer_dress_2, price_under_printed_chiffon_dress]

        print(lista_price_products_quick_view)
        """
    def get_alert_message(self):
        '''
        returns all user errors
        '''
        # alerts = self.driver.find_elements(*ContactUsPageLocators.ALERT_SUCCESS_MESSAGES)
        # alerts_messages = []
        # for e in alerts:
        #     alerts_messages.append(e.text)
        # return alerts_messages

    def get_errors_message(self):
        '''
        returns all user errors
        '''
        # errors = self.driver.find_elements(*ContactUsPageLocators.ERROR_MESSAGES)
        # errors_messages = []
        # for e in errors:
        #     errors_messages.append(e.text)
        # return errors_messages

    def _verify_page(self):
        '''
        verifies home page
        '''
        pass
