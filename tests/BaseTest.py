from datetime import datetime

import pytest


@pytest.mark.usefixtures("setup_and_teardown", "log_on_failure")
class BassTest:
    def generate_email_with_time_stamp(self):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        email = f"test_{timestamp}@gmail.com"
        return "arjun"+email

