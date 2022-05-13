from selenium.webdriver.common.by import By


class HomePageLocators():
    """
    locators use on home page
    """
    SIGN_IN_LINK = (By.CLASS_NAME, 'header_user_info')
    CONTACT_US = (By.ID, 'contact-link')
    FADED = (By.XPATH, '//*[@id="homefeatured"]/li[1]/div/div[2]/div[1]/span')
    BLOUSE = (By.XPATH, '//*[@id="homefeatured"]/li[2]/div/div[2]/div[1]/span')
    PRINTED_DRESS = (By.XPATH, '//*[@id="homefeatured"]/li[3]/div/div[2]/div[1]/span')
    PRINTED_DRESS_2 = (By.XPATH, '//*[@id="homefeatured"]/li[4]/div/div[2]/div[1]/span')
    PRINTED_SUMMER_DRESS = (By.XPATH, '//*[@id="homefeatured"]/li[5]/div/div[2]/div[1]/span[1]')
    PRINTED_SUMMER_DRESS_2 = (By.XPATH, '//*[@id="homefeatured"]/li[6]/div/div[2]/div[1]/span')
    PRINTED_CHIFFON_DRESS = (By.XPATH, '//*[@id="homefeatured"]/li[7]/div/div[2]/div[1]/span[1]')
    # po najechaniu myszką
    UNDER_FADED = (By.XPATH, '//*[@id="homefeatured"]/li[1]/div/div[1]/div/div[2]/span')
    UNDER_BLOUSE = (By.XPATH, '//*[@id="homefeatured"]/li[2]/div/div[1]/div/div[2]/span')
    UNDER_PRINTED_DRESS = (By.XPATH, '//*[@id="homefeatured"]/li[3]/div/div[1]/div/div[2]/span')
    UNDER_PRINTED_DRESS_2 = (By.XPATH, '//*[@id="homefeatured"]/li[4]/div/div[1]/div/div[2]/span')
    UNDER_PRINTED_SUMMER_DRESS = (By.XPATH, '//*[@id="homefeatured"]/li[5]/div/div[1]/div/div[2]/span[1]')
    UNDER_PRINTED_SUMMER_DRESS_2 = (By.XPATH, '//*[@id="homefeatured"]/li[6]/div/div[1]/div/div[2]/span')
    UNDER_PRINTED_CHIFFON_DRESS = (By.XPATH, '//*[@id="homefeatured"]/li[7]/div/div[1]/div/div[2]/span[1]')
    # quick view
    BTN_MORE_FADED = (By.XPATH, "//a[@title='View']")
    BTN_MORE_BLOUSE = (By.XPATH, '//*[@id="homefeatured"]/li[2]/div/div[2]/div[2]/a[2]')
    BTN_MORE_PRINTED_DRESS = (By.XPATH, '//*[@id="homefeatured"]/li[3]/div/div[2]/div[2]/a[2]')
    BTN_MORE_PRINTED_DRESS_2 = (By.XPATH, '//*[@id="homefeatured"]/li[4]/div/div[2]/div[2]/a[2]')
    BTN_MORE_PRINTED_SUMMER_DRESS = (By.XPATH, '//*[@id="homefeatured"]/li[5]/div/div[2]/div[2]/a[2]')
    BTN_MORE_PRINTED_SUMMER_DRESS_2 = (By.XPATH, '//*[@id="homefeatured"]/li[6]/div/div[2]/div[2]/a[2]')
    BTN_MORE_PRINTED_CHIFFON_DRESS = (By.XPATH, '//*[@id="homefeatured"]/li[7]/div/div[2]/div[2]/a[2]')
    # Add product to cart
    ADD_TO_CART_BTN = (By.XPATH, "//a[@class='button ajax_add_to_cart_button btn btn-default']")
    ADD_PRODUCT2_TO_CART_BTN = (By.XPATH, "//a[@class='button ajax_add_to_cart_button btn btn-default'][@data-id-product='2']")
    BTN_TO_CHECKOUT = (By.LINK_TEXT, "Proceed to checkout")
    BTN_CONTINUE_CHECKOUT = (By.XPATH, "//span[@title='Continue shopping']")


class ShoppingPageLocators():
    """
    locators use on shopping page
    """
    BTN_PROCEED_TO_CHECKOUT = (By.PARTIAL_LINK_TEXT, 'Proceed to checkout')
    CART_QUANTITY = (By.XPATH, "//a/span[@class='ajax_cart_quantity']")
    CART_PRICE_TOTAL = (By.XPATH, "//a/span[@class='ajax_cart_total']")
    CART_SUMMARY_OF_PRODUCTS = (By.ID, 'summary_products_quantity')
    BTN_ADD_PRODUCTS_FIRST = (By.ID, 'cart_quantity_up_1_1_0_670353')
    BTN_SUBTRACT_PRODUCTS_FIRST = (By.ID, 'cart_quantity_down_1_1_0_670353')
    BTN_ADD_PRODUCTS_SECOND = (By.ID, 'cart_quantity_up_2_7_0_670353')
    BTN_SUBTRACT_PRODUCTS_SECOND = (By.ID, 'cart_quantity_down_2_7_0_670353')
    QUANTITY_OF_PRODUCTS_FIRST = (By.NAME, 'quantity_1_1_0_670353_hidden')
    ERROR_MESSAGE = (By.XPATH, "//p[@class='fancybox-error']")
    BTN_DELETE_PRODUCT_SECOND = (By.ID, 'cart_quantity_down_2_7_0_670353')
    BTN_ICON_DELETE_FIRST_PRODUCT = (By.ID, '1_1_0_670353')
    ALERT_FOR_USER = (By.XPATH, "//p[@class='alert alert-warning']")
    UNIT_PRICE_FIRST_PRODUCT = (By.ID, 'product_price_1_1_670353')
    TOTAL_PRICE_FIRST_PRODUCT = (By.ID, 'total_product_price_1_1_670353')
    UNIT_PRICE_SECOND_PRODUCT = (By.ID, 'product_price_2_7_670353')
    TOTAL_PRICE_SECOND_PRODUCT = (By.ID, 'total_product_price_2_7_670353')
    QUANTITY_FIRST_BOX = (By.NAME, 'quantity_1_1_0_670353')
    QUANTITY_SECOND_BOX = (By.NAME, 'quantity_2_7_0_670353')
    TOTAL_PRICE_SHIPPING = (By.ID, 'total_shipping')
    TOTAL_PRODUCTS_PRICE_IN_CART = (By.ID, 'total_product')


