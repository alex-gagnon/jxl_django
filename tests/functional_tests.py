from selenium import webdriver
import unittest

class JXLUnitTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_browser_title(self):
        """Opening the initial page should display the correct browser title."""
        self.browser.get('http://localhost:8000')

        assert 'Django' in self.browser.title, f"Browser title was {self.browser.title}"

if __name__ == '__main__':
    unittest.main(warnings='ignore')
