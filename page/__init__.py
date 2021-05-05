from selenium.webdriver.common.by import By

"以下是page_login的配置信息"
# 'x'按钮
# close_button = By.CLASS_NAME, "android.widget.ImageView"

# '我的' 按钮
mine_button = By.XPATH, "//*[@text='我的']"

# 登录注册按钮
login_sign_up_button = By.ID, "com.xiaomi.shop.plugin.homepage:id/mine_root_avatar"

# 用账号密码登录
# username_password_login = By.ID, "com.xiaomi.shop:id/entry_to_password_login"

# 密码登录
use_password_login = By.XPATH, "//*[@text='密码登录']"

# 账号输入框
username_input_text_view = By.ID, "com.xiaomi.shop:id/userId"

# 密码输入框
password_input_text_view = By.ID, "com.xiaomi.shop:id/password"

# 登录按钮
login_click_button = By.ID, "com.xiaomi.shop:id/sign_in_btn"

# 同意条款按钮
accept_button = By.ID, "com.xiaomi.shop:id/footer_user_agreement_checkbox"

# 判断登录成功的/ 我的米圈
mine_xiao_mi = By.ID, "com.xiaomi.shop.plugin.homepage:id/binder_mi_circle_title"

# 设置按钮
setting_button = By.ID, "com.xiaomi.shop.plugin.homepage:id/mine_root_icon_setting"

# 退出账号
sign_out_button = By.ID, "com.xiaomi.shop2.plugin.setting:id/common_button_middletext"

# 确定 退出 按钮
quit_button = By.XPATH, "//*[@text='退出']"

# 错误提示框
error_info = By.ID, "com.xiaomi.shop:id/textinput_error"
