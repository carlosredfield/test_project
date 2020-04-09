import sys
sys.path.append('d:/Atest_project/requests_pytest_xunyuji')
import json
import logging
import pytest
import allure
from util.get_data import data
from util.method import Method


@allure.feature('购物车模块')
class TestShoppingCar():
    method = Method()
    suc_data = data('TestShoppingCar', 'test_shopping_car_success')
    fail_data = data('TestShoppingCar', 'test_shopping_car_success')

    @allure.story('添加商品至购物车成功用例')
    @pytest.mark.parametrize("goods_id", suc_data['data'])
    def test_shopping_car_success(self, login, goods_id):
        logging.info('开始测试：添加商品至购物车成功用例')
        cookies = login
        header = self.suc_data['header']
        url_add_address = self.suc_data['url']

        logging.info('添加商品至购物车')
        r = self.method.main_way('post', url=url_add_address, headers=header,
                                 cookies=cookies, data=goods_id)
        res = r.json()['msg']
        logging.info('添加消息为：%s' % res)
        assert res == '添加成功', "判断添加商品至购物车成功，成功消息为'添加成功'，当前消息为：%s" % res

    @allure.story('添加商品至购物车失败用例')
    @pytest.mark.parametrize("goods_id", fail_data['data'])
    def test_shopping_fail(self, login, goods_id):
        logging.info('开始测试：添加商品至购物车失败用例')
        cookies = login
        header = self.fail_data['header']
        url_add_address = self.fail_data['url']

        logging.info('添加商品至购物车')
        r = self.method.main_way('post', url=url_add_address, headers=header,
                                 cookies=cookies, data=goods_id)
        res = r.json()['msg']
        logging.info('添加消息为：%s' % res)
        assert res == '添加失败', "判断添加商品至购物车失败，失败消息为'添加失败'，当前消息为：%s" % res


if __name__ == '__main__':
    # pytest.main(["-s", "test_shopping_car.py"])
    pytest.main(["-s", "--alluredir", "../report"])
