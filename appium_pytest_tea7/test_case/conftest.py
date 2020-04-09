import sys
sys.path.append('D:\\Atest_project\\appium_pytest_tea7')
import os
import yaml
import pytest
import logging.config
from appium import webdriver
from page.home_page import HomePage
from page.my_page import MyPage
from page.login_page import LoginPage
from page.shopping_car_page import ShoppingCarPage
# from page.setting_page import Settingpage


CON_LOG = '../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


@pytest.fixture(scope='session')
def driver():
    with open('../config/desired_caps.yaml', 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']
    base_dir = os.path.dirname(os.path.dirname(__file__))
    app_path = os.path.join(base_dir, 'app', data['appname'])
    desired_caps['app'] = app_path
    desired_caps['noReset'] = data['noReset']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    logging.info('开始启动app')
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
    driver.implicitly_wait(10)
    logging.info('启动完毕')
    yield driver
    driver.close_app()


# 首页
@pytest.fixture(scope='session')
def home_page(driver):
    return HomePage(driver)

# 从首页点击我的跳转我的


@pytest.fixture(scope='session')
def my_page(driver, home_page):
    home_page.go_to_my_page()
    return MyPage(driver)

# 在我的页面点击登录按钮进入登录页面


@pytest.fixture()
def login_page(driver, my_page):
    login_page = my_page.go_to_login_page()
    yield LoginPage(driver)
    # 定位昵称是否存在来判断登录是否成功
    nick_name_btn = my_page.check_login_status()
    if nick_name_btn:
        setting_page = my_page.go_to_setting_page()
        setting_page.Logout()
    else:
        driver.keyevent(4)
        driver.keyevent(4)

# 前置登录操作,登录后跳转“我的”页面


@pytest.fixture(scope='session')
def login_my_page(driver, my_page):
    login_page = my_page.go_to_login_page()
    login_page.login_action('16533907260', 'cqcarlos1230')
    flag = my_page.check_login_status()
    if flag:
        logging.info('登录成功')
    else:
        logging.error('登录失败')
        # driver.get_screenshot('login_page', '登录失败.png')
    return MyPage(driver)


@pytest.fixture(scope='session')
def shopping_car_page(driver, login_my_page):
    login_my_page.go_to_shopping_car_page()
    return ShoppingCarPage(driver)
