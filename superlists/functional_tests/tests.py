from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVistor(LiveServerTestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self,row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retive_it(self):
        #Elliechecks out new app home page
        self.browser.get(self.live_server_url)

        #she notices it is a "to-do" list
        self.assertIn('To-Do',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # she is invited to enter a item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )

        #she types in "buy stuff" into a text box
        inputbox.send_keys('Buy stuff')

        #she hits enter and the page lists "1:buy stuff" 
        inputbox.send_keys(Keys.ENTER)
        #time.sleep(10)
        #she enters "use stuff" in text box 
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use stuff')
        inputbox.send_keys(Keys.ENTER)
       
        self.check_for_row_in_list_table('1: Buy stuff')
        self.check_for_row_in_list_table('2: Use stuff')
        #she wonders if site will save list, she sees a unique url 
        #with explination text

        #she enters the url directly and sees list
        self.fail('Finish the test')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
