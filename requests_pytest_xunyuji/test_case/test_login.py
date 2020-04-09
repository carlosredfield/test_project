import sys
sys.path.append('d:/Atest_project/requests_pytest_xunyuji')

import json
import logging
import pytest
import allure
from util.get_data import data
from util.method import Method


@allure.feature('登录模块')
class TestLogin():
    method = Method()
    suc_data = data('TestLogin', 'test_login_success')
    fail_data = data('TestLogin', 'test_login_fail')

    url_login = suc_data['url']
    header = suc_data['header']
    # 获取cookies

    @allure.story('获取cookies')
    def get_cookies(self):
        url_home = 'https://www.rzmwzc.com/'
        logging.info('获取cookies')
        r = self.method.main_way('get', url=url_home, headers=self.header)
        return r.cookies

    @pytest.mark.parametrize("success_data", suc_data['data'])
    # 登录成功用例
    @allure.story('登录成功用例')
    def test_login_success(self, success_data):
        """
        用例描述：测试登录成功用例
        """
        logging.info('开始测试：登录成功用例')
        cookies = self.get_cookies()
        logging.info('登录')
        r = self.method.main_way('post', url=self.url_login, headers=self.header,
                                 cookies=cookies, data=success_data)
        res = r.json()['status']
        logging.info("判断登录成功，成功状态码为1，当前状态码的值为：%d" % res)

        assert res == 1, "判断登录成功，成功状态码为1，当前状态码的值为：%d" % res

    @pytest.mark.parametrize("fail_data", fail_data['data'])
    # 登录失败用例
    @allure.story('登录失败用例')
    def test_login_fail(self, fail_data):
        """
        用例描述：测试登录失败用例
        """
        logging.info('开始测试：登录失败用例')
        cookies = self.get_cookies()
        logging.info('登录')
        r = self.method.main_way('post', url=self.url_login, headers=self.header, cookies=cookies, data=fail_data)
        res = r.json()['status']
        logging.info("判断登录失败，失败状态码为0，当前状态码的值为：%d" % res)

        assert res == 0, "判断登录失败，失败状态码为0，当前状态码的值为：%d" % res


if __name__ == '__main__':
    # pytest.main(['-s', '-q', '--alluredir', '../report/xml'])
    pytest.main(["-s", "test_login.py"])
