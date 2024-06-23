from selenium import webdriver
from time import sleep

class  TestHogwards():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def test_mycase(self):


        self.driver.get("https://testerhome.com/")
        self.driver.find_element_by_link_text("社区").click()
        self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a').click()

    def teardown(self):
        self.driver.quit()


