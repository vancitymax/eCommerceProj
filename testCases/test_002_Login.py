import os.path
import pytest
from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities import randomeString
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage

class Test_Login():
    baseUrl = ReadConfig.getApplicationUrl()
    logger = LogGen.loggen()

    user = ReadConfig.getUseremail()
    password = ReadConfig.getUserPassword()

    @pytest.mark.sanity
    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickLogin()

        self.lp = LoginPage(self.driver)
        self.lp.set_email(self.user)
        self.lp.set_password(self.password)
        self.lp.login()

        self.targetpage = self.lp.isMyAccountPageExists()
        if self.targetpage:
            assert True
        else:
            self.driver.save_screenshot('screen.png')
            assert False
        

