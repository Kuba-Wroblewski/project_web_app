from faker import Faker


class TestData:
    def __init__(self):
        fake = Faker()
        self.email = fake.email()
        self.gender = 'male'
        self.last_name = fake.last_name()
        self.password = fake.password()
        self.birthday = '1985-02-19'
        self.adress = 'Sochaczewsa 13'
        self.city = fake.city()
        self.postcode = '05800'
        self.state = 'Virginia'
        self.phone_number = '608136023'
        self.alias = 'kontakt@wp.pl'
