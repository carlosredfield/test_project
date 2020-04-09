import sys
sys.path.append('d:/Atest_project/requests_pytest_xunyuji')
import json
import logging
import pytest
import allure
from util.get_data import data
from util.method import Method


@pytest.mark.skip(reason="修改订单金额有风险，谨慎")
@allure.feature('修改商品订单信息')
class TestGoodsOrder():
    method = Method()
    order_data = data('TestGoodsOrder', 'test_goods_order')

    @allure.story('修改金额')
    @pytest.mark.parametrize("pay_data", order_data['data'])
    def test_goods_order(self, login, pay_data):
        logging.info('开始测试：订单信息')
        cookies = login
        header = self.order_data['header']
        url_add_address = self.order_data['url']

        logging.info('修改订单信息')
        r = self.method.main_way('post', url=url_add_address, headers=header,
                                 cookies=cookies, data=pay_data)
        res = r.json()['msg']
        logging.info('操作失败', "判断修改订单金额失败，失败消息为'操作失败'，当前消息为：%s" % res)

        assert res == '操作失败', "判断修改订单金额失败，失败消息为'操作失败'，当前消息为：%s" % res


if __name__ == '__main__':
    pytest.main(["-s", "test_goods_order.py"])
