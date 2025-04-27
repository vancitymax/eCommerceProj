from pageObjects.HomePage import HomePage


class MyAccountPage():

    log_out_xpath = '//*[@id="logout"]'

    def __init__(self, driver):
        self.driver = driver

    def click_logout(self):
        self.driver.get(self.log_out_xpath)
        