import os
import unittest
import sys

from Utils.utils import Utility

sys.path.append(".")
from selenium import webdriver


class BaseTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        utility = Utility()
        browser = utility.get_browser()
        self.driver = self.startBrowser(browser)
        self.driver.maximize_window()

    @classmethod
    def tearDown(self):
        try:
            self.driver.close()
            self.driver.quit()
        except:
            pass

    def startBrowser(name):
        """
        browsers, firefox, chrome, ie, phantomjs
        """
        try:
            if name.lower() == 'firefox' or name.lower() == 'ff':
                return webdriver.Firefox()
            elif name.lower() == 'chrome':
                return webdriver.Chrome()
            elif name.lower() == 'phantomjs':
                return webdriver.phantomjs()
            else:
                return webdriver.Firefox()
        except Exception as msg:
            print('massage: %s' % str(msg))

