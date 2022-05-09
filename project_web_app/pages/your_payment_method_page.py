from pages.test_page import TestPage
from pages.locators import YourPaymentMethodLocators
from pages.order_summary_page import OrderSummaryPage


class YourPaymentMethod(TestPage):
    """
    Choose Your payment method page
    """
    def pay_by_bank_wire(self):
        """
        Button proceed to checkout
        """
        click_button = self.driver.find_element(*YourPaymentMethodLocators.BTN_PAY_BY_BANK_WIRE)
        click_button.click()
        return OrderSummaryPage(self.driver)

    def price_of_tax(self):
        """
        Price of tax for the order
        """
        price_total_tax = self.driver.find_element(*YourPaymentMethodLocators.PRICE_TOTAL_TAX).text
        return price_total_tax

    def total_price_products(self):
        """
        Total price products
        """
        total_price_products = self.driver.find_element(*YourPaymentMethodLocators.PRICE_TOTAL_PRODUCTS).text
        return total_price_products

    def total_price_cart(self):
        """
        Total price cart with all cost, like tax and shipping
        """
        total_price_cart = self.driver.find_element(*YourPaymentMethodLocators.PRICE_TOTAL_CART).text
        return total_price_cart

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

    def pay_by_check(self):
        pass
