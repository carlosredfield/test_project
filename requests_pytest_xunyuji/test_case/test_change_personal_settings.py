import sys
sys.path.append('d:/Atest_project/requests_pytest_xunyuji')
import json
import logging
import pytest
import allure
from util.get_data import data
from util.method import Method


@allure.feature('更改个人信息模块')
class TestChangePersonalSettings():
    method = Method()
    chg_data = data('TestChangePersonalSettings', 'test_change_personal_settings')

    @allure.story('更改个人信息')
    @pytest.mark.parametrize("personal_data", chg_data['data'])
    def test_change_personal_settings(self, login, personal_data):
        logging.info('开始测试：修改个人信息用例')
        cookies = login
        header = self.chg_data['header']
        url_add_address = self.chg_data['url']

        logging.info('修改个人信息')
        r = self.method.main_way('post', url=url_add_address, headers=header,
                                 cookies=cookies, data=personal_data)
        res = r.text
        assert '修改成功' not in res, "判断修改失败，如果显示修改成功则用例失败"


if __name__ == '__main__':
    pytest.main(["-s", "test_change_personal_settings.py"])
