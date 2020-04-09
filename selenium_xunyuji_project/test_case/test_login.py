import sys
sys.path.append('D:\\Atest_project\\selenium_xunyuji_project')
import logging
import unittest
from ddt import ddt, data, unpack
from drivermodel.driver import browser
from page_view.login_page import LoginPage


@ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        logging.info('开始测试登录模块')
        self.driver = browser()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    def tearDown(self):
        logging.info('结束测试登录模块')
        self.driver.quit()

    @data(
        [1, '16533907260', 'xunyuji123']
    )
    # 登录成功的测试
    @unpack
    #@file_data("./login_success_data.json")
    def test_login_success(self, num, username, password):
        logging.info('开始测试登录成功的第%d条用例' % num)
        po = LoginPage(self.driver)
        po.login_action(username, password)
        self.assertEqual(po.type_loginpass(), '退出')

    @data(
        [1, '', 'xunyuji123', '请填写手机号'],
        [2, '', 'xxcarlos1230', '请填写手机号'],
        [3, '13559696485', '', '请填写密码'],
        [4, '13590388547', 'xxc8555230', '用户名或者密码错误！'],
    )
    # 登录失败的测试
    @unpack
    #@file_data("./login_fail_data.json")
    def test_login_fail(self, num, username, password, assert_status):
        logging.info('开始测试登录失败的第%d条用例' % num)
        po = LoginPage(self.driver)
        po.login_action(username, password)
        try:
            status = po.login_status()
        except:
            po.click_login_submit_btn()
            status = po.login_status()
        self.assertEqual(status, assert_status)


if __name__ == '__main__':
    unittest.main()
