from test_po.contact_page import ContactPage

from test_po.wework_page import WeWork
from time import time
import time



class TestContact:
    def setup(self):
        self.wework=WeWork()
        self.contact = ContactPage(self.wework)
    def teardown(self):
        self.wework.quit()

    def test_add_member(self):
        #contact =ContactPage(self.wework)
        self.contact.add_member("name", "alias","id", "13512345678")
        assert self.contact.get_tips() == "OK"
    def test_add_member_chinese(self):
        #contact =ContactPage(self.wework)
        self.contact.add_member("名字", "别名","id_2", "13512345671")
        assert self.contact.get_tips() == "OK"
    def test_delete_member(self):
        udid=str(time())
        self.contact.add_member("名字"+udid, "别名"+udid,"id_2"+udid, "13512345673")\
            .delete_member()
    def test_update_profile(self):
        self.contact.search_member("赵一").update(name="test %s" % str(time()))
    def test_disable_profile(self):
        self.contact.search_member("赵一").disable("禁用成功")
    def test_enable_profile(self):
        self.contact.search_member("赵一").enable("启用成功")


