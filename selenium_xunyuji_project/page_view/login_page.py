import logging
from base_view.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    url = '/member/common/login.html'
    # 定位器
    username_loc = (By.ID, 'sUserName')
    password_loc = (By.ID, 'sPassword')
    submit_loc = (By.CLASS_NAME, 'lijsubm')
    content = (By.CLASS_NAME, 'layui-layer-content')
    loginpass_loc = (By.LINK_TEXT, '退出')
    loginfail_loc = (By.LINK_TEXT, '注册')

    def type_username(self, username):
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)

    def click_login_submit_btn(self):
        self.find_element(*self.submit_loc).click()

    def login_action(self, username, password):
        self.open()
        self.type_username(username)
        self.type_password(password)
        self.click_login_submit_btn()

    def login_status(self):
        return self.find_element(*self.content).text

    def type_loginpass(self):
        return self.find_element(*self.loginpass_loc).text

    def type_loginfail(self):
        return self.find_element(*self.loginfail_loc).text

    def check_login_btn_exist(self):
        try:
            self.find_element(*self.submit_loc)
            logging.info('存在登录按钮')
            return True
        except:
            logging.error('不存在登录按钮')
            self.get_screenshot('login_page', '不存在登录按钮')
            return False
