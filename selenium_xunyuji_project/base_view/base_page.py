import os
import time
import logging


class BasePage():

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.rzmwzc.com/'
        self.timeout = 20

    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)

    def open(self):
        self._open(self.url)

    def find_element(self, *loc):
        try:
            element = self.driver.find_element(*loc)
        except:
            logging.info('找不到元素')
            return None
        else:
            return element

    # 截图
    def get_screenshot(self, module_name, filename):
        nowtime = time.strftime('%Y_%m_%d_%H_%M_%S')
        self.driver.get_screenshot_as_file('../screenshots/' + module_name + '/' + nowtime + filename + '.png')

    def alert_windows(self):
        try:
            alert = self.driver.switch_to.alert
        except:
            logging.info('找不到弹窗')
            return None
        else:
            alert_text = alert.text
            alert.accept()
            return alert_text
