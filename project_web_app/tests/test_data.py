import random
from faker import Faker
import os


class TestData:
    def __init__(self):
        fake = Faker()
        self.email = fake.email()
        self.login_email = 'testowe@wp.pl'
        self.login_password = 'password1'
        self.default_number = fake.random_digit()
        self.default_word = fake.word()
        self.gender = 'male'
        self.last_name = fake.last_name()
        self.password = fake.password()
        self.name = fake.name()
        self.birthday = '1985-02-19'
        self.birthday_test = '1900-2-29'
        self.address = 'Lipowa 18'
        self.city = fake.city()
        self.postcode = '05800'
        self.state = 'Virginia'
        self.phone_number = '608136023'
        self.alias = 'kontakt@wp.pl'
        self.choose = random.randint(1, 2)
        self.message = fake.paragraph()
        self.image = 'https://source.unsplash.com/random/300x200'
        self.image_put2 = 'random.jpg'
        image = os.path.abspath(self.image_put2)
        image_abs = image.replace('tests', 'graphics')
        self.image_put = image_abs
        self.quantity = '0'
        self.price_shipping = '$2.00'
        # vat 4% = 1.04
        self.tax = 1.04
