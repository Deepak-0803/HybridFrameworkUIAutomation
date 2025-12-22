from selenium.webdriver.common.by import By

from POM.AccountPage import AccountPage
from POM.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    email_address_field_xpath = "//input[@name='email']"
    password_field_xpath = "//input[@name='password']"
    login_button_xpath = "//input[@value='Login']"
    warning_message_xpath = "//div[@id='account-login']/div[1]"

    def enter_email_address(self,email_address_text):
        self.type_into_element(email_address_text,"email_address_field_xpath", self.email_address_field_xpath)
        # self.driver.find_element(By.ID, self.email_address_field_id).click()
        # self.driver.find_element(By.ID, self.email_address_field_id).clear()
        # self.driver.find_element(By.ID, self.email_address_field_id).send_keys(email_address_text)

    def enter_password(self,password_field_id):
        self.type_into_element(password_field_id,"password_field_xpath", self.password_field_xpath)
        # self.driver.find_element(By.ID, self.password_field_id).click()
        # self.driver.find_element(By.ID, self.password_field_id).clear()
        # self.driver.find_element(By.ID, self.password_field_id).send_keys(password_text)

    def click_on_login_button(self):
        self.click_on_element("login_button_xpath", self.login_button_xpath)
        return AccountPage(self.driver)

    def retrieve_warning_message(self):
        return self.retrieve_element_text("warning_message_xpath",self.warning_message_xpath)
        #return self.driver.find_element(By.XPATH, self.warning_message_xpath).text

    def login_to_application(self, email_address_text, password_text):
        self.enter_email_address(email_address_text)
        self.enter_password(password_text)
        return self.click_on_login_button()
