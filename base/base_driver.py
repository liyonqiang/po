import time
from appium import webdriver


class BaseDriver:
    driver = None
    # 获取driver 驱动对象
    @classmethod
    def base_get_driver(cls):
            if cls.driver is None:

                # server 启动参数
                desired_caps = {}
                # 设备信息
                desired_caps['platformName'] = 'Android'
                desired_caps['platformVersion'] = '7.1.2'
                desired_caps['deviceName'] = '127.0.0.1:62001'
                # app的信息
                desired_caps['appPackage'] = 'com.xiaomi.shop'
                desired_caps['appActivity'] = 'com.xiaomi.shop2.activity.MainActivity'
                # 解决输入中文
                desired_caps['unicodeKeyboard'] = True
                desired_caps['resetKeyboard'] = True

                desired_caps['automationName'] = 'Uiautomator2'

                # 不重置应用
                desired_caps["noReset"] = True

                # desired_caps['fullReset'] = False

            # 声明我们的driver对象
            return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    # 关闭driver驱动对象并置空
    @classmethod
    def base_quit_driver(cls):
        if cls.driver:
            time.sleep(3)
            cls.driver.quit()
            cls.driver = None

