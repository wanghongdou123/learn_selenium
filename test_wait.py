import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_Wait():
    def setup(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        browser = os.getenv("browser")

        self.driver = webdriver.Chrome(options=options)
        self.driver.get('https://home.testing-studio.com/')
        # 隐式等待
        self.driver.implicitly_wait(3)



    def test_wait(self):
        # sleep(3)    强制等待
        self.driver.find_element_by_xpath('//*[@title="按类别分组的所有话题"]').click()
        # def wait(x):
        #     return len(self.driver.find_elements(By.XPATH,'//*[@id="categories-only-category"]')) >= 1

        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,
                                            '//*[@title="原创精华文章,有100元奖金"]')))

        self.driver.find_element_by_xpath('//*[@title="原创精华文章,有100元奖金"]').click()


    def teardown(self):
        self.driver.quit()
