from .base import FunctionalTest
from unittest import skip
from selenium.webdriver.common.keys import Keys
import time

class ItemValidationTest(FunctionalTest):
    @skip
    def test_cannot_add_empty_list_items(self):
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys(' ')
        self.get_item_input_box().send_keys(Keys.ENTER)
        time.sleep(2)
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text,"You can't have an empty list item")

        self.get_item_input_box().send_keys('Buy milk')
        self.get_item_input_box().send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1:Buy milk')

        self.get_item_input_box().send_keys(' ')
        self.get_item_input_box().send_keys(Keys.ENTER)
        time.sleep(5)
        self.check_for_row_in_list_table('1:Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        self.get_item_input_box().send_keys('Make tea')
        self.get_item_input_box().send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1:Buy milk')
        self.check_for_row_in_list_table('2:Make tea')


        #self.fail('Write Me!')

    @skip
    def test_cannot_add_duplicate_item(self):
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy wellies')
        self.get_item_input_box().send_keys(Keys.ENTER)
        time.sleep(2)
        self.check_for_row_in_list_table('1:Buy wellies')

        self.get_item_input_box().send_keys('Buy wellies')
        self.get_item_input_box().send_keys(Keys.ENTER)
        time.sleep(2)
        self.check_for_row_in_list_table('1:Buy wellies')
        error=self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text,"You've already got this in your list")

    def get_error_element(self):
        time.sleep(2)
        return self.browser.find_element_by_css_selector('.has-error')

    def test_error_messages_are_cleared_on_input(self):
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys(' ')
        self.get_item_input_box().send_keys(Keys.ENTER)
        error=self.get_error_element()
        self.assertTrue(error.is_displayed())

        self.get_item_input_box().send_keys('a')
        error=self.get_error_element()
        self.assertFalse(error.is_displayed())

