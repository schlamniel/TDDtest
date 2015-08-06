from selenium import webdriver
import unittest

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
        self.fail('Finish the test')

        # she is invited to enter a item

        #she types in "buy stuff" into a text box

        #she hits enter and the page lists "1:buy stuff" 

        #she enters "use stuff" in text box 

        # page updates to show both items

        #she wonders if site will save list, she sees a unique url 
        #with explination text

        #she enters the url directly and sees list

if __name__ == '__main__':
    unittest.main(warnings='ignore')
