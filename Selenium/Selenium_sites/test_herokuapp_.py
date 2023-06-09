import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

class Test_herokuapp(unittest.TestCase):    
     def setUp(self):
         self.driver = webdriver.Firefox(executable_path=r"Z:\Tester\Selenium\drivers\geckodriver.exe")
    
     def test_download(self):
         driver=self.driver
         url='http://the-internet.herokuapp.com/download'
         driver.get(url)
         d1=driver.find_element_by_xpath('/html/body/div[2]/div/div/a[1]')
         d1.click()
        
        
     def test_screenShot(self):
         driver=self.driver
         url='http://the-internet.herokuapp.com/download'
         driver.get(url)
         driver.get_screenshot_as_file("screenshot.png")
        
if __name__== "__main__":
    unittest.main() 