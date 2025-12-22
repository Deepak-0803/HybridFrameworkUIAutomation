from time import sleep

from selenium.webdriver.common.by import By

from POM.AccountSuccessPage import AccountSuccessPage
from POM.BasePage import BasePage


class RegisterPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)


    first_name_field_xpath = "//input[@ID='input-firstname']"
    last_name_field_xpath = "//input[@ID='input-lastname']"
    email_field_xpath = "//input[@ID='input-email']"
    telephone_field_xpath = "//input[@ID='input-telephone']"
    password_field_xpath = "//input[@ID='input-password']"
    password_confirm_xpath = "//input[@ID='input-confirm']"
    check_box_xpath = "//input[@type='checkbox']"
    continue_box_xpath = "//input[@type='submit' and @value='Continue']"
    yes_radio_xpath = "//input[@name='newsletter'][@value='1']"
    duplicate_email_warning_message_xpath = "//div[contains(@class,'alert-danger')]"
    privacy_policy_warning_message_xpath = "//div[@id='account-register']/div[1]"
    first_name_warning_message_xpath = "//input[@name='firstname']/following-sibling::div"
    last_name_warning_message_xpath = "//input[@name='lastname']/following-sibling::div"
    email_warning_message_xpath = "//input[@name='email']/following-sibling::div"
    telephone_warning_message_xpath = "//input[@name='telephone']/following-sibling::div"
    password_warning_message_xpath = "//input[@name='password']/following-sibling::div"


    def register_an_account(self, first_name, last_name, email_text, telephone, password_text, password_conf, yes_or_no, privacy_policy):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email_text)
        self.enter_telephone(telephone)
        self.enter_password(password_text)
        self.enter_password_confirm(password_conf)
        if yes_or_no.__eq__("yes"):
            self.select_yes_radio_button()
        if privacy_policy.__eq__("select"):
            self.select_agree_check_field()

        return self.click_on_continue_button()




    def retrieve_duplicate_email_warning_message(self):
        return self.retrieve_element_text("duplicate_email_warning_message_xpath",self.duplicate_email_warning_message_xpath)


    def retrieve_privacy_policy_warning_message(self):
        return self.retrieve_element_text("privacy_policy_warning_message_xpath",self.privacy_policy_warning_message_xpath)


    def retrieve_first_name_warning_message(self):
        return self.retrieve_element_text("first_name_warning_message_xpath",self.first_name_warning_message_xpath)


    def retrieve_last_name_warning_message(self):
        return self.retrieve_element_text("last_name_warning_message_xpath",self.last_name_warning_message_xpath)


    def retrieve_email_warning_message(self):
        return self.retrieve_element_text("email_warning_message_xpath",self.email_warning_message_xpath)

    def retrieve_telephone_warning_message(self):
        return self.retrieve_element_text("telephone_warning_message_xpath",self.telephone_warning_message_xpath)

    def retrieve_password_warning_message(self):
        return self.retrieve_element_text("password_warning_message_xpath",self.password_warning_message_xpath)

    def retrieve_duplicate_email_warning(self):
        return self.retrieve_element_text("duplicate_email_warning_message_xpath",self.duplicate_email_warning_message_xpath)

    def select_yes_radio_button(self):
        self.click_on_element("yes_radio_xpath",self.yes_radio_xpath)
        #self.driver.find_element(By.XPATH, self.yes_radio_xpath).click()

    def enter_first_name(self, first_name):
        self.type_into_element(first_name,"first_name_field_xpath", self.first_name_field_xpath)

    def enter_last_name(self, last_name):
        self.type_into_element(last_name,"last_name_field_xpath", self.last_name_field_xpath)

    def enter_email(self, email):
        self.type_into_element(email,"email_field_xpath", self.email_field_xpath)

    def enter_telephone(self, telephone):
        self.type_into_element(telephone, "telephone_field_xpath",self.telephone_field_xpath)

    def enter_password(self, password):
        self.type_into_element(password,"password_field_xpath", self.password_field_xpath)

    def enter_password_confirm(self, password):
        self.type_into_element(password, "password_field_xpath", self.password_field_xpath)

    def select_agree_check_field(self):
        self.click_on_element("check_box_xpath",self.check_box_xpath)


    def click_on_continue_button(self):
        self.click_on_element("continue_box_xpath",self.continue_box_xpath)
        #self.driver.find_element(By.XPATH, self.continue_box_xpath).click()
        return AccountSuccessPage(self.driver)

    def verify_all_warnings(self, expected_first_name_warning_message, expected_last_name_warning_message, expected_email_warning_message, expected_telephone_warning_message, expected_password_warning_message):
        actual_first_name_warning_message = self.retrieve_first_name_warning_message()
        actual_last_name_warning_message = self.retrieve_last_name_warning_message()
        actual_email_warning_message = self.retrieve_email_warning_message()
        actual_telephone_warning_message = self.retrieve_telephone_warning_message()
        actual_password_warning_message = self.retrieve_password_warning_message()

        status = False
        if expected_first_name_warning_message.__eq__(actual_first_name_warning_message):
            if expected_last_name_warning_message.__eq__(actual_last_name_warning_message):
                if expected_email_warning_message.__eq__(actual_email_warning_message):
                    if expected_telephone_warning_message.__eq__(actual_telephone_warning_message):
                        if expected_password_warning_message.__eq__(actual_password_warning_message):
                            status = True
        return status

