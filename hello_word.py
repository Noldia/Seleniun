import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = cls.driver
        driver.implicitly_wait(10)

    def test_hello_world(self):
        driver=self.driver
        driver.get('https://www.platzi.com')

    def test_visit_my_page(self):
        self.driver.get('https://noldia.github.io')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reports', report_name='Hello_world_report'))


"""
-----------Estructura general-----------
import unittest
from selenium import webdriver

class HomePageTests(unittes.TestCase):
    
    def setUp(self):
        pass

    def TearDown(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity = 2)
"""
