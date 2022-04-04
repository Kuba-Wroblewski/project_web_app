import unittest
from tests.test_data import TestData
from tests.new_test import NewTest
from time import sleep


class ContactUs(NewTest):
    '''
    send a message to service team  automationpractice.com
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

    @unittest.skip("skip")
    def test_send_message_with_all_fields_typed(self):
        '''
        TC 001 send a message to service team, all fields typed
        '''
        home_page = self.home_page
        # 1. Kliknij „Contact us”
        contact_page = home_page.click_contact_us()
        # 2. Wybierz rodzaj zapytania
        contact_page.choose_subject_heading(self.test_data.choose)
        # 3. Wpisz e-mail
        contact_page.enter_email(self.test_data.email)
        # 4. Wpisz numer referencyjny zamówienia
        contact_page.enter_reference(self.test_data.default_number)
        # 5. załącz plik np. .jpg
        contact_page.generation_random_graphic(self.test_data.image)
        contact_page.attach_file(self.test_data.image_put)
        # 6. Wpisz wiadomość np. losowe słowo
        contact_page.enter_contact_message(self.test_data.default_word)
        # 7. Kliknij przycisk "Send"
        contact_page.click_send_button()

        # Oczekiwany rezultat:
        # 1. Użytkownik otrzymuje komunikat: "Your message has been successfully sent to our team."
        alerts = ['Your message has been successfully sent to our team.']
        alerts_messages = contact_page.get_alert_message()
        self.verify_errors_messages(alerts, alerts_messages)
        # Warunki końcowe:
        # 1. Wiadomość zostaje wysłana

    @unittest.skip("skip")
    def test_send_message_all_fields_blank(self):
        '''
        TC 002 try to send a message to service with all blank fields
        '''
        home_page = self.home_page
        # 1. Kliknij „Contact us”
        contact_page = home_page.click_contact_us()
        # 2. Kliknij przycisk "Send"
        contact_page.click_send_button()

        # Oczekiwany rezultat:
        # 1. Użytkownik otrzymuje komunikat "."
        errors = ['Invalid email address.']
        errors_messages = contact_page.get_errors_message()
        self.verify_errors_messages(errors, errors_messages)
        # Warunki końcowe:
        # 1. Wiadomość nie zostaje wysłana
        # użytkownik powinień otrzymać komunikat również:
        # "The message cannot be blank."
        # "Please select a subject from the list provided."
        # "The Order reference is blank"
        # "The Attach File is blank"

    @unittest.skip("skip")
    def test_send_message_only_typed_subject(self):
        '''
        TC 003 try to send a message to service with only typed in subject fields
        '''
        home_page = self.home_page
        # 1. Kliknij „Contact us”
        contact_page = home_page.click_contact_us()
        # 2. Wybierz rodzaj zapytania
        contact_page.choose_subject_heading(self.test_data.choose)
        # 3. Kliknij przycisk "Send"
        contact_page.click_send_button()

        # Oczekiwany rezultat:
        # 1. Użytkownik otrzymuje komunikat "."
        errors = ['Invalid email address.']
        errors_messages = contact_page.get_errors_message()
        self.verify_errors_messages(errors, errors_messages)
        # Warunki końcowe:
        # 1. Wiadomość nie zostaje wysłana
        # użytkownik powinień otrzymać komunikat również:
        # "Please select a subject from the list provided."
        # "The message cannot be blank."
        # "The Order reference is blank"
        # "The Attach File is blank"

    @unittest.skip("skip")
    def test_send_message_typed_subject_and_email(self):
        '''
        TC 004 try to send a message to service, typed in subject and email
        '''
        home_page = self.home_page
        # 1. Kliknij „Contact us”
        contact_page = home_page.click_contact_us()
        # 2. Wybierz rodzaj zapytania
        contact_page.choose_subject_heading(self.test_data.choose)
        # 3. Wpisz email
        contact_page.enter_email(self.test_data.email)
        # 4. Kliknij przycisk "Send"
        contact_page.click_send_button()

        # Oczekiwany rezultat:
        # 1. Użytkownik otrzymuje komunikat:
        errors = ['The message cannot be blank.']
        errors_messages = contact_page.get_errors_message()
        self.verify_errors_messages(errors, errors_messages)
        # Warunki końcowe:
        # 1. Wiadomość nie zostaje wysłana
        # użytkownik powinień otrzymać komunikat również:
        # "The Order reference is blank"
        # "The Attach File is blank"

    @unittest.skip("skip")
    def test_send_message_typed_email_and_message(self):
        '''
        TC 005 try to send a message to service, typed email and message
        '''
        home_page = self.home_page
        # 1. Kliknij „Contact us”
        contact_page = home_page.click_contact_us()
        # 2. Wpisz email
        contact_page.enter_email(self.test_data.email)
        # 3. Wpisz przykładowy teks w pole meesage
        contact_page.enter_contact_message(self.test_data.default_word)
        # 4. Kliknij przycisk "Send"
        contact_page.click_send_button()

        # Oczekiwany rezultat:
        # 1. Użytkownik otrzymuje komunikat:
        errors = ['Please select a subject from the list provided.']
        errors_messages = contact_page.get_errors_message()
        self.verify_errors_messages(errors, errors_messages)
        # Warunki końcowe:
        # 1. Wiadomość nie zostaje wysłana
        # użytkownik powinień otrzymać komunikat również:
        # "The Order reference is blank"
        # "The Attach File is blank"

    # @unittest.skip("skip")
    def test_name_of_the_tab_contact_us(self):
        '''
        TC 007 name of the tab contact us
        '''
        home_page = self.home_page
        # 1. Kliknij „Contact us”
        contact_page = home_page.click_contact_us()
        # 2. Sprawdź tytuł zakładki na której jesteś
        print(self.driver.title)
        # Oczekiwany rezultat:
        # 1. Użytkownik otrzymuje komunikat:
        errors = ['Contact us - My Store']
        errors_messages = [self.driver.title]
        self.verify_errors_messages(errors, errors_messages)
        # Warunki końcowe:
        # 1. zakładka ma nazwę "Contact us - My Store"
