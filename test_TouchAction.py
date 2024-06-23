from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_Wait():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        # 隐式等待
        self.driver.implicitly_wait(3)



    def test_touchaction(self):
        self.driver.get('https://www.baidu.com/')

        ele1 = self.driver.find_element_by_css_selector('#kw')
        ele1.send_keys('霍格沃兹学院')

        ele2 = self.driver.find_element_by_id('su')

        touch_action = TouchActions(self.driver)
        touch_action.tap(ele2).perform()
        touch_action.scroll_from_element(ele1,0,10000).perform()
        sleep(5)



    def teardown(self):
        self.driver.quit()
