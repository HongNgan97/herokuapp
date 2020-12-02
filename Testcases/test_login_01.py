import sys

from Objects.account import Account
from Pages.result_page import ResultPage

sys.path.append(".")

import unittest
from Pages.login_page import LoginPage
from Testcases.base_test import BaseTest
from Testdata.test_data import Data


class HerokuAppLogin1(BaseTest):

    @classmethod
    def setUp(self):
        super().setUp()

    @classmethod
    def tearDown(self):
        super().tearDown()

    def test_login_successfully(self):
        login_page = LoginPage(self.driver)

        account = Account(Data.USERNAME, Data.PASSWORD)

        login_page.login_object(account)

        # login_page.login_object(Data.USERNAME, Data.PASSWORD)
        # login_page.login(Data.USERNAME, Data.PASSWORD)
        result_page = ResultPage(self.driver)

        print(result_page.get_message())
        self.assertIn("You logged into a secure area!", result_page.get_message())


if __name__ == "__main__":
    unittest.main()
