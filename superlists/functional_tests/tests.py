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
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy stuff')

        #time.sleep(10)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use stuff')
        inputbox.send_keys(Keys.ENTER)
       
        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table('1: Buy stuff')
        self.check_for_row_in_list_table('2: Use stuff')
        
        # new user Francis comes along

        #use a new browser session to make sure there is no residual info
        self.browser.quit()
        self.browser = webdriver.Firefox()

        #Francis visits the home page. There is no sign of Edith
        self.brower.get(self.live_server_url)
        page_text = self.browser.find_element_by_taag_name('body').text
        self.assertNotIn('Buy stuff',page_text)
        self.assertNotIn('Use stuff', page_text)

        #Fransis starts a new list 
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        #new url
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        #check for Edith's list
        page_text = self.browser.find_element_by_tag_name('bod').text
        self.assertNotIn('Buy Stuff', page_text)
        self.assertIn('Buy milk', page_text)
        
        self.fail('Finish the test')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
