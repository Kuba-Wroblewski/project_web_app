import unittest
from tests.new_test import NewTest
from time import sleep


class ProductTest(NewTest):
    """
    checking the price of products
    """
    # @unittest.skip("skip")
    def verify_errors_messages(self, errors, errors_messages):
        """
        verifies errors displayed for the user
        verify all errors and successfully message
        """
        alert = 'successfully'
        for element in errors:
            element
        if alert in element:
            print("\n", "Expected successfully alerty >>", errors)
            print("Current successfully alerty >>", errors_messages)
            self.assertCountEqual(errors, errors_messages)
        else:
            print("\n", "Expected errors >>", errors)
            print("Current errors >>", errors_messages)
            self.assertCountEqual(errors, errors_messages)
        sleep(2)

    @unittest.skip("skip")
    def test_checking_price_of_product(self):
        """
        TC 001 checking the price of all products on home site
        """
        home_page = self.home_page
        # 1. Sprawdzamy ceny wszystkich produktów widocznych na stronie
        price_of_products_on_site = home_page.check_all_price_products_on_site()
        # print('\nPrice of products on home site', price_of_products_on_site)
        # 2. Sprawdzamy ceny po najechaniu myszką na produkt
        # najechać myszką na każdy produkt i pobranie ceny produktu
        products_price_on_mouse_over = home_page.mouse_hover_to_products()
        # print('Price of products on hovering over the mouse', products_price_on_mouse_over)
        # 3. Sprawdzamy ceny w nowej karcie produktu "More"
        price_of_products_in_view_more = home_page.getting_the_price_of_products_when_push_button_more()
        # print('Price of products when click button "more"', price_of_products_in_view_more)
        # 4. Weryfikujemy ceny względem kroków poprzednich
        self.verify_errors_messages(price_of_products_on_site, products_price_on_mouse_over)
        self.verify_errors_messages(price_of_products_on_site, price_of_products_in_view_more)

    def test_name_cart(self):
        """
        TC 002 Testing the name of cards and the names of buttons
        """


















