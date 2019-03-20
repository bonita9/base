import os
import sys
sys.path.append(os.getcwd())

import pytest

from back.page.page_login import PageLogin
from back.tools.get_driver import get_driver

# 获取数据
def get_data():
    return [("11111", "2222"), ("","")]


class TestLogin:

    # setup
    def setup(self):
        # 实例化 获取PageLogin
        self.login = PageLogin(get_driver())

    # teardown
    def teardown(self):
        # 关闭driver
        self.login.driver.quit()

    # 测试方法 login
    @pytest.mark.parametrize("username,pwd", get_data())
    def test_login(self, username, pwd):
        # 调用登录方法
        self.login.page_login(username, pwd)