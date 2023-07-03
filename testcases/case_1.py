import pytest

from pages.launch_page import LaunchPage
from testcases import conftest


@pytest.mark.usefixtures("setup")
class TestingSkype():
    def test_case1(self):
        lp = LaunchPage(self.driver)
        lp.allow()
        lp.create()
        lp.enter_email("json7753@gmail.com")
        lp.otp()
        lp.email()
        lp.enter_opt()