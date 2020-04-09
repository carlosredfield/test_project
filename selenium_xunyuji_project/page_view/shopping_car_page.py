import time
import logging
from base_view.base_page import BasePage
from page_view.goods_page import GoodsPage
from selenium import webdriver
from selenium.webdriver.common.by import By


class ShoppingCarPage(BasePage):

    url = '/shop/car_list'
    logout_loc = (By.LINK_TEXT, '退出')  # 退出按钮
    settlement_btn_loc = (By.ID, 'jiesuan2')  # 结算按钮

    def open_shopping_car_page(self):
        logging.info('打开购物车页面')
        self.open()
        logging.info('打开购物车页面成功')

    def logout_action(self):
        logging.info('退出登录')
        self.find_element(*self.logout_loc).click()

    # 根据商品goods_id查看是否存在购物车内
    def goods_exist(self, goods_id):
        logging.info('打开购物车页面')
        self.open()
        # 找到该商品的id
        path = '//a[@href="/Shop/shop_show?id=%s"]' % goods_id
        id_path = (By.XPATH, path)
        # 判断是否存在
        try:
            goods = self.find_element(*id_path)
            logging.info('该商品在购物车内')
            return True
        except:
            logging.error('该商品不在购物车内')
            self.get_screenshot('shopping_car_page', '该商品不在购物车内')
            return False

    # 根据商品goods_id查看该商品的购物车car_id
    def get_shopping_car_id(self, goods_id):

        flag = self.goods_exist(goods_id)
        # 查找商品id
        if flag == True:
            logging.info('获取该商品在购物车的购物车ID')
            path = '//a[@href="/Shop/shop_show?id=%s"]/../input' % goods_id
            car_id_path = (By.XPATH, path)
            return self.find_element(*car_id_path).get_attribute('value')
        else:
            logging.error('该商品不在购物车内')
            self.get_screenshot('shopping_car_page', '该商品不在购物车内')

    # 根据购物车car_id进行删除对应的商品
    def delete_goods(self, car_id):
        logging.info('打开购物车页面')
        self.open()
        path = '//a[@href="/shop/car_del/id/%s"]' % car_id
        id_path = (By.XPATH, path)
        logging.info('在购物车内根据ID删除对应商品')
        goods = self.find_element(*id_path).click()
        try:
            good = self.find_element(*id_path)
            logging.error('删除不成功')
            self.get_screenshot('shopping_car_page', '删除不成功')
            return False
        except:
            logging.info('删除成功')
            return True

    # 根据购物车car_id获取商品的数量
    def get_shopping_car_num(self, car_id):
        path = 'shuliang%s' % car_id
        id_path = (By.ID, path)
        num = self.find_element(*id_path).get_attribute('value')
        return int(num)

    def click_settlement_btn(self):
        self.find_element(*self.settlement_btn_loc).click()

    def is_alert(self):
        self.click_settlement_btn()
        alert = self.alert_windows()

        if '请选择商品' in alert:
            logging.info('弹窗弹出"请选择商品"')
            return True
        else:
            logging.error('没有弹窗弹出"请选择商品"')
            self.get_screenshot('shopping_car_page', '没有弹窗弹出"请选择商品')
            return False
