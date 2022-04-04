from selenium.webdriver.support.select import Select
from pages.test_page import TestPage
from pages.locators import CreateAnAccountPageLocators


class CreateAnAccountPage(TestPage):
    '''
    create an account page object
    '''
    def choose_gender(self, gender):
        # jesli facet to wybierz mr
        if gender == 'male':
            # choose mr
            self.driver.find_element(*CreateAnAccountPageLocators.GENDER_MALE).click()
        else:
            # a jak kobieta to wybierz mrs
            self.driver.find_element(*CreateAnAccountPageLocators.GENDER_FEMALE).click()

    def enter_name(self, name):
        '''
        enter first name
        '''
        first_name = self.driver.find_element(*CreateAnAccountPageLocators.PERSONAL_FIRST_NAME)
        first_name.send_keys(name)

    def enter_lastname(self, name):
        '''
        enter last name
        '''
        last_name = self.driver.find_element(*CreateAnAccountPageLocators.PERSONAL_LAST_NAME)
        last_name.send_keys(name)

    def get_email(self):
        '''
        returns email entered in input below last name
        '''
        return_email = self.driver.find_element(*CreateAnAccountPageLocators.EMAIL)
        return return_email.get_attribute('value')

    def enter_password(self, password):
        '''
        Enter password
        '''
        enter_password = self.driver.find_element(*CreateAnAccountPageLocators.PASSWORD)
        enter_password.send_keys(password)

    def choose_birthday(self, date):
        '''
        Enter date = birthday
        '''
        # self.birthday = '1985-02-19'
        date_splitted = date.split('-')
        year = date_splitted[0]
        month = str(int(date_splitted[1]))
        day = date_splitted[2]
        day_select = Select(self.driver.find_element(*CreateAnAccountPageLocators.BIRTHDAY))
        day_select.select_by_value(day)
        month_select = Select(self.driver.find_element(*CreateAnAccountPageLocators.MONTHS))
        month_select.select_by_value(month)
        year_select = Select(self.driver.find_element(*CreateAnAccountPageLocators.YEARS))
        year_select.select_by_value(year)

    def get_first_name(self):
        '''
        verify entered in input below name
        '''
        first_name = self.driver.find_element(*CreateAnAccountPageLocators.ADDRESS_FIRST_NAME)
        return first_name.get_attribute('value')

    def get_last_name(self):
        '''
        verify entered in input below last name
        '''
        last_name = self.driver.find_element(*CreateAnAccountPageLocators.ADDRESS_LAST_NAME)
        # przewiniecie do elementu
        last_name.location_once_scrolled_into_view
        return last_name.get_attribute('value')

    def enter_adress(self, adress):
        '''
        enter adress
        '''
        enter_adress = self.driver.find_element(*CreateAnAccountPageLocators.ADDRESS)
        enter_adress.send_keys(adress)

    def enter_city(self, city):
        '''
        enter city
        '''
        enter_city = self.driver.find_element(*CreateAnAccountPageLocators.CITY)
        enter_city.send_keys(city)

    def enter_postal_code(self, postcode):
        post_code = self.driver.find_element(*CreateAnAccountPageLocators.POSTCODE)
        post_code.send_keys(postcode)

    def enter_state(self, state):
        '''
        enter state
        '''
        enter_state = Select(self.driver.find_element(*CreateAnAccountPageLocators.STATE))
        enter_state.select_by_visible_text(state)

    def enter_mobile_phone_number(self, phone):
        '''
        enter phone number
        '''
        phone_number = self.driver.find_element(*CreateAnAccountPageLocators.PHONE_NUMBER)
        phone_number.send_keys(phone)

    def enter_address_alias(self, alias):
        '''
        enter address alias
        '''
        enter_alias = self.driver.find_element(*CreateAnAccountPageLocators.ADDRESS_ALIAS)
        enter_alias.clear()
        enter_alias.send_keys(alias)

    def click_register_button(self):
        '''
        click register
        '''
        self.driver.find_element(*CreateAnAccountPageLocators.REGISTER_BUTTON).click()

    def get_numbers_of_errors_visible_text(self):
        '''
        returns the message with the number of errors commited by the user
        '''
        # znajduje wszystkie bledy - lista web elementy
        el = self.driver.find_elements(*CreateAnAccountPageLocators.NUMBER_OF_MESSAGES_ERRORS)
        number_errors_text = []
        for e in el:
            # dodaje do listy widoczny teks
            number_errors_text.append(e.text)
        return number_errors_text

    def get_errors_messages(self):
        '''
        returns all user errors
        '''
        errors = self.driver.find_elements(*CreateAnAccountPageLocators.ERROR_MESSAGES)
        errors_message = []
        for e in errors:
            errors_message.append(e.text)
        return errors_message

    def _verify_page(self):
        '''
        verifications create an account page
        '''
        pass
