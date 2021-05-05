import time

import yaml
from selenium.webdriver.support.wait import WebDriverWait

from base.base_driver import BaseDriver


class BaseAction:
    def __init__(self):
        # 获取手机驱动对象
        self.driver = BaseDriver.base_get_driver()

    # 公用的找元素方法
    def base_find_element(self, loc, timeout=10.0, poll=0.5, swipe=False):
        if swipe is True:
            while True:
                try:
                    return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(loc[0], loc[1]))
                except:
                    # 手机屏幕宽
                    mobile_width = self.driver.get_window_size()["width"]

                    # 手机屏幕高
                    mobile_height = self.driver.get_window_size()["height"]

                    # 滑动前页面所有的元素
                    before_page_source = self.driver.page_source

                    # 滑动半屏
                    self.driver.swipe(mobile_width * 1 / 4, mobile_height * 3 / 4, mobile_width * 1 / 4,
                                      mobile_height * 1 / 4, 5000)

                    # 滑动后页面所有的元素
                    after_page_source = self.driver.page_source

                    # 判断滑动前后页面所有的元素是否相同
                    if before_page_source == after_page_source:
                        print("滑动到底部仍没有找到该元素: {}".format(loc))

                        # 终止查找循环
                        break
        else:
            try:
                return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(loc[0], loc[1]))
            except:
                return False

    # 公用的点击方法
    def base_click(self, loc, timeout=10.0, poll=0.5, swipe=False):
        self.base_find_element(loc, timeout=timeout, poll=poll, swipe=swipe).click()

    # 输入方法
    def base_input(self, loc, text):
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(text)

    # 获取元素文本的方法
    def base_get_ele_text(self, loc):
        return self.base_find_element(loc).text

    # 获取元素属性
    def base_get_attribute(self, loc, attribute):
        return self.base_find_element(loc).get_attribute(attribute)

    # 截图方法
    def base_screen_shot(self, picture_name):
        print("截图了!!!")
        self.driver.get_screenshot_as_file("./image/" + picture_name + "{}.PNG".format(time.strftime("%Y_%m_%d %H_%M_%S")))

    # 判断元素是否存在
    def base_if_ele_exists(self, loc, swipe=False, timeout=10):
        if self.base_find_element(loc, swipe=swipe, timeout=timeout):
            return True
        else:
            return False
