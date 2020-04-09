import random
import time
import logging
from base_view.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By


class GoodsPage(BasePage):

    goods_id = random.randint(18, 23)

    url = '/Shop/shop_show?id=%d' % goods_id
    # 定位器
    add_num_loc = (By.ID, 'jia')
    reduce_num_loc = (By.ID, 'jian')
    add_car_loc = (By.CLASS_NAME, 'sc_gwc')
    buy_now_loc = (By.CLASS_NAME, 'sc_btn')

    def add_goods_num(self, n=None):
        if n == None:
            pass
        else:
            logging.info('点击增加商品%d件，共%d件' % (n, n + 1))
            while n > 0:
                self.find_element(*self.add_num_loc).click()
                time.sleep(2)
                n = n - 1

    def add_shopping_car(self):
        logging.info('点击添加购物车')
        self.find_element(*self.add_car_loc).click()

    def buy_now(self):
        logging.info('点击立即购买')
        self.find_element(*self.buy_now_loc).click()

    def add_shopping_car_action(self, n):
        logging.info('打开商品详情页')
        self.open()
        self.add_goods_num(n)
        self.add_shopping_car()

    def buy_now_action(self, n):
        logging.info('打开商品详情页')
        self.open()
        self.add_goods_num(n)
        self.buy_now()
