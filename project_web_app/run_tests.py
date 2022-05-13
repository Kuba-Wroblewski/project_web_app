import unittest
from tests.registration_test import RegistrationTest
from tests.contact_test import ContactUs
from tests.cart_test import ProductTest


# pobierz testy, które chcesz uruchomić
test_a_registration = unittest.TestLoader().loadTestsFromTestCase(RegistrationTest)
test_b_contact = unittest.TestLoader().loadTestsFromTestCase(ContactUs)
test_c_product = unittest.TestLoader().loadTestsFromTestCase(ProductTest)


# Lista testów do uruchomienia
test_for_run = [
    test_a_registration,
    test_b_contact,
    test_c_product

    # kolejny test
    # ...
                ]

# Stwórz test Suitę łączący testy
test_suite = unittest.TestSuite(test_for_run)

# Odpal testy
# unittest.TextTestRunner().run(test_suite)
