from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from selenium_learn.page.BasePage import BasePage


class AddMember(BasePage):

    def add_member(self):
        self.find(By.ID, 'username').send_keys('aname2')
        self.find(By.ID, 'memberAdd_acctid').send_keys('123456799')
        self.find(By.ID, 'memberAdd_phone').send_keys('17700000003')
        # 保存
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()


    def updata_page(self):
        content: str = self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text').text
        # 1/10
        return [int(x) for x in content.split('/',1)]


    def get_member(self, value):
        # 单选框出现检查
        self.wait_for_click((By.CSS_SELECTOR, '.ww_checkbox'))
        cur_page,total_page = self.updata_page()

        while True:
            # 获取名字username
            elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            for element in elements:
                if value == element.get_attribute('title'):
                    return True
            cur_page = self.updata_page()[0]
            if cur_page == total_page:
                return False
            # 点击下一页
            self.find(By.CSS_SELECTOR, '.js_next_page').click()