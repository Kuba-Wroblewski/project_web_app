from pages.test_page import TestPage
from pages.locators import ShoppingPageLocators
from pages.addresses_page import AddressesPage
from time import sleep


class ShoppingCartPage(TestPage):
    """
    Shopping cart summary page
    """
    def proceed_to_checkout(self):
        """
        Button proceed to checkout
        """
        click_button = self.driver.find_element(*ShoppingPageLocators.BTN_PROCEED_TO_CHECKOUT)
        click_button.click()
        return AddressesPage(self.driver)

    def get_quantity_of_cart(self):
        """
        get quantity products of cart
        """
        cart_quantity_total = []
        get_quantity = self.driver.find_elements(*ShoppingPageLocators.CART_QUANTITY)
        for e in get_quantity:
            cart_quantity_total.append(e.text)
        return cart_quantity_total

    def get_summary_products_in_cart(self):
        """
        get summary products in cart
        """
        summary_products = []
        get_summary_products = self.driver.find_elements(*ShoppingPageLocators.CART_SUMMARY_OF_PRODUCTS)
        for e in get_summary_products:
            summary_products.append(e.text)
        return summary_products

    def add_more_first_product_in_the_cart(self, times=None):
        """
        Add more products in the cart by button in cart
        """
        quantity_product = self.driver.find_element(*ShoppingPageLocators.QUANTITY_OF_PRODUCTS_FIRST)
        total = int(quantity_product.get_attribute('value'))

        button_add = self.driver.find_element(*ShoppingPageLocators.BTN_ADD_PRODUCTS_FIRST)
        while total < times:
            total += 1
            button_add.click()

    def delete_second_product_in_cart(self):
        """
        delete second product in cart
        """
        btn_subtract = self.driver.find_element(*ShoppingPageLocators.BTN_DELETE_PRODUCT_SECOND)
        btn_subtract.click()

    def delete_product_icon_delete(self):
        """
        removing a product via the delete icon
        """
        btn_icon_delete = self.driver.find_element(*ShoppingPageLocators.BTN_ICON_DELETE_FIRST_PRODUCT)
        btn_icon_delete.click()

    def add_first_product_qty(self, quantity):
        """
        Add moore quantity first product in box
        """
        qty_box = self.driver.find_element(*ShoppingPageLocators.QUANTITY_FIRST_BOX).send_keys(quantity)

    def add_second_product_qty(self, quantity):
        """
        Add moore quantity first product in box
        """
        qty_box = self.driver.find_element(*ShoppingPageLocators.QUANTITY_SECOND_BOX).send_keys(quantity)

    def alert_for_user(self):
        """
        Alert message for user
        """
        alert_list = []
        alert = self.driver.find_elements(*ShoppingPageLocators.ALERT_FOR_USER)
        # alert quantity_product.get_attribute('class')

        for e in alert:
            alert_list.append(e.text)
        return alert_list

    def get_unit_price_first_product_in_cart(self):
        """
        Get unit price of first products
        """
        unit_price_first_product = self.driver.find_element(*ShoppingPageLocators.UNIT_PRICE_FIRST_PRODUCT).text
        return unit_price_first_product

    def get_total_price_first_product_in_cart(self):
        """
        Get total price of first products
        """
        total_price_first_product = self.driver.find_element(*ShoppingPageLocators.TOTAL_PRICE_FIRST_PRODUCT).text
        return total_price_first_product

    def get_unit_price_second_product_in_cart(self):
        """
        Get unit price of second products
        """
        unit_price_second_product = self.driver.find_element(*ShoppingPageLocators.UNIT_PRICE_SECOND_PRODUCT).text
        return unit_price_second_product

    def get_total_price_second_product_in_cart(self):
        """
        Get total price of second products
        """
        total_price_second_product = self.driver.find_element(*ShoppingPageLocators.TOTAL_PRICE_SECOND_PRODUCT).text
        return total_price_second_product

    def convert_str_and_sum(self, *arg):
        """
        convert srt to float and minus $
        """
        lista = [*arg]
        f_list = [entry.replace('$', '') for entry in lista]

        lista_cen = 0
        for i in range(len(f_list)):
            f_list[i] = float(f_list[i])
            lista_cen += f_list[i]
        lista_cen = int(lista_cen/0.01)/100
        return lista_cen

    def get_price_total_products_in_cart(self):
        """
        Price of total products in cart
        """
        total_products_price = self.driver.find_element(*ShoppingPageLocators.TOTAL_PRODUCTS_PRICE_IN_CART).text
        return total_products_price

    def get_price_of_total_shipping(self):
        """
        Get price of total shipping
        """
        total_price_shipping = self.driver.find_element(*ShoppingPageLocators.TOTAL_PRICE_SHIPPING).text
        return total_price_shipping

    def continue_shopping(self):
        """
        Button to undo the page "Continue shopping"
        """
