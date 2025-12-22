from telnetlib import EC
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver= driver


    def type_into_element(self, text,locator_name,  locator_value):
        element = self.get_element(locator_name, locator_value)
        element.click()
        element.clear()
        element.send_keys(text)

    def click_on_element(self, locator_name,  locator_value):
        element = self.get_element(locator_name,  locator_value)

        element.click()

    def retrieve_element_text(self, locator_name,  locator_value):
        element = self.get_element(locator_name,  locator_value)
        return  element.text

    def check_display_status_element(self, locator_name,  locator_value):
        element = self.get_element(locator_name,  locator_value)
        return element.is_displayed()

    # def get_element(self, locator_name,  locator_value):
    #     wait = WebDriverWait(self.driver, 10)
    #     element = None
    #
    #     if locator_name.__contains__("_xpath"):
    #         element = self.driver.find_element(By.XPATH, locator_value)
    #
    #     elif locator_name.__contains__("_name"):
    #         element = self.driver.find_element(By.NAME, locator_value)
    #
    #     elif locator_name.__contains__("_class_name"):
    #         element = self.driver.find_element(By.CLASS_NAME, locator_value)
    #
    #     elif locator_name.__contains__("_link_text"):
    #         element = self.driver.find_element(By.LINK_TEXT, locator_value)
    #
    #     elif locator_name.__contains__("_id"):
    #         element = self.driver.find_element(By.ID, locator_value)
    #
    #     elif locator_name.__contains__("_css"):
    #         element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
    #
    #     return element

    def get_element(self, locator_name, locator_value):
        wait = WebDriverWait(self.driver, 10)

        if "_xpath" in locator_name:
            return wait.until(EC.presence_of_element_located((By.XPATH, locator_value)))

        elif "_id" in locator_name:
            return wait.until(EC.presence_of_element_located((By.ID, locator_value)))

        elif "_name" in locator_name:
            return wait.until(EC.presence_of_element_located((By.NAME, locator_value)))

        elif "_class_name" in locator_name:
            return wait.until(EC.presence_of_element_located((By.CLASS_NAME, locator_value)))

        elif "_link_text" in locator_name:
            return wait.until(EC.presence_of_element_located((By.LINK_TEXT, locator_value)))

        elif "_css" in locator_name:
            return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_value)))

        else:
            raise ValueError(f"Unknown locator type: {locator_name}")
