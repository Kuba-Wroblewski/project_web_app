import unittest
from tests.new_test import NewTest
from time import sleep
from tests.test_data import TestData


class RegistrationTest(NewTest):
    maxDiff = None
    '''
    registration tests
    '''
    # @unittest.skip("skip")
    def verify_errors_messages(self, errors, errors_messages):
        '''
        verifies errors displayed for the user
        verify all errors
        '''
        print("\n", errors)
        print(errors_messages)
        self.assertCountEqual(errors, errors_messages)
        sleep(2)

    @unittest.skip("skip")
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

    @unittest.skip("skip")
    def test_number_in_the_email_field(self):
        '''
        TC 002 typed a number in the email field
        '''
        home_page = self.home_page
        # 1. Kliknij „Sign in”
        self.authentication_page = home_page.click_sign_in()
        # 2. Wprowadż cyfre w pole email
        self.authentication_page.create_account_with_email(self.test_data.default_number)
        # 2. Kliknij przycisk „Create account”
        self.authentication_page.click_create_an_account()
        # Oczekiwany rezultat:
        # 1. Użytkownik otrzymuje komunikat „Invalid email address.”
        errors = ['Invalid email address.']
        errors_messages = self.authentication_page.get_errors_messages()
        self.verify_errors_messages(errors, errors_messages)
        # Warunki końcowe:
        # 1. Konto nie zostaje założone

    @unittest.skip("skip")
    def test_default_word_to_email(self):
        '''
        TC 003 typed a random word in the email field
        '''
        home_page = self.home_page
        # 1. Kliknij „Sign in”
        self.authentication_page = home_page.click_sign_in()
        # 2. Wprowadż cyfre w pole email
        self.authentication_page.create_account_with_email(self.test_data.default_word)
        # 2. Kliknij przycisk „Create account”
        self.authentication_page.click_create_an_account()
        # Oczekiwany rezultat:
        # 1. Użytkownik otrzymuje komunikat „Invalid email address.”
        errors = ['Invalid email address.']
        errors_messages = self.authentication_page.get_errors_messages()
        self.verify_errors_messages(errors, errors_messages)
        # Warunki końcowe:
        # 1. Konto nie zostaje założone

    @unittest.skip("skip")
    def test_default_word_plus_word_to_email(self):
        '''
        TC 004 typed a random word + @ in the email field
        '''
        home_page = self.home_page
        # 1. Kliknij „Sign in”
        self.authentication_page = home_page.click_sign_in()
        # 2. Wprowadż cyfre w pole email
        self.authentication_page.create_account_with_email(self.test_data.default_word+"@")
        # 2. Kliknij przycisk „Create account”
        self.authentication_page.click_create_an_account()
        # Oczekiwany rezultat:
        # 1. Użytkownik otrzymuje komunikat „Invalid email address.”
        errors = ['Invalid email address.']
        errors_messages = self.authentication_page.get_errors_messages()
        self.verify_errors_messages(errors, errors_messages)
        # Warunki końcowe:
        # 1. Konto nie zostaje założone

    @unittest.skip("skip")
    def test_default_word_plus_default_world_to_email(self):
        '''
        TC 005 typed a random word + @ + default world in the email field
        '''
        fake_word = self.test_data.default_word
        home_page = self.home_page
        # 1. Kliknij „Sign in”
        self.authentication_page = home_page.click_sign_in()
        # 2. Wprowadż cyfre w pole email
        self.authentication_page.create_account_with_email(fake_word+"@"+fake_word)
        # 2. Kliknij przycisk „Create account”
        self.authentication_page.click_create_an_account()
        # Oczekiwany rezultat:
        # 1. Użytkownik otrzymuje komunikat „Invalid email address.”
        errors = ['Invalid email address.']
        errors_messages = self.authentication_page.get_errors_messages()
        self.verify_errors_messages(errors, errors_messages)
        # Warunki końcowe:
        # 1. Konto nie zostaje założone

    @unittest.skip("skip")
    def test_default_number_plus_number_to_email(self):
        '''
        TC 006 typed a random number + @ + default number plus "." plus number in the email field
        '''
        fake_digit = str(self.test_data.default_number)
        home_page = self.home_page
        # 1. Kliknij „Sign in”
        self.authentication_page = home_page.click_sign_in()
        # 2. Wprowadż cyfre w pole email
        self.authentication_page.create_account_with_email(fake_digit+"@"+fake_digit+"."+fake_digit)
        # 2. Kliknij przycisk „Create account”
        self.authentication_page.click_create_an_account()
        # Oczekiwany rezultat:
        # 1. Użytkownik otrzymuje komunikat „Invalid email address.”
        errors = ['Invalid email address.']
        errors_messages = self.authentication_page.get_errors_messages()
        self.verify_errors_messages(errors, errors_messages)
        # Warunki końcowe:
        # 1. Konto nie zostaje założone

    @unittest.skip("skip")
    def test_default_word_plus_world_plus_special_sign_to_email(self):
        '''
        TC 007 typed a default word plus @ plus default world + "." plus special sign in the email field
        '''
        fake_word = self.test_data.default_word
        home_page = self.home_page
        # 1. Kliknij „Sign in”
        self.authentication_page = home_page.click_sign_in()
        # 2. Wprowadż cyfre w pole email
        self.authentication_page.create_account_with_email(fake_word + "@" + fake_word+"."+"/")
        # 2. Kliknij przycisk „Create account”
        self.authentication_page.click_create_an_account()
        # Oczekiwany rezultat:
        # 1. Użytkownik otrzymuje komunikat „Invalid email address.”
        errors = ['Invalid email address.']
        errors_messages = self.authentication_page.get_errors_messages()
        self.verify_errors_messages(errors, errors_messages)
        # Warunki końcowe:
        # 1. Konto nie zostaje założone

    @unittest.skip("skip")
    def test_nothing_type_in_create_account(self):
        '''
        TC 008 nothing type at CREATE AN ACCOUNT just click REGISTER
        '''
        home_page = self.home_page
        # 1. kliknij sign in
        authentication_page = home_page.click_sign_in()
        # 2. wpisz e-mail
        # 3. kliknij przycisk create account
        create_an_account_page = authentication_page.create_account_with_email(self.test_data.email)
        # 4. Kliknij Register
        create_an_account_page.click_register_button()
        # Oczekiwany rezultat:
        # 1. Użytkownik otrzymuje komunikat:
        # "You must register at least one phone number.
        # lastname is required.
        # firstname is required.
        # passwd is required.
        # address1 is required.
        # city is required.
        # The Zip/Postal code you've entered is invalid. It must follow this format: 00000
        # This country requires you to choose a State."
        errors = ['You must register at least one phone number.', 'lastname is required.', 'firstname is required.',
                  'passwd is required.', 'address1 is required.', 'city is required.',
                  "The Zip/Postal code you've entered is invalid. It must follow this format: 00000",
                  'This country requires you to choose a State.']
        errors_messages = create_an_account_page.get_errors_messages()
        self.verify_errors_messages(errors, errors_messages)
        # Warunki końcowe:
        # 1. Konto nie zostaje założone

    @unittest.skip("skip")
    def test_default_number_in_password_field(self):
        '''
        TC 009 enter default number in password field
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
        create_an_account_page.enter_name(self.test_data.name)
        # 6. Wpisz nazwisko
        create_an_account_page.enter_lastname(self.test_data.last_name)
        # 7. Sprawdz poprawnosc emaila
        self.assertEqual(self.test_data.email, create_an_account_page.get_email(), 'mail different from previously!')
        # 8. Wpisz hasło
        create_an_account_page.enter_password(self.test_data.default_number)
        # 9. wpisz datę urodzenia
        create_an_account_page.choose_birthday(self.test_data.birthday)
        # 10. Sprawdź pole „First name”
        create_an_account_page.get_first_name()
        self.assertEqual(create_an_account_page.get_first_name(), self.test_data.name)
        # 11. Sprawdź pole „Last name”
        create_an_account_page.get_last_name()
        self.assertEqual(create_an_account_page.get_last_name(), self.test_data.last_name)
        # 12. Wpisz adres
        create_an_account_page.enter_adress(self.test_data.adress)
        # 13. Wpisz miasto
        create_an_account_page.enter_city(self.test_data.city)
        # 14. Wpisz kod pocztowy
        create_an_account_page.enter_postal_code(self.test_data.postcode)
        # 15. Wybierz stan
        create_an_account_page.enter_state(self.test_data.state)
        # 16. Wpisz nr telefonu komórkowego
        create_an_account_page.enter_mobile_phone_number(self.test_data.phone_number)
        # 17. Wpisz alias adresu
        create_an_account_page.enter_address_alias(self.test_data.alias)
        # 18. Kliknij Register
        create_an_account_page.click_register_button()
        # Oczekiwany rezultat:
        # 1. Użytkownik otrzymuje komunikat „passwd is invalid.”
        errors = ['passwd is invalid.']
        errors_messages = create_an_account_page.get_errors_messages()
        self.verify_errors_messages(errors, errors_messages)
        # Warunki końcowe:
        # 1. Konto nie zostaje założone

    @unittest.skip("skip")
    def test_date_birthday(self):
        '''
        TC 010 enter 29 february in 1900 of birthday
        '''
        home_page = self.home_page
        # 1. kliknij sign in
        authentication_page = home_page.click_sign_in()
        # 2. wpisz e-mail
        # 3. kliknij przycisk create account
        create_an_account_page = authentication_page.create_account_with_email(self.test_data.email)
        # 4. wybierrz płeć
        create_an_account_page.choose_gender(self.test_data.gender)
        # 5. Wpisz imie
        # anulowanie wpisywania imienia, ponieważ może mi założyć konto z przyjęcia błędnej daty
        # create_an_account_page.enter_name(self.test_data.name)
        # 6. Wpisz nazwisko
        create_an_account_page.enter_lastname(self.test_data.last_name)
        # 7. Sprawdz poprawnosc emaila
        self.assertEqual(self.test_data.email, create_an_account_page.get_email(), 'mail different from previously!')
        # 8. Wpisz hasło
        create_an_account_page.enter_password(self.test_data.password)
        # 9. wpisz datę urodzenia
        # szukamy dni przestepnych
        # błąd na stronie -można wybrać w każdym roku do 31 lutego
        create_an_account_page.choose_birthday(self.test_data.birthday_test)
        # 10. Sprawdź pole „First name”
        create_an_account_page.get_first_name()
        self.assertEqual(create_an_account_page.get_first_name(), '')
        # 11. Sprawdź pole „Last name”
        create_an_account_page.get_last_name()
        self.assertEqual(create_an_account_page.get_last_name(), self.test_data.last_name)
        # 12. Wpisz adres
        create_an_account_page.enter_adress(self.test_data.adress)
        # 13. Wpisz miasto
        create_an_account_page.enter_city(self.test_data.city)
        # 14. Wpisz kod pocztowy
        create_an_account_page.enter_postal_code(self.test_data.postcode)
        # 15. Wybierz stan
        create_an_account_page.enter_state(self.test_data.state)
        # 16. Wpisz nr telefonu komórkowego
        create_an_account_page.enter_mobile_phone_number(self.test_data.phone_number)
        # 17. Wpisz alias adresu
        create_an_account_page.enter_address_alias(self.test_data.alias)
        # 18. Kliknij Register
        create_an_account_page.click_register_button()
        # Oczekiwany rezultat:
        # 1. Użytkownik otrzymuje komunikat „'firstname is required.', 'Invalid date of birth'”
        errors = ['firstname is required.', 'Invalid date of birth']
        errors_messages = create_an_account_page.get_errors_messages()
        self.verify_errors_messages(errors, errors_messages)
        # Warunki końcowe:
        # 1. Konto nie zostaje założone
        # 2. błąd na stronie -można wybrać w każdym roku do 31 lutego

    @unittest.skip("skip")
    def test_number_in_firstname_lastname_field(self):
        '''
        TC 011 enter default number in field first name and last name
        '''
        home_page = self.home_page
        # 1. kliknij sign in
        authentication_page = home_page.click_sign_in()
        # 2. wpisz e-mail
        # 3. kliknij przycisk create account
        create_an_account_page = authentication_page.create_account_with_email(self.test_data.email)
        # 4. wybierrz płeć
        create_an_account_page.choose_gender(self.test_data.gender)
        # 5. Wpisz imie
        create_an_account_page.enter_name(self.test_data.default_number)
        # 6. Wpisz nazwisko
        create_an_account_page.enter_lastname(self.test_data.default_number)
        # 7. Sprawdz poprawnosc emaila
        self.assertEqual(self.test_data.email, create_an_account_page.get_email(), 'mail different from previously!')
        # 8. Wpisz hasło
        create_an_account_page.enter_password(self.test_data.password)
        # 9. wpisz datę urodzenia
        create_an_account_page.choose_birthday(self.test_data.birthday)
        # 10. Sprawdź pole „First name”
        create_an_account_page.get_first_name()
        self.assertEqual(create_an_account_page.get_first_name(), str(self.test_data.default_number))
        # 11. Sprawdź pole „Last name”
        create_an_account_page.get_last_name()
        self.assertEqual(create_an_account_page.get_last_name(), str(self.test_data.default_number))
        # 12. Wpisz adres
        create_an_account_page.enter_adress(self.test_data.adress)
        # 13. Wpisz miasto
        create_an_account_page.enter_city(self.test_data.city)
        # 14. Wpisz kod pocztowy
        create_an_account_page.enter_postal_code(self.test_data.postcode)
        # 15. Wybierz stan
        create_an_account_page.enter_state(self.test_data.state)
        # 16. Wpisz nr telefonu komórkowego
        create_an_account_page.enter_mobile_phone_number(self.test_data.phone_number)
        # 17. Wpisz alias adresu
        create_an_account_page.enter_address_alias(self.test_data.alias)
        # 18. Kliknij Register
        create_an_account_page.click_register_button()
        # Oczekiwany rezultat:
        # 1. Użytkownik otrzymuje komunikat „'lastname is invalid.', 'firstname is invalid.'”
        errors = ['lastname is invalid.', 'firstname is invalid.']
        errors_messages = create_an_account_page.get_errors_messages()
        self.verify_errors_messages(errors, errors_messages)
        # Warunki końcowe:
        # 1. Konto nie zostaje założone

    @unittest.skip("skip")
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
        self.assertEqual(self.test_data.email, create_an_account_page.get_email(), 'mail different from previously!')
        # 7. Wpisz hasło
        create_an_account_page.enter_password(self.test_data.password)
        # 8. wpisz datę urodzenia
        create_an_account_page.choose_birthday(self.test_data.birthday)
        # 9. Sprawdź pole „First name”
        create_an_account_page.get_first_name()
        self.assertEqual(create_an_account_page.get_first_name(), '')
        # 10. Sprawdź pole „Last name”
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
        self.verify_errors_messages(errors, errors_messages)
        # Warunki końcowe:
        # 1. Konto nie zostaje założone
