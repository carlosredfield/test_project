import logging
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.classify_page import ClassifyPage


class ShoppingCarPage(BasePage):

    settlement_loc = (By.ID, 'com.tea7.app:id/tv_pay')
    toast = (By.XPATH, "//*[@class='android.widget.Toast']")
    classify_page_loc = (By.ID, 'com.tea7.app:id/iv_class')
    goods_num_loc = (By.ID, 'com.tea7.app:id/tv_number')
    edit_loc = (By.ID, 'com.tea7.app:id/tv_edit')
    select_all_loc = (By.XPATH, '//android.widget.TextView[@text="全选(0)"]')
    delete_loc = (By.ID, 'com.tea7.app:id/tv_delete')
    remove_collection_loc = (By.ID, 'com.tea7.app:id/tv_remove_shou_cang')

    def settlement(self):
        logging.info('点击结算按钮')
        self.find_element(*self.settlement_loc).click()

    def get_toast_text(self):
        toast_text = self.toast_text()
        return toast_text

    def go_to_classify_page(self):
        logging.info('点击"分类"按钮')
        self.find_element(*self.classify_page_loc).click()
        return ClassifyPage(self.driver)

    def get_goods_num(self):
        logging.info('获取商品数量')
        goods_num = self.find_element(*self.goods_num_loc).text
        return goods_num

    def click_edit_btn(self):
        logging.info('点击编辑按钮')
        self.find_element(*self.edit_loc).click()

    def click_select_all(self):
        logging.info('点击全选')
        self.find_element(*self.select_all_loc).click()

    def click_delete_btn(self):
        logging.info('点击删除所选')
        self.find_element(*self.delete_loc).click()

    def delete_all(self):
        logging.info('删除所有购物车商品')
        self.click_edit_btn()
        self.click_select_all()
        self.click_delete_btn()
