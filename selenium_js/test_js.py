from selenium_js.base import Base
import time
import pytest

class TestJs(Base):

    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        ele = self.driver.execute_script("return document.getElementById('su')")
        ele.click()
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        time.sleep(3)


    def test_time(self):
        self.driver.get("https://www.12306.cn/index/")
        time_ele = self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-30'")
        time.sleep(3)



