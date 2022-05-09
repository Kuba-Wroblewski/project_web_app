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
            self.assertEqual(errors, errors_messages)
        else:
            print("\n", "Expected errors >>", errors)
            print("Current errors >>", errors_messages)
            self.assertEqual(errors, errors_messages)
        sleep(2)

    @unittest.skip("skip")
    def test_checking_price_of_product(self):
        """
        TC 001 Checking the price of all products on home site,
        and in the new window "MORE" view of products
        """
        home_page = self.home_page
        # 1. Sprawdzamy ceny wszystkich produktów widocznych na stronie
        price_of_products_on_site = home_page.check_all_price_products_on_site()
        # 2. Sprawdzamy ceny po najechaniu myszką na produkt
        # najechać myszką na każdy produkt i pobranie ceny produktu
        products_price_on_mouse_over = home_page.mouse_hover_to_products()
        # 3. Sprawdzamy ceny w nowej karcie produktu "More"
        price_of_products_in_view_more = home_page.getting_the_price_of_products_when_push_button_more()
        # 4. Weryfikujemy ceny względem kroków poprzednich
        # Weryfikacja cen z kroku 3 względem kroku 2
        self.verify_errors_messages(price_of_products_on_site, products_price_on_mouse_over)
        # Weryfikacja cen z kroku 1 względem kroku 3
        self.verify_errors_messages(price_of_products_on_site, price_of_products_in_view_more)

    @unittest.skip("skip")
    def test_placing_an_order(self):
        """
        TC 002 placing the order with login user
        """
        home_page = self.home_page
        # logowanie klienta
        authentication_page = home_page.click_sign_in()
        # wpisz dane klienta
        my_account_page = authentication_page.log_in(self.test_data.login_email, self.test_data.login_password)
        # Cofnij się do strony domowej "Home"
        my_account_page.back_to_home_page()
        # 1. Dodać jeden produkt do koszyka
        # 2. klikamy przejdź do kasy
        shopping_cart_page = home_page.add_the_first_product_to_the_cart_go_to_cart()
        # 3. W koszyku klikamy przejdź do kasy
        addresses_page = shopping_cart_page.proceed_to_checkout()
        # 4. W polu Adres klikamy przejdź do kasy
        shipping_page = addresses_page.proceed_to_checkout()
        # 5. W polu wysyłka klikamy przejdź do kasy
        shipping_page.agree_to_the_terms_of_service()
        your_payment_methods = shipping_page.proceed_to_checkout()
        # 6. W polu płatność wybieramy zapłać przelewem bankowym
        order_summary_page = your_payment_methods.pay_by_bank_wire()
        # 7. Klikamy potwierdź moje zamówienie
        confirm_my_order = order_summary_page.confirm_my_order()
        order_message = confirm_my_order.get_message_your_confirm_order()
        # Oczekiwany rezultat:
        # 1. Użytkownik dostaje komunikat na stronie:
        # "Your order on My Store is complete."
        messages = 'Your order on My Store is complete.'
        self.verify_errors_messages(messages, order_message)

    @unittest.skip("skip")
    def test_adding_and_removing_products_from_the_cart(self):
        """
        TC 003 Adding and removing products from the cart
        """
        home_page = self.home_page
        # logowanie klienta
        authentication_page = home_page.click_sign_in()
        # wpisz dane klienta
        my_account_page = authentication_page.log_in(self.test_data.login_email, self.test_data.login_password)
        # Cofnij się do strony domowej "Home"
        my_account_page.back_to_home_page()
        # 1. Dodać jeden produkt do koszyka
        # 2. klikamy kontynuować zakupy
        add_the_first_product = home_page.add_the_first_product_to_the_cart_continue_shopping()
        # 3. Dodać kolejny inny produkt do koszyka
        # 4. Przejdź do kasy (koszyka)
        shopping_cart_page = home_page.add_the_second_product_to_the_cart_go_to_cart()
        # 5. Weryfikacja ilości produktów w koszyku
        cart_quantity_total = shopping_cart_page.get_quantity_of_cart()
        cart_summary_products = shopping_cart_page.get_summary_products_in_cart()
        self.assertIn(cart_quantity_total[0], cart_summary_products[0])
        # 6. Zwiększenie ilości produktu pierwszego w koszyku poprzez
        #     przycisk "Dodać" przy produkcie, do ilości np. 5
        add_products_in_cart = shopping_cart_page.add_more_first_product_in_the_cart(5)
        # 7. Weryfikacja ilości produktów w koszyku
        sleep(5)
        cart_quantity_total = shopping_cart_page.get_quantity_of_cart()
        print(cart_quantity_total)
        cart_summary_products = shopping_cart_page.get_summary_products_in_cart()
        print(cart_summary_products)
        # self.assertIn(cart_quantity_total2[0], cart_summary_products2[0])
        self.assertIn(cart_quantity_total[0], cart_summary_products[0])
        # 8. Zmniejszenie ilości produktu drugiego w koszyku poprzez
        #     przycisk "Odjąć" przy produkcie, do liczby 0
        shopping_cart_page.delete_second_product_in_cart()
        sleep(2)
        # 9. Weryfikacja ilości produktów w koszyku
        cart_quantity_total = shopping_cart_page.get_quantity_of_cart()
        print(cart_quantity_total)
        cart_summary_products = shopping_cart_page.get_summary_products_in_cart()
        print(cart_summary_products)
        # 10. Usunięcie produktów z koszyka poprzez przycisk "Delete"
        delete_product_via_icon_delete = shopping_cart_page.delete_product_icon_delete()
        sleep(3)

        # Oczekiwany rezultat:
        # 1. Użytkownik nie powinien napotkać żadnego błędu.
        # 2. Użytkownik otrzymuje komunikat:
        #     'Your shopping cart is empty.'
        message = ['Your shopping cart is empty.']
        message_for_user = shopping_cart_page.alert_for_user()
        self.verify_errors_messages(message, message_for_user)

