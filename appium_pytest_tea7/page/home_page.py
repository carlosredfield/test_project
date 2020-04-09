import logging
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.my_page import MyPage
from page.shopping_car_page import ShoppingCarPage


class HomePage(BasePage):
    myb_tn_loc = (By.ID, 'com.tea7.app:id/ll_my')
    shopping_car_loc = (By.ID, 'com.tea7.app:id/ll_cart')

    def go_to_my_page(self):
        logging.info('点击"我的"跳转到该页')
        self.find_element(*self.myb_tn_loc).click()
        return MyPage(self.driver)

    def go_to_shopping_car_page(self):
        logging.info('点击购物车按钮')
        self.find_element(*self.shopping_car_loc).click()
        return ShoppingCarPage(self.driver)