class MyAccountPageLocators():
    """
    locators use on My Account page
    """
    BTN_HOME = (By.PARTIAL_LINK_TEXT, 'Home')


class AddressesPageLocators():
    """
    locators use on Addresses page
    """
    BTN_PROCEED_TO_CHECKOUT = (By.NAME, 'processAddress')


class ShippingPageLocators():
    """
    locators use on Shipping page
    """
    BTN_PROCEED_TO_CHECKOUT = (By.NAME, 'processCarrier')
    CHECK_THE_BOX = (By.ID, 'uniform-cgv')


class YourPaymentMethodLocators():
    """
    locators use on Your Payment Method page
    """
    BTN_PAY_BY_BANK_WIRE = (By.PARTIAL_LINK_TEXT, 'Pay by bank wire')
    PRICE_TOTAL_TAX = (By.ID, 'total_tax')
    PRICE_TOTAL_PRODUCTS = (By.ID, 'total_product')
    PRICE_TOTAL_CART = (By.ID, 'total_price')


class OrderSummaryLocators():
    """
    locators use on Order Summary page
    """
    BTN_CONFIRM_MY_ORDER = (By.XPATH, "//button[@class='button btn btn-default button-medium']")
    GET_MESSAGE_ORDER = (By.XPATH, '//*[@id="center_column"]/div/p/strong')


class OrderConfirmationLocators():
    """
    locators use on Order confirmation page
    """
    GET_MESSAGE_ORDER = (By.XPATH, '//*[@id="center_column"]/div/p/strong')


class MoreLocatorsOfProducts():
    """
    Locators of all products in window to more information of product
    """
    FADED = (By.ID, 'our_price_display')
    BLOUSE = (By.ID, 'our_price_display')
    PRINTED_DRESS = (By.ID, 'our_price_display')
    PRINTED_DRESS_2 = (By.ID, 'our_price_display')
    PRINTED_SUMMER_DRESS = (By.ID, 'our_price_display')
    PRINTED_SUMMER_DRESS_2 = (By.ID, 'our_price_display')
    PRINTED_CHIFFON_DRESS = (By.ID, 'our_price_display')


class AuthenticationPageLocators():
    """
    locators use on authentication page
    """
    CREATE_AN_ACCOUNT_EMAIL = (By.ID, 'email_create')
    BUTTON_CREATE_AN_ACCOUNT = (By.ID, 'SubmitCreate')
    # do testu 001
    ERROR_MESSAGES = (By.XPATH, "//div[@id='create_account_error']/ol/li")
    ALREADY_REGISTERED_EMAIL = (By.ID, 'email')
    ALREADY_REGISTERED_PASSWORD = (By.ID, 'passwd')
    BTN_SUBMIT_LOGIN = (By.ID, 'SubmitLogin')


class CreateAnAccountPageLocators():
    """
    locators use on account page
    """
    PERSONAL_FIRST_NAME = (By.ID, 'customer_firstname')
    GENDER_MALE = (By.ID, 'id_gender1')
    GENDER_FEMALE = (By.ID, 'id_gender2')
    PERSONAL_LAST_NAME = (By.ID, 'customer_lastname')
    EMAIL = (By.ID, 'email')
    PASSWORD = (By.ID, 'passwd')
    BIRTHDAY = (By.ID, 'days')
    MONTHS = (By.ID, 'months')
    YEARS = (By.ID, 'years')
    ADDRESS_FIRST_NAME = (By.ID, 'firstname')
    ADDRESS_LAST_NAME = (By.ID, 'lastname')
    ADDRESS = (By.ID, 'address1')
    CITY = (By.ID, 'city')
    POSTCODE = (By.ID, 'postcode')
    STATE = (By.ID, 'id_state')
    PHONE_NUMBER = (By.ID, 'phone_mobile')
    ADDRESS_ALIAS = (By.ID, 'alias')
    REGISTER_BUTTON = (By.ID, 'submitAccount')
    NUMBER_OF_MESSAGES_ERRORS = (By.XPATH, "//div[@class='alert alert-danger']/p")
    ERROR_MESSAGES = (By.XPATH, "//div[@class='alert alert-danger']/ol/li")


class ContactUsPageLocators():
    """
    locators use on contact page
    """
    CHOOSE_SUBJECT = (By.ID, 'id_contact')
    EMAIL = (By.ID, 'email')
    ORDER_REFERENCE = (By.ID, 'id_order')
    ATTACH_FILE = (By.XPATH, "//div[@id='uniform-fileUpload']/input")
    CONTACT_MESSAGE = (By.ID, 'message')
    SEND_BUTTON = (By.ID, 'submitMessage')
    ALERT_SUCCESS_MESSAGES = (By.XPATH, "//p[@class='alert alert-success']")
    ERROR_MESSAGES = (By.XPATH, "//div[@class='alert alert-danger']/ol/li")
