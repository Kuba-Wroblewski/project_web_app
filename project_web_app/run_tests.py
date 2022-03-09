import unittest
from tests.registration_test import RegistrationTest

# pobierz testy które chcesz uruchomić
registratiion_test = unittest.TestLoader().loadTestsFromTestCase(RegistrationTest)

# Lista testów do uruchomienia
test_for_run = [
    registratiion_test,
    # kolejny test
    # ...
                ]

# Stwórz test Suitę łączący testy
test_suite = unittest.TestSuite(test_for_run)

# Odpal testy
# unittest.TextTestRunner().run(test_suite)

