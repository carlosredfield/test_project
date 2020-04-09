import logging
from selenium.webdriver.common.by import By
from page.base_page import BasePage


class SettingPage(BasePage):
    logout_loc = (By.ID, 'com.tea7.app:id/tv_exit')

    def Logout(self):
        logging.info('点击退出账号')
        self.find_element(*self.logout_loc).click()
        logging.info('退出成功')
