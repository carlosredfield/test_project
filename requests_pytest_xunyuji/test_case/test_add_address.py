import sys
sys.path.append('d:/Atest_project/requests_pytest_xunyuji')
import json
import logging
import pytest
import allure
from util.get_data import data
from util.method import Method


@allure.feature('添加收货地址模块')
class TestAddAddress():
  method = Method()
  suc_data = data('TestAddAddress', 'test_add_address_scuess')
  fail_data = data('TestAddAddress', 'test_add_address_fail')


  @allure.story('添加收货地址成功用例')
  @pytest.mark.parametrize("address_data", suc_data['data'])
  def test_add_address_scuess(self, login, address_data):
    logging.info('开始测试：添加收货地址成功用例')
    cookies = login
    header = self.suc_data['header']
    url_add_address = self.suc_data['url']

    logging.info('添加收货地址')
    r = self.method.main_way('post', url=url_add_address, headers=header,
                             cookies=cookies, data=address_data)
    res = r.json()['status']
    assert res == 1, "判断添加收货地址成功，成功状态码为1，当前状态码的值为：%d" % res

  @allure.story('添加收货地址失败用例')
  @pytest.mark.parametrize("address_data", fail_data['data'])
  def test_add_address_fail(self, login, address_data):
    logging.info('开始测试：添加收货地址失败用例')
    cookies = login
    header = self.fail_data['header']
    url_add_address = self.fail_data['url']

    logging.info('添加购物车')
    r = self.method.main_way('post', url=url_add_address, headers=header,
                             cookies=cookies, data=address_data)
    res = r.json()['status']
    assert res == 0, "判断添加收货地址失败，失败状态码为0，当前状态码的值为：%d" % res


if __name__ == '__main__':
  pytest.main(["-s", "test_add_address.py"])
