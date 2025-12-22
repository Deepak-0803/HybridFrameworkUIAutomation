
from time import sleep, time

import pytest

from POM.HomePage import HomePage
from tests.BaseTest import BassTest
from utilities import EXCELUtils


class TestLogin(BassTest):

    @pytest.mark.parametrize(
        "email_address,password",
        EXCELUtils.get_data_from_excel(
            "ExcelFiles/ToturialNinja.xlsx",
            "Sheet1"
        )
    )

    def test_login_with_valid_credentials(self, email_address, password):
        home_page= HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application(email_address, password)
        #login_to_application("deepak22080320@gmail.com", "Deepak@08" )
        account_page = login_page.click_on_login_button()
        assert account_page.display_status_of_edit_your_account_information_option()




    def test_login_with_invalid_email_and_valid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application(self.generate_email_with_time_stamp(), "Deepak@08")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)


    def test_login_with_invalid_email_and_invalid_password(self):
        home_page= HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application("deepak22080320@gmail.com" , "Deepakdnaf08")
        sleep(2)
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        sleep(2)
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)


    def test_login_without_entering_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application(" ", " ")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        sleep(3)
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)




