import os.path

from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities import randomeString
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_AccountReg:
    baseURL = ReadConfig.getApplicationUrl()
    logger = LogGen.loggen()
    def test_account_reg(self, setup):
        self.logger.info("test_account_reg")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.hp = HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickRegister()
        self.logger.info("Provide customer credentials")
        self.regpage = AccountRegistrationPage(self.driver)
        self.regpage.setFirstName("John")
        self.regpage.setLastName("Canedy")
        self.email = randomeString.random_string_generator() + '@gmail.com'  # Виправлено відступ
        self.regpage.setEmail(self.email)
        self.regpage.setTelephone("65656565")
        self.regpage.setPassword("abcxyz")
        self.regpage.setConfirmPassword("abcxyz")
        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        self.confmsg = self.regpage.getconfirmationmsg()
        if self.confmsg == "Your Account Has Been Created!":
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\" + "test_account_reg.png")
            assert False
        self.logger.info("test_account_reg finished")