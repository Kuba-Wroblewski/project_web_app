from selenium.webdriver.support.select import Select
from pages.test_page import TestPage
from pages.locators import ContactUsPageLocators
import urllib.request
import os


class ContactPage(TestPage):
    """
    contact page object
    """
    def choose_subject_heading(self, choose):
        """
        choose subject heading for the contact
        """
        # str_choose = str(choose)
        choose_select = Select(self.driver.find_element(*ContactUsPageLocators.CHOOSE_SUBJECT))
        choose_select.select_by_value(str(choose))

    def enter_email(self, email):
        """
        enter your email
        """
        enter_email = self.driver.find_element(*ContactUsPageLocators.EMAIL)
        enter_email.send_keys(email)

    def clears_field_email(self):
        """
        clears field of email
        """
        clear_email = self.driver.find_element(*ContactUsPageLocators.EMAIL).clear()

    def enter_reference(self, reference):
        """
        enter order reference
        """
        enter_reference = self.driver.find_element(*ContactUsPageLocators.ORDER_REFERENCE)
        enter_reference.send_keys(reference)

    def generate_random_graphic(self, image):
        """
        generation random graphic from url
        """
        urllib.request.urlretrieve(image, "/home/amd/Pulpit/my_project_alk/project_web_app/graphics/random.jpg")

    def attach_file(self, image_put):
        """
        attach helpful file like .jpg from disc
        """
        put_to_url = self.driver.find_element(*ContactUsPageLocators.ATTACH_FILE)
        put_to_url.send_keys(image_put)

    def enter_contact_message(self, message):
        """
        enter message explaining the problem to service
        """
        enter_message = self.driver.find_element(*ContactUsPageLocators.CONTACT_MESSAGE)
        enter_message.send_keys(message)

    def click_send_button(self):
        """
        click send button to send a message
        """
        click_send_button = self.driver.find_element(*ContactUsPageLocators.SEND_BUTTON).click()

    def get_alert_message(self):
        """
        returns all user errors
        """
        alerts = self.driver.find_elements(*ContactUsPageLocators.ALERT_SUCCESS_MESSAGES)
        alerts_messages = []
        for e in alerts:
            alerts_messages.append(e.text)
        return alerts_messages

    def get_errors_message(self):
        """
        returns all user errors
        """
        errors = self.driver.find_elements(*ContactUsPageLocators.ERROR_MESSAGES)
        errors_messages = []
        for e in errors:
            errors_messages.append(e.text)
        return errors_messages
