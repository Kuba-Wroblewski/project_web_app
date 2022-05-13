from pages.test_page import TestPage
from pages.locators import HomePageLocators
from pages.locators import MoreLocatorsOfProducts
from pages.authentication_page import AuthenticationPage
from pages.contact_page import ContactPage
from selenium.webdriver import ActionChains
from pages.shopping_cart_page import ShoppingCartPage


class HomePage(TestPage):
    """
    landing page object and returns authenticationPage instance
    """
    def click_sign_in(self):
        '''
        clicks sign in
        '''
        # zlokalizuj sign in
        sign_in = self.driver.find_element(*HomePageLocators.SIGN_IN_LINK)
        # kliknij
        sign_in.click()
        # zwróć kolejna stronę (authentication page)
        return AuthenticationPage(self.driver)

    def click_contact_us(self):
        """
        clicks contact us
        """
        contact_us = self.driver.find_element(*HomePageLocators.CONTACT_US)
        contact_us.click()
        # zwróć kolejną stronę (contact us)
        return ContactPage(self.driver)

    def check_all_price_products_on_site(self):
        """
        check price of all products on home site
        """
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
        """
        hover the mouse over the products and get the price
        """
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

        lista_price_products_hover_mouse = [
            price_under_faded, price_under_blouse, price_under_printed_dress, price_under_printed_dress_2,
            price_under_printed_summer_dress, price_under_printed_summer_dress_2, price_under_printed_chiffon_dress]

        return lista_price_products_hover_mouse

    def getting_the_price_of_products_when_push_button_more(self):
        """
        hover the mouse over the product and click button "more" for all products
        """
        action = ActionChains(self.driver)
        find = self.driver.find_element
        lista_price_products = []

        faded = find(*HomePageLocators.FADED)
        btn_more_faded = find(*HomePageLocators.BTN_MORE_FADED)

        action.move_to_element(faded).move_to_element(btn_more_faded).click().perform()
        price_faded = self.driver.find_element(*MoreLocatorsOfProducts.FADED).text
        lista_price_products.append(price_faded); self.driver.back()

        blouse = find(*HomePageLocators.BLOUSE)
        btn_more_blouse = find(*HomePageLocators.BTN_MORE_BLOUSE)

        action.move_to_element(blouse).move_to_element(btn_more_blouse).click().perform()
        price_blouse = self.driver.find_element(*MoreLocatorsOfProducts.BLOUSE).text
        lista_price_products.append(price_blouse); self.driver.back()

        printed_dress = find(*HomePageLocators.PRINTED_DRESS)
        btn_more_printed_dress = find(*HomePageLocators.BTN_MORE_PRINTED_DRESS)

        action.move_to_element(printed_dress).move_to_element(btn_more_printed_dress).click().perform()
        price_printed_dress = self.driver.find_element(*MoreLocatorsOfProducts.PRINTED_DRESS).text
        lista_price_products.append(price_printed_dress); self.driver.back()

        printed_dress_2 = find(*HomePageLocators.PRINTED_DRESS_2)
        btn_more_printed_dress_2 = find(*HomePageLocators.BTN_MORE_PRINTED_DRESS_2)

        action.move_to_element(printed_dress_2).move_to_element(btn_more_printed_dress_2).click().perform()
        price_printed_dress_2 = self.driver.find_element(*MoreLocatorsOfProducts.PRINTED_DRESS_2).text
        lista_price_products.append(price_printed_dress_2); self.driver.back()

        printed_summer_dress = find(*HomePageLocators.PRINTED_SUMMER_DRESS)
        btn_more_printed_summer_dress = find(*HomePageLocators.BTN_MORE_PRINTED_SUMMER_DRESS)

        action.move_to_element(printed_summer_dress).move_to_element(btn_more_printed_summer_dress).click().perform()
        price_printed_summer_dress = self.driver.find_element(*MoreLocatorsOfProducts.PRINTED_SUMMER_DRESS).text
        lista_price_products.append(price_printed_summer_dress); self.driver.back()

        printed_summer_dress_2 = find(*HomePageLocators.PRINTED_SUMMER_DRESS_2)
        btn_more_printed_summer_dress_2 = find(*HomePageLocators.BTN_MORE_PRINTED_SUMMER_DRESS_2)

        action.move_to_element(printed_summer_dress_2).move_to_element(btn_more_printed_summer_dress_2).click().perform()
        price_printed_summer_dress_2 = self.driver.find_element(*MoreLocatorsOfProducts.PRINTED_SUMMER_DRESS_2).text
        lista_price_products.append(price_printed_summer_dress_2); self.driver.back()

        printed_chiffon_dress = find(*HomePageLocators.PRINTED_CHIFFON_DRESS)
        btn_more_printed_chiffon_dress = find(*HomePageLocators.BTN_MORE_PRINTED_CHIFFON_DRESS)

        action.move_to_element(printed_chiffon_dress).move_to_element(btn_more_printed_chiffon_dress).click().perform()
        price_printed_chiffon_dress = self.driver.find_element(*MoreLocatorsOfProducts.PRINTED_CHIFFON_DRESS).text
        lista_price_products.append(price_printed_chiffon_dress); self.driver.back()
        return lista_price_products

    def add_the_first_product_to_the_cart_go_to_cart(self):
        """
        Add the product to the cart
        """
        action = ActionChains(self.driver)
        find = self.driver.find_element

        faded = find(*HomePageLocators.FADED)
        btn_add_to_cart = find(*HomePageLocators.ADD_TO_CART_BTN)
        action.move_to_element(faded).move_to_element(btn_add_to_cart).click().perform()
        find(*HomePageLocators.BTN_TO_CHECKOUT).click()
        return ShoppingCartPage(self.driver)

    def add_the_first_product_to_the_cart_continue_shopping(self):
        """
        Add the first product to the cart and continue shopping
        """
        action = ActionChains(self.driver)
        find = self.driver.find_element

        faded = find(*HomePageLocators.FADED)
        btn_add_to_cart = find(*HomePageLocators.ADD_TO_CART_BTN)
        action.move_to_element(faded).move_to_element(btn_add_to_cart).click().perform()
        find(*HomePageLocators.BTN_CONTINUE_CHECKOUT).click()

    def add_the_second_product_to_the_cart_go_to_cart(self):
        """
        Add the product to the cart
        """
        action = ActionChains(self.driver)
        find = self.driver.find_element

        blouse = find(*HomePageLocators.BLOUSE)
        btn_add_to_cart = find(*HomePageLocators.ADD_PRODUCT2_TO_CART_BTN)
        action.move_to_element(blouse).move_to_element(btn_add_to_cart).click().perform()
        find(*HomePageLocators.BTN_TO_CHECKOUT).click()
        return ShoppingCartPage(self.driver)

    def get_alert_message(self):
        """
        returns all user errors
        """
        # alerts = self.driver.find_elements(*ContactUsPageLocators.ALERT_SUCCESS_MESSAGES)
        # alerts_messages = []
        # for e in alerts:
        #     alerts_messages.append(e.text)
        # return alerts_messages

    def get_errors_message(self):
        """
        returns all user errors
        """
        # errors = self.driver.find_elements(*ContactUsPageLocators.ERROR_MESSAGES)
        # errors_messages = []
        # for e in errors:
        #     errors_messages.append(e.text)
        # return errors_messages

    def _verify_page(self):
        """
        verifies home page
        """
        pass
