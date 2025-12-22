from time import sleep

from selenium.webdriver.common.by import By

from POM.BasePage import BasePage


class AccountSuccessPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)



    account_creation_message_xpath = "//div[@id='content']/h1"

    def retrieve_account_creation_message(self):
        sleep(2)
        return self.retrieve_element_text("account_creation_message_xpath",self.account_creation_message_xpath)
