from tests.new_test import NewTest
from time import sleep
from tests.test_data import TestData


class RegistrationTest(NewTest):
    '''
    registration tests
    '''

    def verify_errors_messages(self, errors, errors_messages):
        '''
        verifies errors displayed for the user
        verify all errors
        '''
        print(errors)
        print(errors_messages)
        self.assertCountEqual(errors, errors_messages)

        # 2-ga opcja sprawdzania błędów -poprzez self.assert...Equal (problem z pobieraniem errors)
        # print('Wyprintowanie błędów >>', self.authentication_page.get_errors_messages())
        # self.assertCountEqual(self.authentication_page.get_errors_messages(), errors)

    def test_no_email(self):
        '''
        TC 001 Not typed by user email in email window.
        '''
        home_page = self.home_page
        # 1. Kliknij „Sign in”
        self.authentication_page = home_page.click_sign_in()
        # 2. Kliknij przycisk „Create account”
        self.authentication_page.click_create_an_account()
        # Oczekiwany rezultat:
        # 1. Użytkownik otrzymuje komunikat „Invalid email address.”
        errors = ['Invalid email address.']
        errors_messages = self.authentication_page.get_errors_messages()
        self.verify_errors_messages(errors, errors_messages)
        # Warunki końcowe:
        # 1. Konto nie zostaje założone

    def test_number_in_the_email_field(self):
        '''
        TC 002 typed a number in the email field
        '''
        home_page = self.home_page
        # 1. Kliknij „Sign in”
        self.authentication_page = home_page.click_sign_in()
        # 2. Wprowadż cyfre w pole email
        self.authentication_page.create_account_with_email(self.test_data.email_number)
        # 2. Kliknij przycisk „Create account”
        self.authentication_page.click_create_an_account()
        # Oczekiwany rezultat:
        # 1. Użytkownik otrzymuje komunikat „Invalid email address.”
        errors = ['Invalid email address.']
        errors_messages = self.authentication_page.get_errors_messages()
        self.verify_errors_messages(errors, errors_messages)
        # Warunki końcowe:
        # 1. Konto nie zostaje założone



    def pass_test(self):
        pass

    def test_no_name(self):
        '''
        TC ALK (w szkole). click mr if gender is male and mrs otherwise ( otherwize - w innym przypadku)
        '''
        home_page = self.home_page
        # 1. kliknij sign in
        authentication_page = home_page.click_sign_in()
        # 2. wpisz e-mail
        # 3. kliknij przycisk create account
        create_an_account_page = authentication_page.create_account_with_email(self.test_data.email)
        # 4. wybierrz płeć
        create_an_account_page.choose_gender(self.test_data.gender)
        # 5. Wpisz nazwisko
        create_an_account_page.enter_lastname(self.test_data.last_name)
        # 6. Sprawdz poprawnosc emaila
        # pokaze nam co mamy w emailu
        # print(create_an_account_page.get_email())
        self.assertEqual(self.test_data.email, create_an_account_page.get_email(), 'mail different from previously!')
        # 7. Wpisz hasło
        create_an_account_page.enter_password(self.test_data.password)
        # 8. wpisz datę urodzenia
        create_an_account_page.choose_birthday(self.test_data.birthday)
        # 9. Sprawdź pole „First name”
        create_an_account_page.get_first_name()
        self.assertEqual(create_an_account_page.get_first_name(), '')
        # 10. Sprawdź pole „Last name”
        # pokazuje nam pole last name
        # print(create_an_account_page.get_first_name(), create_an_account_page.get_last_name())
        create_an_account_page.get_last_name()
        self.assertEqual(create_an_account_page.get_last_name(), self.test_data.last_name)
        # 11. Wpisz adres
        create_an_account_page.enter_adress(self.test_data.adress)
        # 12. Wpisz miasto
        create_an_account_page.enter_city(self.test_data.city)
        # 13. Wpisz kod pocztowy
        create_an_account_page.enter_postal_code(self.test_data.postcode)
        # 14. Wybierz stan
        create_an_account_page.enter_state(self.test_data.state)
        # 15. Wpisz nr telefonu komórkowego
        create_an_account_page.enter_mobile_phone_number(self.test_data.phone_number)
        # 16. Wpisz alias adresu
        create_an_account_page.enter_address_alias(self.test_data.alias)
        # 17. Kliknij Register
        create_an_account_page.click_register_button()
        # Oczekiwany rezultat:
        # 1. Użytkownik otrzymuje komunikat „firstname is required”
        # create_an_account_page.find_error()
        # print('Wyprintowanie błędów >>', create_an_account_page.get_errors_messages())
        # print('Wyprintowanie ilosci błędów  >>', create_an_account_page.get_numbers_of_errors_visible_text())
        errors = ['firstname is required.']
        errors_messages = create_an_account_page.get_errors_messages()
        # ilosc bledów errors = 1 ("There is 1 error")
        self.verify_errors_messages(errors, errors_messages)
        # Warunki końcowe:
        # 1. Konto nie zostaje założone

        sleep(2)
