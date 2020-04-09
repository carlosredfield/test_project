import logging
import time
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page import home_page


class GoodsPage(BasePage):
    customer_service_loc = (By.ID, 'com.tea7.app:id/tv_kefu')
    check_shopping_car_loc = (By.ID, 'com.tea7.app:id/ll_cart')
    add_shopping_car_loc = (By.ID, 'com.tea7.app:id/tv_cart')
    add_goods_num_loc = (By.ID, 'com.tea7.app:id/tv_jia')
    sure_btn_loc = (By.ID, 'com.tea7.app:id/tv_sure')
    collection_loc = (By.ID, 'com.tea7.app:id/ll_shoucang')
    buy_now_loc = (By.ID, 'com.tea7.app:id/tv_buy')
    share_loc = (By.ID, 'com.tea7.app:id/ll_share')
    home_loc = (By.ID, 'com.tea7.app:id/ll_home')
    goods_name_loc = (By.ID, 'com.tea7.app:id/tv_name')

    # 输入手机号
    def click_customer_service(self):
        logging.info('点击客服')
        self.find_element(*self.customer_service_loc).click()

    def check_shopping_car(self):
        logging.info('点击查看购物车')
        self.find_element(*self.check_shopping_car).click()

    def add_shopping_car(self):
        logging.info('点击加入购物车')
        self.find_element(*self.add_shopping_car_loc).click()
        self.find_element(*self.add_goods_num_loc).click()
        self.find_element(*self.sure_btn_loc).click()

    def collection(self):
        logging.info('点击收藏')
        self.find_element(*self.collection_loc).click()

    def buy_now(self):
        logging.info('点击立即购买')
        self.find_element(*self.buy_now_loc).click()

    def get_toast_text(self):
        toast_text = self.toast_text()
        return toast_text

    def get_goods_name(self):
        name = self.find_element(*self.goods_name_loc).text
        return name

    def go_to_home_page(self):
        logging.info('点击收藏')
        self.find_element(*self.share_loc).click()
        self.find_element(*self.home_loc).click()
        return home_page.HomePage(self.driver)
