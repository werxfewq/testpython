import pytest
from test_appium_po.driver.driver import Driver
from test_appium_po.page.homepage import HomePage


class TestSearch:
    def setup_class(self):
        self.home = HomePage(self.driver)
        self.driver = Driver().get_driver()
    def teardown(self):
        self.driver.quit()
    def test_search_us(self):
        self.home.geto_search().select().get_price()
    def test_search_us_other(self):
        self.home.geto_search().select().getname()
    @pytest.mark.parametrize("search_name,expect",[
        ("alibaba","阿里巴巴"),
        ("xiaomi","小米集团")
    ])
    def test_search(self,search_name,expect):
        text=self.home.geto_search().search(search_name).select().get_name()
        assert expect in text

    def test_add_optional(self):
        text=self.home.geto_search().search("alibaba").add_optional().get_hint()
        assert text in "添加成功"
    def test_sure_optional(self):
        text=self.home.geto_search().search("alibaba").add_optional().get_optional()
        assert text in "已添加"
    def test_delete_optional(self):
        pass