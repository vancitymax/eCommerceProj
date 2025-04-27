from selenium.webdriver.common.by import By


class LoginPage:
    txt_email = "/input[@name='email']"
    txt_password = "/input[@name='password']"
    login_btn = "//button[@type='submit']"
    msg_myaccount_xpath = "/textarea[@name='myaccount']"

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element_by_xpath(self.txt_email).send_keys(email)
    def set_password(self, password):
        self.driver.find_element_by_xpath(self.txt_password).send_keys(password)
    def login(self):
        self.driver.find_element_by_xpath(self.login_btn).click()

    def isMyAccountPageExists(self):
        return self.driver.find_element_by_xpath(self.msg_myaccount_xpath).is_displayed()