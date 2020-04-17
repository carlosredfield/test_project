import sys
sys.path.append('d:/Atest_project/requests_pytest_xunyuji')
import os
import time
import logging
from util.send_mail import send_mail


def run():
    os.chdir('D:\\Atest_project\\requests_pytest_xunyuji\\test_case')
    logging.info('开始启动测试')
    os.system('pytest --html=../reports/report.html --self-contained-html')
    logging.info('测试完毕')
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
