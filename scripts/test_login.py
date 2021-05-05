import os, sys
import time
sys.path.append(os.getcwd())

from base.base_driver import BaseDriver
from page.page_login import PageLogin
import pytest
from base.base_yml import base_yml_with_file


def data_with_key(key):
    return base_yml_with_file("data_yml_login", key)


class TestLogin:
    def setup_class(self):
        # 使用page页面创建对象
        self.page_login = PageLogin()

        # 先去判断xiaomi商城是否处于登录状态
        # 点击我的
        self.page_login.page_click_mine_button()
        try:
            # 断言是登录状态
            assert self.page_login.page_if_login_success()
            # 调用退出登录
            self.page_login.page_sign_out()

        except:
            pass

        # 调用登录方法
        self.page_login.page_login()

    # 关闭驱动对象
    def teardown_class(self):
        BaseDriver().base_quit_driver()

    # 登录
    @pytest.mark.parametrize("args", data_with_key("test_login"))
    def test_login(self, args):
        username = args["username"]
        password = args["password"]
        result = args["result"]

        # 输入用户账号
        self.page_login.page_username_input_text_view(username)

        # 输入密码
        self.page_login.page_password_input_text_view(password)

        # 点击同意条款
        self.page_login.page_click_accept_button()

        # 点击登录
        self.page_login.page_click_login_click_button()

        time.sleep(2)

        # 如果用户名密码正确
        if result == "true":

            # 判断是否登录成功
            try:
                assert self.page_login.page_if_login_success()

                # 调用退出登录方法
                self.page_login.page_sign_out()

                # 判断是否退出成功
                try:
                    # 断言退出成功
                    assert self.page_login.page_if_login_sign_out()
                    # 调用登录方法
                    self.page_login.page_login()
                except AssertionError:
                    # 如果没有退出成功,截图
                    self.page_login.page_screen_shot()
                    raise
            except AssertionError:
                # 截图
                self.page_login.page_screen_shot()
                raise

        else:
            # 预期错误提示框信息
            error_info_expected = args["error_info"]

            # 获取错误提示框信息
            error_info_actual = self.page_login.get_error_info()
            try:
                assert error_info_expected == error_info_actual

            except AssertionError:
                # 截图
                self.page_login.page_screen_shot()
                raise
