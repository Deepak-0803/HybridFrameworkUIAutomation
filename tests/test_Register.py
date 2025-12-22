from datetime import datetime
from time import sleep
from POM.HomePage import HomePage
from tests.BaseTest import BassTest
from utilities import EXCELUtils


class TestRegister(BassTest):

    def test_register_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        register_page= home_page.navigate_to_register_page()
        account_success_page = register_page.register_an_account(EXCELUtils.get_cell_data("ExcelFiles/ToturialNinja.xlsx","Sheet2",2,1), ("ExcelFiles/ToturialNinja.xlsx","Sheet2",2,2) , self.generate_email_with_time_stamp(), "1234567890", "12345", "12345", "no", "select" )
        expected_heading_text = "Your Account Has Been Created!"
        assert account_success_page.retrieve_account_creation_message().__eq__(expected_heading_text)


    def test_register_with_all_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_success_page = register_page.register_an_account("Arjun", "Reddy",self.generate_email_with_time_stamp(), "1234567770", "12345", "12345", "yes", "select")
        expected_heading_text = "Your Account Has Been Created!"
        assert account_success_page.retrieve_account_creation_message().__eq__(expected_heading_text)

    def test_register_with_duplicate_email(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account("Arjun", "Reddy", "deepak22080320@gmail.com", "1233567770","12345", "12345", "yes", "select")
        expected_warning_message = "Warning: E-Mail Address is already registered!"
        assert expected_warning_message in register_page.retrieve_duplicate_email_warning_message()

    def test_without_entering_any_fields(self):
        sleep(2)
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account(" ", " "," ", " ", " ", " ",
                                          "yes", "select")
        assert register_page.verify_all_warnings("First Name must be between 1 and 32 characters!","Last Name must be between 1 and 32 characters!", "E-Mail Address does not appear to be valid!", "Telephone must be between 3 and 32 characters!", "Password must be between 4 and 20 characters!" )


