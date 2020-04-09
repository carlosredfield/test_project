from page.base_page import BasePage
from selenium.webdriver.common.by import By
import logging


class LoginPage(BasePage):
    pwd_login_loc = (By.XPATH, '//android.widget.TextView[@text="密码登录"]')
    phone_num_loc = (By.ID, 'com.tea7.app:id/ed_phone')
    password_loc = (By.ID, 'com.tea7.app:id/ed_pwd')
    login_btn_loc = (By.ID, 'com.tea7.app:id/bt_login')
    toast = (By.XPATH, "//*[@class='android.widget.Toast']")

    # 输入手机号
    def input_phonenum(self, username):
        logging.info('输入手机号')
        self.find_element(*self.phone_num_loc).clear()
        self.find_element(*self.phone_num_loc).send_keys(username)

    # 输入密码
    def input_password(self, password):
        logging.info('输入密码')
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    # 点击登录
    def loginbtn_click(self):
        logging.info('点击登录')
        self.find_element(*self.login_btn_loc).click()

    # 从验证码登录转为密码登录
    def to_pwd_login(self):
        logging.info('点击密码登录')
        self.find_element(*self.pwd_login_loc).click()

    # 执行登录操作
    def login_action(self, username, password):
        self.to_pwd_login()
        self.input_phonenum(username)
        self.input_password(password)
        self.loginbtn_click()

    def get_toast_text(self):
        toast_text = self.toast_text()
        return toast_text


    def check_login_status(self):
        logging.info('查找是否存在登录按钮来判断登录是否成功')
        logbtn = self.is_element_exsist(*self.login_btn_loc)
        if logbtn:
            logging.info('还存在登录按钮，登录失败')
            return False
        else:
            logging.info('不存在登录按钮，登录成功')
            return True


