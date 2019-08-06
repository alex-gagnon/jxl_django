"""Make sure dev server is running before attempting to run functional_tests.py"""
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class JXLUnitTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_jxl_page(self):
        """Opening the initial page should display the correct browser title,
        labels should be present"""
        self.browser.get('http://localhost:8000')

        # Is the browser title correct?
        self.assertIn('JXL - Home', self.browser.title)

        # Are labels present?
        version_box = self.browser.find_element_by_id('id_version')

        self.assertTrue(self.browser.find_element_by_id('id_project'))
        self.assertTrue(self.browser.find_element_by_id('id_filter_by'))
        self.assertTrue(version_box)

        # Is Version placeholder text correct?
        self.assertEqual(
            version_box.get_attribute('placeholder'),
            'Enter version number (e.g. 10.2)'
        )

        # A version can be input into version_box
        version_box.send_keys('10.1')

        # When enter key is hit, the page updates
        version_box.send_keys(Keys.ENTER)
        time.sleep(2)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
