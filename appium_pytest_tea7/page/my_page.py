import logging
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.login_page import LoginPage
from page.setting_page import SettingPage
from page.shopping_car_page import ShoppingCarPage


class MyPage(BasePage):
    reglog_btn_loc = (By.ID, 'com.tea7.app:id/tv_login')
    setting_loc = (By.ID, 'com.tea7.app:id/rl_setting')
    nickname_loc = (By.ID, 'com.tea7.app:id/tv_nickname')
    shopping_car_loc = (By.ID, 'com.tea7.app:id/ll_cart')

    def go_to_login_page(self):
        logging.info('点击登录/注册按钮')
        self.find_element(*self.reglog_btn_loc).click()
        return LoginPage(self.driver)

    def go_to_setting_page(self):
        self.swipe_down()
        logging.info('点击设置按钮')
        self.find_element(*self.setting_loc).click()
        return SettingPage(self.driver)

    def go_to_shopping_car_page(self):
        logging.info('点击购物车按钮')
        self.find_element(*self.shopping_car_loc).click()
        return ShoppingCarPage(self.driver)

    def check_login_status(self):
        # logging.info('检查是否存在昵称')
        nick_name_btn = self.is_element_exsist(*self.nickname_loc)
        return nick_name_btn
