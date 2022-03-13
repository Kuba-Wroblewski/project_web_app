from selenium.webdriver.common.by import By


class HomePageLocators():
    '''
    locators use on home page
    '''
    SIGN_IN_LINK = (By.CLASS_NAME, 'header_user_info')


class AuthenticationPageLocators():
    '''
    location use on authentication page
    '''
    CREATE_AN_ACCOUNT_EMAIL = (By.ID, 'email_create')
    BUTTON_CREATE_AN_ACCOUNT = (By.ID, 'SubmitCreate')
    # do testu 001
    ERROR_MESSAGES = (By.XPATH, "//div[@class='alert alert-danger']/ol/li")


class CreateAnAccountPageLocators():
    '''
    location use on account page
    '''
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
    ADRESS = (By.ID, 'address1')
    CITY = (By.ID, 'city')
    POSTCODE = (By.ID, 'postcode')
    STATE = (By.ID, 'id_state')
    PHONE_NUMBER = (By.ID, 'phone_mobile')
    ADDRESS_ALIAS = (By.ID, 'alias')
    REGISTER_BUTTON = (By.ID, 'submitAccount')
    NUMBER_OF_MESSAGES_ERRORS = (By.XPATH, "//div[@class='alert alert-danger']/p")
    ERROR_MESSAGES = (By.XPATH, "//div[@class='alert alert-danger']/ol/li")







