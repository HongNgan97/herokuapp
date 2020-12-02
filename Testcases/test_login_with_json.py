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

    def test_login(self):
        data = Data()
        accounts = data.get_account_json()

        for acc in accounts:
            username = acc['username']
            password = acc['password']
            message = acc['message']
            account = Account(username, password)

            login_page = LoginPage(self.driver)
            login_page.login_object(account)

            result_page = ResultPage(self.driver)
            self.assertIn(message, result_page.get_message())


if __name__ == "__main__":
    unittest.main()
