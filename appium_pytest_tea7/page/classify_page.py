import logging
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.goods_page import GoodsPage


class ClassifyPage(BasePage):
    lg_recommend_loc = (By.XPATH, '//android.widget.TextView[@text="推荐"]')
    lg_green_tea_loc = (By.XPATH, '//android.widget.TextView[@text="绿茶"]')
    lg_red_tes_loc = (By.XPATH, '//android.widget.TextView[@text="红茶"]')
    lg_oolong_tea_loc = (By.XPATH, '//android.widget.TextView[@text="乌龙"]')
    tie_Guan_yin_loc = (By.XPATH, '//android.widget.TextView[@text="铁观音"]')
    longjin_loc = (By.XPATH, '//android.widget.TextView[@text="龙井"]')
    goods_02_loc = (By.XPATH, '//android.widget.TextView[@text="浓香型 铁观音2号 250克 消青工艺"]')

    def choose_goods(self):
        logging.info('点击铁观音')
        self.find_element(*self.tie_Guan_yin_loc).click()
        logging.info('点击铁观音分类下的2号商品')
        self.find_element(*self.goods_02_loc).click()
        return GoodsPage(self.driver)
