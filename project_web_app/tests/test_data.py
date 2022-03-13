from faker import Faker

class TestData:
    def __init__(self):
        fake = Faker()
        self.email = fake.email()
        self.default_number = fake.random_digit()
        self.default_word = fake.word()
        self.gender = 'male'
        self.last_name = fake.last_name()
        self.password = fake.password()
        self.birthday = '1985-02-19'
        self.birthday_number = '1900-1-1'
        self.adress = 'Sochaczewsa 13'
        self.city = fake.city()
        self.postcode = '05800'
        self.state = 'Virginia'
        # self.state = 'Warszawa'
        self.phone_number = '608136023'
        self.alias = 'kontakt@wp.pl'
