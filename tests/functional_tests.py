"""Make sure dev server is running before attempting to run functional_tests.py"""

import unittest
import time

from selenium import webdriver


class JXLUnitTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_browser_title(self):
        """Opening the initial page should display the correct browser title."""
        self.browser.get('http://localhost:8000')
        time.sleep(2)

        assert 'Hello' in self.browser.title, f"Browser title was {self.browser.title}"


if __name__ == '__main__':
    unittest.main(warnings='ignore')
