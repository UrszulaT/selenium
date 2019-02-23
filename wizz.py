# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
import time

class WizzairRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window
        self.driver.get("http://wizzair.com/pl-pl#/")

    def tearDown(self):
        self.driver.quit()
        pass
#I Rejestracja nowego użytkownika używając adresu email - dane niepoprawne (niekompletny email)

    def test_wrong_email(self):
        pass



    # def test_search(self):
    #     driver = self.driver
    #     driver.get("http://www.google.pl")
    #     input = driver.find_element_by_name("q")
    #     input.send_keys("Chorzów")
    #     time.sleep(3)
    #     pass

if __name__ == '__main__':
    unittest.main()
