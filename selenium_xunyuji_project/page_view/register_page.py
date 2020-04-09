from base_view.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By


class RegisterPage(BasePage):

    url = '/member/common/register.html'
    # 定位器
    username_loc = (By.ID, 'txtPhone')
    password_loc = (By.ID, 'txtPwd')
    password_confirm_loc = (By.ID, 'txtRepwd')
    invite_loc = (By.ID, 'invite')
    get_code_loc = (By.ID, 'TencentCaptcha')
    type_code_loc = (By.ID, 'code')
    register_btn_loc = (By.ID, 'Img12')
    agree_btn_loc = (By.ID, 'xieyi')
    content = (By.CLASS_NAME, 'layui-layer-content')

    def type_username(self, username):
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)

    def type_password_confirm(self, password_confirm):
        self.find_element(*self.password_confirm_loc).send_keys(password_confirm)

    def type_invite(self, invite):
        self.find_element(*self.invite_loc).send_keys(invite)

    def click_get_code_btn(self):
        self.find_element(*self.get_code_loc).click()

    def type_code(self, code):
        self.find_element(*self.type_code_loc).send_keys(code)

    def click_register_submit_btn(self):
        self.find_element(*self.register_btn_loc).click()

    def register_action(self, username, password, password_confirm, invite, code):
        self.open()
        self.type_username(username)
        self.type_password(password)
        self.type_password_confirm(password)
        self.type_invite(invite)
        self.type_code(code)
        self.click_register_submit_btn()

    def register_status(self):
        return self.find_element(*self.content).text
