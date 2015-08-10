from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVistor(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retive_it(self):
        #Elliechecks out new app home page
        self.browser.get('http://localhost:8000')

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

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        #self.assertTrue(
            #any(row.text == '1: Buy stuff'  for row in rows),
            #"New to-do item did not appear in table -- it was:\n%s" %(
            #    table.text,
            #)    
        #)
        self.assertIn('1: Buy stuff', [row.text for row in rows])
        
        #she enters "use stuff" in text box 
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use stuff')
        inputbox.send_keys(Keys.ENTER)

        # page updates to show both items
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(
            '2: Use stuff', [row.text for row in rows]
        )
        
        #she wonders if site will save list, she sees a unique url 
        #with explination text

        #she enters the url directly and sees list
        self.fail('Finish the test')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
