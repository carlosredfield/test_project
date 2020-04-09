import sys
sys.path.append('D:\\Atest_project\\selenium_xunyuji_project')
import logging
import unittest
from ddt import ddt, data, unpack
from drivermodel.driver import browser
from page_view.login_page import LoginPage
from page_view.goods_page import GoodsPage
from page_view.shopping_car_page import ShoppingCarPage


@ddt
class TestOrder(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        logging.info('开始测试订单模块')
        self.driver = browser()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get('https://www.rzmwzc.com/member/common/login.html')
        self.login = LoginPage(self.driver)
        self.login.login_action('16533907260', 'xunyuji123')
        self.gp = GoodsPage(self.driver)
        self.scp = ShoppingCarPage(self.driver)

    @classmethod
    def tearDownClass(self):
        logging.info('结束测试订单模块')
        self.driver.quit()

    # @unittest.skip
    def test_shopping_car_001(self):
        logging.info('开始测试:提交订单后，在订单页面正确显示订单号，金额、商品信息，数量')
        self.gp.add_shopping_car_action(1)
        gid = self.gp.goods_id
        falg = self.scp.goods_exist(gid)
        self.assertEqual(falg, True)
        logging.info('结束测试:商品添加至购物车，在购物车内是否被显示')