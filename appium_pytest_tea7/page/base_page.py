import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
# from test_case.conftest import appium_desired


class BasePage():
    # 黑名单：处理广告、好评、定位权限等待弹窗
    # black_list = [
    #     (By.ID, 'android:id/button1')
    # ]

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc):
        try:
            element = self.driver.find_element(*loc)
        except NoSuchElementException:
            logging.info('找不到元素')
            return None
        else:
            return element

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return(x, y)

    def swipe_left(self):
        size = self.get_size()
        x1 = size[0] * 0.8
        y1 = size[1] * 0.5
        x2 = size[0] * 0.2
        logging.info('左滑操作')
        self.driver.swipe(x1, y1, x2, y1, 1000)

    def swipe_down(self):
        size = self.get_size()
        x1 = size[0] * 0.5
        y1 = size[1] * 0.8
        y2 = size[0] * 0.2
        logging.info('下滑操作')
        self.driver.swipe(x1, y1, x1, y2, 1000)

    # # 黑名单处理：处理广告、好评、定位权限等待弹窗
    # def excpetion_handle(self):
    #     for locator in self.black_list:
    #         elements = self.driver.find_elements(*locator)
    #         if len(elements) >= 1:  # 如果弹窗元素出现就点击它
    #             elements[0].click()
    #         else:
    #             print(f'{locator} not found')

    # 判断元素是否存在
    def is_element_exsist(self, *loc):
        try:
            self.driver.find_element(*loc)
            return True
        except:
            logging.info('找不到元素')
            return False

    def get_screenshot(self, module_name, filename):
        nowtime = time.strftime('%Y_%m_%d_%H_%M_%S')
        self.driver.get_screenshot_as_file('../screenshots/' + module_name + '/' + nowtime + filename + '.png')

    def toast_text(self):
        logging.info('获取toast')
        toast_text = self.find_element(By.XPATH, "//*[@class='android.widget.Toast']").text
        return toast_text
