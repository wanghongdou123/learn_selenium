from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_Wait():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')
        # 隐式等待
        self.driver.implicitly_wait(3)


    def test_wait(self):
        # self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys('霍格沃兹学院')
        self.driver.find_element_by_css_selector('#kw').send_keys('霍格沃兹学院')
        self.driver.find_element_by_id('su').click()


    def teardown(self):
        self.driver.quit()
