from selenium import webdriver


class Test_Wait():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # 隐式等待
        self.driver.implicitly_wait(3)



    def test_wait(self):
        self.driver.get('https://testerhome.com/account/sign_in')
        self.driver.find_element_by_id('user_login').send_keys('whd3322@163.com')
        self.driver.find_element_by_id('user_password').send_keys('Whd940102.')
        self.driver.find_element_by_name('commit').click()


    def teardown(self):
        self.driver.quit()
