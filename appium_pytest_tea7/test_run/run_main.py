import sys
sys.path.append('D:\\Atest_project\\appium_pytest_tea7')
import os
import time
import logging
from common.tools_unit import send_mail


def run():
    logging.info('连接手机')
    os.system('adb connect 192.168.3.24:5555')
    os.chdir('D:\\Atest_project\\appium_pytest_tea7\\test_case')
    os.system('pytest --html=../reports/report.html --self-contained-html')
    logging.info('发送邮件')
    send_mail('../reports/report.html')
    logging.info('发送完毕')
    # logging.info('开始启动测试')
    # os.system('pytest --alluredir ../reports/allure_raw')
    # logging.info('测试完毕')
    # logging.info('打开报告')
    # os.system('allure serve ../reports/allure_raw')


if __name__ == '__main__':
    run()
