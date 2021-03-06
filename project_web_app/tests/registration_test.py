import unittest
from tests.new_test import NewTest
from time import sleep
from tests.test_data import TestData


class RegistrationTest(NewTest):
    maxDiff = None
    """
    registration tests
    """
    # @unittest.skip("skip")
    def verify_errors_messages(self, errors, errors_messages):
        """
        verifies errors displayed for the user
        """
        print("\n", "Oczekiwane błędy >>", errors)
        print("Aktualne błędy >>", errors_messages)
        self.assertEqual(errors, errors_messages)
        # sleep(2)

    # @unittest.skip("skip")
    def test_a_no_email(self):
        """
        TC 001 Do not enter an e-mail in the email field.
        """
        home_page = self.home_page
        # 1. Kliknij „Sign in”
        self.authentication_page = home_page.click_sign_in()
        # 2. Kliknij przycisk „Create account”
        self.authentication_page.click_create_an_account()
        # Oczekiwany rezultat:
        # 1. Użytkownik otrzymuje komunikat "Invalid email address."
        errors = ['Invalid email address.']
        errors_messages = self.authentication_page.get_errors_messages()
        self.verify_errors_messages(errors, errors_messages)
        # Warunki końcowe:
        # 1. Konto nie zostaje założone

    # @unittest.skip("skip")
    def test_b_number_in_the_email_field(self):
        """
        TC 002 Enter a default number in the e-mail field
        """
        home_page = self.home_page
        # 1. Kliknij „Sign in”
        self.authentication_page = home_page.click_sign_in()
        # 2. Wprowadź cyfrę w pole email
        self.authentication_page.create_account_with_email(self.test_data.default_number)
        # 2. Kliknij przycisk „Create account”
        self.authentication_page.click_create_an_account()
        # Oczekiwany rezultat:
        # 1. Użytkownik otrzymuje komunikat "Invalid email address."
        errors = ['Invalid email address.']
        errors_messages = self.authentication_page.get_errors_messages()
        self.verify_errors_messages(errors, errors_messages)
        # Warunki końcowe:
        # 1. Konto nie zostaje założone

    # @unittest.skip("skip")
    def test_c_word_int_the_email_field(self):
        """
        TC 003 Enter a random word in the e-mail field
        """
        home_page = self.home_page
        # 1. Kliknij „Sign in”
        self.authentication_page = home_page.click_sign_in()
        # 2. Wprowadź cyfrę w pole email
        self.authentication_page.create_account_with_email(self.test_data.default_word)
        # 2. Kliknij przycisk „Create account”
        self.authentication_page.click_create_an_account()
        # Oczekiwany rezultat:
        # 1. Użytkownik otrzymuje komunikat "Invalid email address."
        errors = ['Invalid email address.']
        errors_messages = self.authentication_page.get_errors_messages()
        self.verify_errors_messages(errors, errors_messages)
        # Warunki końcowe:
        # 1. Konto nie zostaje założone

    # @unittest.skip("skip")
    def test_d_word_plus_special_sign_to_email_field(self):
        """
        TC 004 Enter a random word + @ in the e-mail field
        """
        home_page = self.home_page
        # 1. Kliknij „Sign in”
        self.authentication_page = home_page.click_sign_in()
        # 2. Wprowadź cyfrę w pole email
        self.authentication_page.create_account_with_email(self.test_data.default_word+"@")
        # 2. Kliknij przycisk „Create account”
        self.authentication_page.click_create_an_account()
        # Oczekiwany rezultat:
        # 1. Użytkownik otrzymuje komunikat "Invalid email address."
        errors = ['Invalid email address.']
        errors_messages = self.authentication_page.get_errors_messages()
        self.verify_errors_messages(errors, errors_messages)
        # Warunki końcowe:
        # 1. Konto nie zostaje założone

    # @unittest.skip("skip")
    def test_e_word_plus_special_sign_plus_world_to_email_field(self):
        """
        TC 005 Enter a random word + @ + random world in the email field
        """
        fake_word = self.test_data.default_word
        fake_word2 = self.test_data.default_word2
        home_page = self.home_page
        # 1. Kliknij „Sign in”
        self.authentication_page = home_page.click_sign_in()
        # 2. Wprowadź cyfrę w pole email
        self.authentication_page.create_account_with_email(fake_word+"@"+fake_word2)
        # 2. Kliknij przycisk „Create account”
        self.authentication_page.click_create_an_account()
        # Oczekiwany rezultat:
        # 1. Użytkownik otrzymuje komunikat "Invalid email address."
        errors = ['Invalid email address.']
        errors_messages = self.authentication_page.get_errors_messages()
        self.verify_errors_messages(errors, errors_messages)
        # Warunki końcowe:
        # 1. Konto nie zostaje założone

    # @unittest.skip("skip")
    def test_f_world_plus_special_sign_plus_number_and_number_to_email_field(self):
        """
        TC 006 Enter a random number + @ + default number plus "." plus number in the email field
        """
        fake_digit = str(self.test_data.default_number)
        fake_word = self.test_data.default_word
        home_page = self.home_page
        # 1. Kliknij „Sign in”
        self.authentication_page = home_page.click_sign_in()
        # 2. Wprowadź cyfrę w pole email
        self.authentication_page.create_account_with_email(fake_word+"@"+fake_digit+"."+fake_digit)
        # 2. Kliknij przycisk „Create account”
        self.authentication_page.click_create_an_account()
        # Oczekiwany rezultat:
        # 1. Użytkownik otrzymuje komunikat "Invalid email address."
        errors = ['Invalid email address.']
        errors_messages = self.authentication_page.get_errors_messages()
        self.verify_errors_messages(errors, errors_messages)
        # Warunki końcowe:
        # 1. Konto nie zostaje założone

    # @unittest.skip("skip")
    def test_g_default_word_plus_world_plus_special_sign_to_email(self):
        """
        TC 007 Enter a default word plus @ plus default world + "." plus special sign in the email field
        """
        fake_word = self.test_data.default_word
        home_page = self.home_page
        # 1. Kliknij „Sign in”
        self.authentication_page = home_page.click_sign_in()
        # 2. Wprowadź cyfrę w pole email
        self.authentication_page.create_account_with_email(fake_word + "@" + fake_word+"."+"/")
        # 2. Kliknij przycisk „Create account”
        self.authentication_page.click_create_an_account()
        # Oczekiwany rezultat:
        # 1. Użytkownik otrzymuje komunikat "Invalid email address."
        errors = ['Invalid email address.']
        errors_messages = self.authentication_page.get_errors_messages()
        self.verify_errors_messages(errors, errors_messages)
        # Warunki końcowe:
        # 1. Konto nie zostaje założone

    # @unittest.skip("skip")
    def test_h_nothing_type_in_create_account(self):
        """
        TC 008 Nothing type at CREATE AN ACCOUNT just click REGISTER
        """
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

    # @unittest.skip("skip")
    def test_i_default_number_in_password_field(self):
        """
        TC 009 Enter default number in password field
        """
        home_page = self.home_page
        # 1. kliknij sign in
        authentication_page = home_page.click_sign_in()
        # 2. wpisz e-mail
        # 3. kliknij przycisk create account
        create_an_account_page = authentication_page.create_account_with_email(self.test_data.email)
        # 4. wybierz płeć
        create_an_account_page.choose_gender(self.test_data.gender)
        # 5. Wpisz nazwisko
        create_an_account_page.enter_name(self.test_data.name)
        # 6. Wpisz nazwisko
        create_an_account_page.enter_lastname(self.test_data.last_name)
        # 7. Sprawdź poprawność e-maila
        self.assertEqual(self.test_data.email, create_an_account_page.get_email(), 'mail different from previously!')
        # 8. Wpisz hasło
        create_an_account_page.enter_password(self.test_data.default_number)
        # aby zobaczyć czy coś wpisał
        sleep(3)
        # 9. wpisz datę urodzenia
        create_an_account_page.choose_birthday(self.test_data.birthday)
        # 10. Sprawdź pole „First name”
        create_an_account_page.get_first_name()
        self.assertEqual(create_an_account_page.get_first_name(), self.test_data.name)
        # 11. Sprawdź pole „Last name”
        create_an_account_page.get_last_name()
        self.assertEqual(create_an_account_page.get_last_name(), self.test_data.last_name)
        # 12. Wpisz adres
        create_an_account_page.enter_adress(self.test_data.address)
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
        # 1. Użytkownik otrzymuje komunikat "passwd is invalid."
        errors = ['passwd is invalid.']
        errors_messages = create_an_account_page.get_errors_messages()
        self.verify_errors_messages(errors, errors_messages)
        # Warunki końcowe:
        # 1. Konto nie zostaje założone

    # @unittest.skip("skip")
    def test_j_date_birthday(self):
        """
        TC 010 Enter 29 february in 1900 of birthday
        """
        home_page = self.home_page
        # 1. kliknij sign in
        authentication_page = home_page.click_sign_in()
        # 2. wpisz e-mail
        # 3. kliknij przycisk create account
        create_an_account_page = authentication_page.create_account_with_email(self.test_data.email)
        # 4. wybierz płeć
        create_an_account_page.choose_gender(self.test_data.gender)
        # 5. Wpisz imie
        # anulowanie wpisywania imienia, ponieważ może mi założyć konto z przyjęcia błędnej daty
        # create_an_account_page.enter_name(self.test_data.name)
        # 6. Wpisz nazwisko
        create_an_account_page.enter_lastname(self.test_data.last_name)
        # 7. Sprawdź poprawność emaila
        self.assertEqual(self.test_data.email, create_an_account_page.get_email(), 'mail different from previously!')
        # 8. Wpisz hasło
        create_an_account_page.enter_password(self.test_data.password)
        # 9. Wpisz datę urodzenia
        # szukamy dni przestępnych
        # błąd na stronie -można wybrać w każdym roku do 31 lutego
        create_an_account_page.choose_birthday(self.test_data.birthday_test)
        sleep(10)
        # 10. Sprawdź pole „First name”
        create_an_account_page.get_first_name()
        self.assertEqual(create_an_account_page.get_first_name(), '')
        # 11. Sprawdź pole „Last name”
        create_an_account_page.get_last_name()
        self.assertEqual(create_an_account_page.get_last_name(), self.test_data.last_name)
        # 12. Wpisz adres
        create_an_account_page.enter_adress(self.test_data.address)
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

    # @unittest.skip("skip")
    def test_k_number_in_firstname_and_lastname_field(self):
        """
        TC 011 enter default number in first name and last name field
        """
        fake_digit = str(self.test_data.default_number)
        fake_digit_2 = str(self.test_data.default_number_2)
        home_page = self.home_page
        # 1. kliknij sign in
        authentication_page = home_page.click_sign_in()
        # 2. wpisz e-mail
        # 3. kliknij przycisk create account
        create_an_account_page = authentication_page.create_account_with_email(self.test_data.email)
        # 4. wybierz płeć
        create_an_account_page.choose_gender(self.test_data.gender)
        # 5. Wpisz imie
        create_an_account_page.enter_name(fake_digit)
        # 6. Wpisz nazwisko
        create_an_account_page.enter_lastname(fake_digit_2)
        # 7. Sprawdź poprawność e-maila
        self.assertEqual(self.test_data.email, create_an_account_page.get_email(), 'mail different from previously!')
        # 8. Wpisz hasło
        sleep(5)
        create_an_account_page.enter_password(self.test_data.password)
        # 9. wpisz datę urodzenia
        create_an_account_page.choose_birthday(self.test_data.birthday)
        # 10. Sprawdź pole „First name”
        create_an_account_page.get_first_name()
        self.assertEqual(create_an_account_page.get_first_name(), fake_digit)
        # 11. Sprawdź pole „Last name”
        create_an_account_page.get_last_name()
        self.assertEqual(create_an_account_page.get_last_name(), fake_digit_2)
        # 12. Wpisz adres
        create_an_account_page.enter_adress(self.test_data.address)
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

    # @unittest.skip("skip")
    def test_l_default_word_plus_number_in_firstname_lastname_field(self):
        """
        TC 012 enter default word + default number in field first name and last name
        """
        default_number = str(self.test_data.default_number)
        default_world = self.test_data.default_word
        home_page = self.home_page
        # 1. kliknij sign in
        authentication_page = home_page.click_sign_in()
        # 2. wpisz e-mail
        # 3. kliknij przycisk create account
        create_an_account_page = authentication_page.create_account_with_email(self.test_data.email)
        # 4. wybierz płeć
        create_an_account_page.choose_gender(self.test_data.gender)
        # 5. Wpisz imie
        create_an_account_page.enter_name(default_number+default_world)
        # 6. Wpisz nazwisko
        create_an_account_page.enter_lastname(default_world+default_number)
        # 7. Sprawdź poprawność emaila
        self.assertEqual(self.test_data.email, create_an_account_page.get_email(), 'mail different from previously!')
        # 8. Wpisz hasło
        create_an_account_page.enter_password(self.test_data.password)
        # 9. wpisz datę urodzenia
        create_an_account_page.choose_birthday(self.test_data.birthday)
        # 10. Sprawdź pole „First name”
        create_an_account_page.get_first_name()
        self.assertEqual(create_an_account_page.get_first_name(), default_number+default_world)
        # 11. Sprawdź pole „Last name”
        create_an_account_page.get_last_name()
        self.assertEqual(create_an_account_page.get_last_name(), default_world+default_number)
        # 12. Wpisz adres
        create_an_account_page.enter_adress(self.test_data.address)
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
