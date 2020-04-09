import sys
sys.path.append('D:\\Atest_project\\appium_pytest_tea7')
import logging
import pytest
from page.my_page import MyPage
from page.login_page import LoginPage


class TestLogin():

    @pytest.mark.skip(reason='暂时跳过')
    def test_tea7_login_success(self, login_page):
        logging.info('开始运行登录成功测试')
        login_page.login_action('16533907260', 'cqcarlos1230')
        flag = login_page.check_login_status()
        toast = login_page.get_toast_text()
        assert flag == True, '判断登录成功，成功为True，实际值为%s' % flag

    @pytest.mark.parametrize('phone_num,password,assert_msg',
                             [('165339060', 'cqcaos123', '请输入正确的手机号'),
                                 ('', 'cqcarlos1230', '请输入手机号'),
                                 ('16533907260', '', '请输入密码'),
                              ])
    def test_tea7_login_fail(self, login_page, phone_num, password, assert_msg):
        logging.info('开始运行登录失败测试')
        login_page.login_action(phone_num, password)
        toast = login_page.get_toast_text()
        flag = login_page.check_login_status()
        assert assert_msg in toast
        assert flag == False, '判断登录失败，失败为False，实际值为%s' % flag


if __name__ == '__main__':
    pytest.main(['-s', 'test_login.py'])
