from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_Wait():
    def setup(self):
        self.driver = webdriver.Chrome()
        # 隐式等待
        self.driver.implicitly_wait(3)


    @pytest.mark.skip
    def test_wait(self):
        self.driver.get('https://www.baidu.com/')
        element_input = self.driver.find_element_by_css_selector('#kw')
        element_click = self.driver.find_element_by_id('su')

        action = ActionChains(self.driver)
        action.click(element_input).send_keys('霍格沃兹学院')
        action.click(element_click)
        action.perform()

    @pytest.mark.skip
    # 鼠标移动到某个元素
    def test_moveto(self):
        self.driver.get('https://www.baidu.com/')
        ele = self.driver.find_element_by_id('s-usersetting-top')
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        sleep(3)
        action.perform()

    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        drag_element = self.driver.find_element_by_id('dragger')
        # div的父元素body的第5个子元素
        drop_element = self.driver.find_element_by_css_selector('body > div:nth-child(5)')
        action = ActionChains(self.driver)
        # action.drag_and_drop(drag_element,drop_element)   拖拽1
        # action.click_and_hold(drag_element).release(drop_element)    拖拽2
        # 拖拽3
        action.click_and_hold(drag_element).move_to_element(drop_element).release()
        sleep(3)
        action.perform()


    # 模拟键盘按键
    def test_sendkey(self):
        self.driver.get('http://sahitest.com/demo/label.htm')
        ele = self.driver.find_element_by_xpath('/html/body/label[1]/input')
        action = ActionChains(self.driver)
        action.click(ele).send_keys('username').pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).pause(1)
        action.perform()


    def teardown(self):
        self.driver.quit()

if __name__ == '__main__':
    pytest.main(['-v','-s','test_ActionChains.py'])