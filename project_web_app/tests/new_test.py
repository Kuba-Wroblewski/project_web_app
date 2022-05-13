import unittest
from selenium import webdriver
from pages.home_page import HomePage
from tests.test_data import TestData


class NewTest(unittest.TestCase):
    '''
    base clas for each test
    '''

    def setUp(self):
        # 1. Z otwartą przeglądarką
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()
        # self.driver.maximize_window()

        # 2. Przeglądarka działa w tle (czyli przeglądarka się nie odpali) a testy idą normalnie.
        # options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        # self.driver = webdriver.Chrome(chrome_options=options)

        self.driver.get('http://automationpractice.com/')
        self.driver.implicitly_wait(10)
        self.home_page = HomePage(self.driver)
        self.test_data = TestData()

    def tearDown(self):
        self.driver.quit()
