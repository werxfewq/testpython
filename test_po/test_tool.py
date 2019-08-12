
from test_po.tool_page import ToolPage
from test_po.wework_page import WeWork
from time import time
import time

class TestTool:
    def setup(self):
        self.wework=WeWork()
        self.tool = ToolPage(self.wework)
    def teardown(self):
        self.wework.quit()
    def test_upload_picture(self):
        self.tool.upload_picturce("D:\HS.JPG")