# @unittest.skip("skip")
    def test_price_of_product_when_adding_to_cart(self):
        """
        TC 004 Adding and removing products from the cart
        """
        home_page = self.home_page
        # logowanie klienta
        authentication_page = home_page.click_sign_in()
        # wpisz dane klienta
        my_account_page = authentication_page.log_in(self.test_data.login_email, self.test_data.login_password)
        # Cofnij się do strony domowej "Home"
        my_account_page.back_to_home_page()
        home_page = self.home_page
        # 1. Dodać jeden produkt do koszyka
        # 2. klikamy kontynuować zakupy
        add_the_first_product = home_page.add_the_first_product_to_the_cart_continue_shopping()
        # 3. Dodać kolejny inny produkt do koszyka
        # 4. Przejdź do kasy (koszyka)
        shopping_cart_page = home_page.add_the_second_product_to_the_cart_go_to_cart()
        # 5. Weryfikacja ceny produktu w koszyku -względem ceny całości produktu
        unit_price_first_product = shopping_cart_page.get_unit_price_first_product_in_cart()
        total_price_first_product = shopping_cart_page.get_total_price_first_product_in_cart()
        unit_price_second_product = shopping_cart_page.get_unit_price_second_product_in_cart()
        total_price_second_product = shopping_cart_page.get_total_price_second_product_in_cart()
        self.verify_errors_messages(unit_price_first_product, total_price_first_product)
        self.verify_errors_messages(unit_price_second_product, total_price_second_product)
        # 6. Zwiększenie ilości pierwszego produktu w koszyku poprzez
        #     wprowadzenie ilości np. 10
        add_products_first_in_cart = shopping_cart_page.add_first_product_qty(self.test_data.quantity)
        sleep(10)
        # 7. Weryfikacja ceny produktu w koszyku -względem ceny całości produktu
        unit_price_first_product = shopping_cart_page.get_unit_price_first_product_in_cart()
        convert_total_price_first_product = shopping_cart_page.convert_str_and_sum(
            shopping_cart_page.get_total_price_first_product_in_cart())

        multiply_unit_price_first = shopping_cart_page.convert_str_and_sum(unit_price_first_product)*10
        multiply_unit_price_first = round(multiply_unit_price_first, 2)
        self.verify_errors_messages(str(convert_total_price_first_product), str(multiply_unit_price_first))
        # 8. Zwiększenie ilości drugiego produktu w koszyku poprzez
        #     wprowadzenie ilości np. 10
        add_products_second_in_cart = shopping_cart_page.add_second_product_qty(self.test_data.quantity)
        sleep(10)
        # 9. Weryfikacja ceny produktu w koszyku -względem ceny całości produktu
        unit_price_second_product = shopping_cart_page.get_unit_price_second_product_in_cart()
        convert_total_price_second_product = shopping_cart_page.convert_str_and_sum(
            shopping_cart_page.get_total_price_second_product_in_cart())
        multiply_unit_price_second = shopping_cart_page.convert_str_and_sum(unit_price_second_product) * 10
        multiply_unit_price_second = round(multiply_unit_price_second, 2)
        self.verify_errors_messages(str(convert_total_price_second_product), str(multiply_unit_price_second))
        # 10. Weryfikacja ceny produktów w koszyku -względem ceny całości produktów
        total_price_products = convert_total_price_first_product + convert_total_price_second_product
        total_price_first_product = shopping_cart_page.get_total_price_first_product_in_cart()
        total_price_second_product = shopping_cart_page.get_total_price_second_product_in_cart()
        suma_price_all_products_in_cart = shopping_cart_page.convert_str_and_sum(
            total_price_first_product, total_price_second_product)
        total_price_products_in_cart = shopping_cart_page.convert_str_and_sum(
            shopping_cart_page.get_price_total_products_in_cart())
        self.verify_errors_messages(str(suma_price_all_products_in_cart), str(total_price_products_in_cart))
        # 11. Sprawdzenie naliczania kosztu transportu
        total_price_shipping = shopping_cart_page.get_price_of_total_shipping()
        # przekonwertowana cena transportu na float
        total_price_shipping_convert = shopping_cart_page.convert_str_and_sum(total_price_shipping)
        self.verify_errors_messages(self.test_data.price_shipping, total_price_shipping)
        # 12. Sprawdzenie naliczania VAT
        addresses_page = shopping_cart_page.proceed_to_checkout()
        shipping_page = addresses_page.proceed_to_checkout()
        shipping_page.agree_to_the_terms_of_service()
        your_payment_methods = shipping_page.proceed_to_checkout()
        # przekonwertowana cena vat
        price_total_tax_convert = your_payment_methods.convert_str_and_sum(your_payment_methods.price_of_tax())
        # przekonwertowana cena koszów produktów
        total_price_products_convert = your_payment_methods.convert_str_and_sum(your_payment_methods.total_price_products())
        #  przekonwertowana cena całego koszyka wraz z vat i transportem
        total_price_cart_convert = your_payment_methods.convert_str_and_sum(your_payment_methods.total_price_cart())
        # cenę produktów dodać cenę transportu dodać 4% vat powinno się równać z total cart (454.58)
        expected_price = 454.58
        total_price = (total_price_products_convert + total_price_shipping_convert) * self.test_data.tax
        total_price_convert = int(total_price / 0.01) / 100
        self.verify_errors_messages(str(expected_price), str(total_price_convert))
