import sys
sys.path.append('D:\\Atest_project\\selenium_xunyuji_project')
import logging
import unittest
from common.tools import *
from BSTestRunner import BSTestRunner
import time


def RunMain():
    report_dir = '../report'
    testcase_dir = '../test_case'

    logging.info('查找测试用例')
    discover = unittest.defaultTestLoader.discover(testcase_dir, pattern='test_*.py')
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    report_name = report_dir + '/' + now + 'result.html'

    logging.info('开始写报告')
    with open(report_name, 'wb+')as f:
        runner = BSTestRunner(stream=f, title='XunYuJi_UI_TestReport', description='寻渔记UI自动化测试')
        logging.info('运行测试用例')
        runner.run(discover)
        logging.info('运行测试用例结束')

    logging.info('查找最新报告')
    latest_report = last_report(report_dir)

    logging.info('开始发送邮件')
    sendmail(latest_report)
    logging.info('邮件发送完毕')


if __name__ == '__main__':
    RunMain()
