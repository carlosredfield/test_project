import sys
sys.path.append('D:\\Atest_project\\selenium_xunyuji_project')

from selenium import webdriver
import logging.config

# 读取日志配置
CON_LOG = '../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


def browser(bro=None):

    if bro == None:
        logging.info('启动火狐浏览器')
        driver = webdriver.Firefox()
    elif bro == 'Chrome':
        logging.info('启动谷歌浏览器')
        driver = webdriver.Chrome()
    elif bro == 'Edge':
        logging.info('启动IE浏览器')
        driver = webdriver.Edge()
    else:
        logging.info('启动其他浏览器')

    # driver.get('http://www.baidu.com')

    return driver


if __name__ == '__main__':
    browser()
