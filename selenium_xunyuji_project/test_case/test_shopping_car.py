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
class TestShoppingCar(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        logging.info('开始测试购物车模块')
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
        logging.info('结束测试购物车模块')
        self.driver.quit()

    # @unittest.skip
    def test_shopping_car_001(self):
        logging.info('开始测试:商品添加至购物车，在购物车内是否被显示')
        self.gp.add_shopping_car_action(1)
        gid = self.gp.goods_id
        falg = self.scp.goods_exist(gid)
        self.assertEqual(falg, True)
        logging.info('结束测试:商品添加至购物车，在购物车内是否被显示')

    # @unittest.skip
    def test_shopping_car_002(self):
        logging.info('开始测试:商品添加至购物车，从购物车内删除，查看商品是否被删除')
        self.gp.add_shopping_car_action(1)
        gid = self.gp.goods_id
        car_id = self.scp.get_shopping_car_id(gid)
        flag = self.scp.delete_goods(car_id)
        self.assertEqual(flag, True)
        logging.info('结束测试:商品添加至购物车，从购物车内删除，查看商品是否被删除')

    # @unittest.skip
    def test_shopping_car_003(self):
        logging.info('开始测试:添加3件商品添加至购物车，从购物车内查看商品是否存在3件')
        self.gp.add_shopping_car_action(2)
        gid = self.gp.goods_id
        car_id = self.scp.get_shopping_car_id(gid)
        flag = self.scp.get_shopping_car_num(car_id)
        self.assertEqual(flag, 3)
        logging.info('结束测试:添加3件商品添加至购物车，从购物车内查看商品是否存在3件')

    # @unittest.skip
    def test_shopping_car_004(self):
        logging.info('开始测试:未登录时点击购物车，跳转到用户登录页面')
        self.scp.logout_action()
        self.scp.open_shopping_car_page()
        flag = self.login.check_login_btn_exist()
        self.assertEqual(flag, True)
        logging.info('结束测试:未登录时点击购物车，跳转到用户登录页面')

    def test_shopping_car_005(self):
        logging.info('开始测试:商品在未勾选的状态下，结算按钮点击时弹出提示按钮"请选择商品"')
        self.gp.add_shopping_car_action(1)
        self.scp.open_shopping_car_page()
        flag = self.scp.is_alert()
        self.assertEqual(flag, True)
        logging.info('结束测试:商品在未勾选的状态下，结算按钮点击时弹出提示按钮"请选择商品"')




if __name__ == '__main__':
    unittest.main()
