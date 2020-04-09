import time
import logging
from base_view.base_page import BasePage
from page_view.goods_page import GoodsPage
from selenium import webdriver
from selenium.webdriver.common.by import By


class ShoppingCarPage(BasePage):

    url = '/shop/do_order'
    logout_loc = (By.LINK_TEXT, '退出')  # 退出按钮
    settlement_btn_loc = (By.ID, 'jiesuan2')  # 结算按钮

    def open_shopping_car_page(self):
        logging.info('打开购物车页面')
        self.open()
        logging.info('打开购物车页面成功')

    def logout_action(self):
        logging.info('退出登录')
        self.find_element(*self.logout_loc).click()