from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium_learn.page.BasePage import BasePage
from selenium_learn.page.add_member import AddMember

class Main(BasePage):

    _base_url = 'https://work.weixin.qq.com/wework_admin/frame'

    def goto_add_member(self):
        self.find(By.ID, 'menu_contacts').click()

        # 显示等待，判断元素是否出现，未出现则一直点击
        def wait_add_member(x):
            elements_len = len(self.finds(By.CSS_SELECTOR, '#username'))
            if elements_len <= 0:
                self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
            return elements_len > 0

        self.wait_for_element(wait_add_member)
        return AddMember(self._driver)