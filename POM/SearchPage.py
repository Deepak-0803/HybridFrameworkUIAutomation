from time import sleep

from selenium.webdriver.common.by import By

from POM.BasePage import BasePage


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    valid_Hp_product_link_text= "HP LP3065"
    no_product_message_xpath = "//input[@value='Search']/following-sibling::p"


    def display_status_of_valid_product(self):
        return self.check_display_status_element("valid_Hp_product_link_text",self.valid_Hp_product_link_text)
        #return self.driver.find_element(By.LINK_TEXT, self.valid_Hp_product_link_text).is_displayed()


    def retrieve_no_product_message(self):
        sleep(5)
        self.retrieve_element_text("no_product_message_xpath",self.no_product_message_xpath)
        #return self.driver.find_element(By.XPATH, self.no_product_message_xpath).text
