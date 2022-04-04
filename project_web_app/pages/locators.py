from selenium.webdriver.common.by import By


class HomePageLocators():
    '''
    locators use on home page
    '''
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
    QUICK_FADED = (By.XPATH, '//*[@id="homefeatured"]/li[1]/div/div[1]/div/a[2]/span')
    QUICK_BLOUSE = (By.XPATH, '//*[@id="homefeatured"]/li[2]/div/div[1]/div/a[2]/span')
    QUICK_PRINTED_DRESS = (By.XPATH, '//*[@id="homefeatured"]/li[3]/div/div[1]/div/a[2]/span')
    QUICK_PRINTED_DRESS_2 = (By.XPATH, '//*[@id="homefeatured"]/li[4]/div/div[1]/div/a[2]/span')
    QUICK_PRINTED_SUMMER_DRESS = (By.XPATH, '//*[@id="homefeatured"]/li[5]/div/div[1]/div/a[2]/span')
    QUICK_PRINTED_SUMMER_DRESS_2 = (By.XPATH, '//*[@id="homefeatured"]/li[6]/div/div[1]/div/a[2]/span')
    QUICK_PRINTED_CHIFFON_DRESS = (By.XPATH, '//*[@id="homefeatured"]/li[7]/div/div[1]/div/a[2]/span')
    # quick view price
    IN_QUICK_FADED = (By.XPATH, '//*[@id="our_price_display"]')
    BODY_WINDOW_QUICK_VIEW = (By.XPATH, '//*[@id="fancybox-frame1648214234805"]')
    COLORS = (By.XPATH, '//*[@id="color_14"]')
    TWEET = (By.XPATH, '//*[@id="product"]/div/div/div[2]/p[7]/button[1]')
    IN_QUICK_BLOUSE = (By.XPATH, '//*[@id="our_price_display"]')
    IN_QUICK_PRINTED_DRESS = (By.XPATH, '//*[@id="our_price_display"]')
    IN_QUICK_PRINTED_DRESS_2 = (By.XPATH, '//*[@id="our_price_display"]')
    IN_QUICK_PRINTED_SUMMER_DRESS = (By.XPATH, '//*[@id="our_price_display"]')
    IN_QUICK_PRINTED_SUMMER_DRESS_2 = (By.XPATH, '//*[@id="our_price_display"]')
    IN_QUICK_PRINTED_CHIFFON_DRESS = (By.XPATH, '//*[@id="our_price_display"]')


class AuthenticationPageLocators():
    '''
    locators use on authentication page
    '''
    CREATE_AN_ACCOUNT_EMAIL = (By.ID, 'email_create')
    BUTTON_CREATE_AN_ACCOUNT = (By.ID, 'SubmitCreate')
    # do testu 001
    ERROR_MESSAGES = (By.XPATH, "//div[@class='alert alert-danger']/ol/li")


class CreateAnAccountPageLocators():
    '''
    locators use on account page
    '''
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
    '''
    locators use on contact page
    '''
    CHOOSE_SUBJECT = (By.ID, 'id_contact')
    EMAIL = (By.ID, 'email')
    ORDER_REFERENCE = (By.ID, 'id_order')
    ATTACH_FILE = (By.XPATH, "//div[@id='uniform-fileUpload']/input")
    CONTACT_MESSAGE = (By.ID, 'message')
    SEND_BUTTON = (By.ID, 'submitMessage')
    ALERT_SUCCESS_MESSAGES = (By.XPATH, "//p[@class='alert alert-success']")
    ERROR_MESSAGES = (By.XPATH, "//div[@class='alert alert-danger']/ol/li")
