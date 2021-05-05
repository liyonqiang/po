import page
from base.base_action import BaseAction


class PageLogin(BaseAction):
    # 点击前置取消
    # def page_close_button(self):
    #     self.base_click(page.close_button, swipe=False)

    # 点击我的
    def page_click_mine_button(self):
        self.base_click(page.mine_button)

    # 点击登录/注册
    def page_click_login_sigh_up(self):
        self.base_click(page.login_sign_up_button)

    # 点击 用账号密码登录
    def page_click_password_login(self):
        self.base_click(page.use_password_login)

    # 输入用户账号
    def page_username_input_text_view(self, username):
        self.base_input(page.username_input_text_view, username)

    # 输入密码
    def page_password_input_text_view(self, password):
        self.base_input(page.password_input_text_view, password)

    # 点击同意条款  (判断同意条款按钮， 没有选中则点击, 已选中则不点)
    def page_click_accept_button(self):

        checked = self.base_get_attribute(page.accept_button, 'checked')
        # 如果按钮是勾选状态
        if checked == "true":
            return

        # 如果按钮不是勾选状态
        elif checked == "false":
            # 勾选
            self.base_click(page.accept_button)

    # 点击登录
    def page_click_login_click_button(self):
        self.base_click(page.login_click_button)

    # 判断是否登录成功
    def page_if_login_success(self):
        if self.base_if_ele_exists(page.mine_xiao_mi, timeout=5):
            return True
        else:
            return False

    # 判断是否退出成功
    def page_if_login_sign_out(self):
        if self.base_if_ele_exists(page.login_sign_up_button):
            return True
        else:
            return False

    # 设置点击
    def page_click_setting(self):
        self.base_click(page.setting_button)

    # 退出账号点击
    def page_click_sign_out(self):
        self.base_click(page.sign_out_button, swipe=True, timeout=5, poll=0.5)

    def page_click_quit_button(self):
        self.base_click(page.quit_button)

    # 截图
    def page_screen_shot(self):
        self.base_screen_shot("login_False_")

    # 获取错误提示框信息
    def get_error_info(self):
        return self.base_get_ele_text(page.error_info)

    # 组合登录业务功能
    def page_login(self):
        # 点击前置取消
        # self.page_close_button()

        # 点击我的
        self.page_click_mine_button()

        # 点击登录/注册
        self.page_click_login_sigh_up()

        # 点击用账号密码登录
        self.page_click_password_login()

        # # 输入用户账号
        # self.page_username_input_text_view(username)
        #
        # # 输入密码
        # self.page_password_input_text_view(password)
        #
        # # 点击同意条款
        # self.page_click_accept_button()
        #
        # # 点击登录
        # self.page_click_login_click_button()

    # 组合退出登录功能
    def page_sign_out(self):
        self.page_click_setting()
        self.page_click_sign_out()
        self.page_click_quit_button()
        self.page_click_mine_button()