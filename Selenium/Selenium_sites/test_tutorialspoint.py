from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


class upload(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox(executable_path=r"Z:\Tester\Selenium\drivers\geckodriver.exe")
  
    def test_upload(self)  :
        driver=self.driver
        # driver.implicity_wait(1)
        driver.maximize_window()
        url="https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm"
        driver.get(url)
        consent= driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[1]/div[2]/div[2]/button[1]/p")
        driver.execute_script("arguments[0].click();", consent)
        time.sleep(2)
        
        picture=driver.find_element_by_xpath("//input[@type='file']")
        driver.execute_script("arguments[0].scrollIntoView(true);",picture)
        picture.send_keys(r"C:\Users\dajmi\Desktop\wolf.jpg")
        time.sleep(2)
        
    def test_click(self):
        driver=self.driver
        driver.maximize_window()
        url="https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm"
        driver.get(url)        
        consent= driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[1]/div[2]/div[2]/button[1]/p")
        driver.execute_script("arguments[0].click();", consent)   
                
        comand=driver.find_element_by_xpath("/html/body/main/div/div/div[2]/div[4]/div/form/table/tbody/tr[10]/td[2]/select/option[4]")
        driver.execute_script("arguments[0].scrollIntoView(true);", comand)
        driver.execute_script("arguments[0].click();", comand)
                
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="dynamicColor"]').click()

        
        name=driver.find_element_by_xpath("/html/body/main/div/div/div[2]/div[4]/div/form/table/tbody/tr[9]/td[2]/select")
        driver.execute_script("arguments[0].click();", name)

        wait = WebDriverWait(driver, 10)
        # wait.until(lambda driver: driver.find_element_by_name("continents")).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/div[2]/div[4]/div/form/table/tbody/tr[9]/td[2]")))
        bb=driver.find_element_by_xpath("/html/body/main/div/div/div[2]/div[4]/div/form/table/tbody/tr[9]/td[2]/select/option[5]")
        driver.execute_script("arguments[0].click();", bb)
    
    def test_userForm(self):
        driver=self.driver
        driver.maximize_window()
        url="https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm"
        driver.get(url)        
        consent= driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[1]/div[2]/div[2]/button[1]/p")
        driver.execute_script("arguments[0].click();", consent)  
        name=driver.find_element_by_xpath("//input[@name='firstname']")
        name.send_keys("Ania")
        lastname=driver.find_element_by_xpath("//input[@name='lastname']")
        lastname.send_keys("Zet")
        sex=driver.find_element_by_xpath("//input[@name='sex'][1]")
        driver.execute_script("arguments[0].click();", sex) 
        sex=driver.find_element_by_xpath("//input[@name='sex'][2]")
        driver.execute_script("arguments[0].click();", sex)
        year=driver.find_element_by_xpath("(//input[@name='exp'])[3]")
        driver.execute_script("arguments[0].click();", year)
        prof=driver.find_element_by_xpath("(//input[@name='profession'])[2]")
        driver.execute_script("arguments[0].click();", prof)
        selenium=driver.find_element_by_xpath("(//input[@name='tool'])[2]")
        driver.execute_script("arguments[0].click();", selenium)
        # driver.find_element_by_xpath('//*[@href="/selenium/selenium_discussion.htm"]').click()
        # driver.find_element_by_link_text("Next Page").click()
        
    def test_alert(self):
        driver=self.driver
        driver.maximize_window()
        url="https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm"
        driver.get(url)
        consent= driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[1]/div[2]/div[2]/button[1]/p")
        driver.execute_script("arguments[0].click();", consent)
        time.sleep(2)
        alert=driver.find_element_by_xpath("//html/body/main/div/div/div[2]/div[4]/div/form/table/tbody/tr[11]/td[2]/button")
        driver.execute_script("arguments[0].click();", alert)
        time.sleep(2)
        try:
            driver.implicitly_wait(3)
            driver.switch_to.alert.dismiss()
            
            print("ODPWIEDZ: alert dismissed")
        except:
            print("no alert")
        
        time.sleep(1)
        driver.execute_script("arguments[0].click();", alert)

        try:
            WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                    'Timed out waiting for PA creation ' +
                                    'confirmation popup to appear.')

            alert = driver.switch_to.alert
            alert.accept()
            print("alert accepted")
        except:
            print("no alert")
        time.sleep(2)
                

        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
