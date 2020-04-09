import sys
sys.path.append('D:\\Atest_project\\selenium_xunyuji_project')
import logging
import unittest
from ddt import ddt, data, unpack
from drivermodel.driver import browser
from page_view.register_page import RegisterPage


@ddt
class TestRegister(unittest.TestCase):
    def setUp(self):
        logging.info('开始测试注册模块')
        self.driver = browser()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    def tearDown(self):
        logging.info('结束测试注册模块')
        self.driver.quit()

    @data(
        [1, '13596969696', 'xxx123', 'xxx123', '83721', '9527', '手机验证码不正确'],
        [2, '13596969696', 'xxx123', 'xxx123', '', '9527', '手机验证码不正确'],
        [3, '', 'xxx123', 'xxx123', '83721', '9527', '手机号不能为空'],
    )
    # 注册失败的测试
    @unpack
    def test_register_fail(self, num, username, password, password_confirm, invite, code, assert_status):
        logging.info('开始测试注册的第%d条用例' % num)
        po = RegisterPage(self.driver)
        po.register_action(username, password, password_confirm, invite, code)
        try:
            status = po.register_status()
        except:
            po.click_register_submit_btn()
            status = po.register_status()
        self.assertEqual(status, assert_status)


if __name__ == '__main__':
    unittest.main()
