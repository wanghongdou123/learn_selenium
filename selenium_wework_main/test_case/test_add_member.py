from selenium_wework_main.page.main import Main


class TestAddMember:

    def setup(self):
        self.main = Main()


    def test_add_member(self):
        assert self.main.goto_add_member().add_member()