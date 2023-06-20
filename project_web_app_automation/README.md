# project_web_app

Project > 
Website automation testing http://automationpractice.com/

## Description:
The aim of the project is to test selected functionalities of the website:
(http://automationpractice.com/)
For this purpose, 23 test cases were developed.
4 product cases, (File> Cart)
7 cases of contact with the service, (file> Contact us)
12 user registrations. (file> Registration test)
This paper uses the Page Object design pattern and data-driven testing.

## Installation:
To run this project, install the appropriate WebDriver for your browser.
I suggest to use Google Chrome in my case was faster.

For Google Chrome install WebDriver from this site: https://chromedriver.chromium.org/downloads

For Firefox install geckodriver from this site: https://github.com/mozilla/geckodriver/releases

We can run tests in e.g. Pycharm or in Visual Studio Code.
When we install the appropriate webdriver to control the browser.
then we install Python and all from file > requirements.txt. 
"start and have fun"

>linux Ubuntu 20.04 LTS
>
> requirements.txt



## Technologies:
> interpreter python 3.8
> 
> Selenium 4.1.0
> 
> pytest 7.0.1
> 
> Faker 13.3.0

### Test scenarios in the folder:
>scenariusze_testowe


Executable file for testing:
### user registration tests:
> project_web_app / tests /
> registration_test.py
### service contact tests:
> project_web_app / tests /
> contact_test.py
### product tests:
> project_web_app / tests /
> cart_test.py


# Test report.
executable file:
> project_web_app / tests /
> run_tests.py

###### creates an html report in the folder of the executable file.
