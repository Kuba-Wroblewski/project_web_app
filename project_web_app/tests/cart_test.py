import unittest
from tests.test_data import TestData
from tests.new_test import NewTest
from time import sleep

"""
class CartTest(NewTest):
    '''
    Cart test, add, deleted
    '''
"""


class ProductTest(NewTest):
    '''
    checking the price of products
    '''
    # @unittest.skip("skip")
    def verify_errors_messages(self, errors, errors_messages):
        '''
        verifies errors displayed for the user
        verify all errors and successfully message
        '''
        alert = 'successfully'
        for element in errors:
            print(element)
        if alert in element:
            print("\n", "Expected successfully alerty >>", errors)
            print("Current successfully alerty >>", errors_messages)
            self.assertCountEqual(errors, errors_messages)
        else:
            print("\n", "Expected errors >>", errors)
            print("Current errors >>", errors_messages)
            self.assertCountEqual(errors, errors_messages)
        sleep(2)

    # @unittest.skip("skip")
    def test_checking_price_of_product(self):
        '''
        TC 001 checking the price of all products on home site
        '''
        home_page = self.home_page
        # 1. Sprawdzamy ceny wszystkich produktów widocznych na stronie
        price_of_products_on_site = home_page.check_all_price_products_on_site()
        print(price_of_products_on_site)
        # ceny produktów widocznych na stronie głównej pod produktem
        # 2. Sprawdzamy ceny po najechaniu myszką
        # najechać myszką na każdy produkt
        # i pobranie ceny produktu
        # products_price_on_mouse_over = home_page.mouse_hover_to_products()
        # 3. Sprawdzamy ceny w oknie "Quick view"
        # home_page.go_to_quick_view_of_products()

        # 4. Weryfikujemy ceny względem kroków poprzednich
        # self.verify_errors_messages(price_of_products_on_site, products_price_on_mouse_over)































