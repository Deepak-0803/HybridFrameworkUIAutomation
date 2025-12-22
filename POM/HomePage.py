from time import sleep

from selenium.webdriver.common.by import By

from POM.BasePage import BasePage
from POM.LoginPage import LoginPage
from POM.RegisterPage import RegisterPage
from POM.SearchPage import SearchPage


class HomePage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    search_box_field_xpath = "//input[@name='search']"
    search_button_xpath = "//button[contains(@class,'btn-default')]"
    my_account_drop_menu_xpath = "//span[text()='My Account']"
    login_option_link_text = "Login"
    register_option_link_text = "Register"

    def navigate_to_register_page(self):
        self.click_in_my_account_drop_menu_xpath()
        return self.select_register_option()

    def enter_product_into_search_box_field(self, product_name):
        self.type_into_element(product_name,"search_box_field_xpath", self.search_box_field_xpath)
        # self.driver.find_element(By.XPATH, self.search_box_field_xpath).click()
        # self.driver.find_element(By.XPATH, self.search_box_field_xpath).clear()
        # self.driver.find_element(By.XPATH,self.search_box_field_xpath).send_keys(product_name)

    def click_on_search_button(self):
        self.click_on_element("search_button_xpath", self.search_button_xpath)
        #self.driver.find_element(By.XPATH, self.search_button_xpath).click()
        return SearchPage(self.driver)

    def click_in_my_account_drop_menu_xpath(self):
        self.click_on_element("my_account_drop_menu_xpath",self.my_account_drop_menu_xpath)
        # self.driver.find_element(By.XPATH, self.my_account_drop_menu_xpath).click()

    def select_login_option(self):
        self.click_on_element("login_option_link_text",self.login_option_link_text)
        # self.driver.find_element(By.LINK_TEXT,self.login_option_link).click()
        return LoginPage(self.driver)

    def select_register_option(self):
        self.click_on_element("register_option_link_text",self.register_option_link_text)
        #self.driver.find_element(By.LINK_TEXT, self.register_option_link_text).click()
        return RegisterPage(self.driver)

    def search_for_a_product(self, product_name):
        self.enter_product_into_search_box_field(product_name)
        sleep(2)
        return self.click_on_search_button()


    def navigate_to_login_page(self):
        self.click_in_my_account_drop_menu_xpath()
        return self.select_login_option()

