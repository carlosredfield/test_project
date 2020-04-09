import sys
sys.path.append('D:\\Atest_project\\appium_tea7')
from HTMLTestRunner import HTMLTestRunner
from common.tools_unit import *
import unittest
import time
import logging

'''

test_dir = '../test_case'
report_dir = '../reports'

#加载测试用例
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

#定义报告的文件格式
now = time.strftime("%Y_%m_%d_%H_%M_%S")
report_name = report_dir + '/' + now + ' test_report.html'

#运行用例并生成测试报告
with open(report_name,'wb') as f:
    runner = HTMLTestRunner(stream=f, title="凤凰众筹app测试报告", description="主要为凤凰众筹app的自动化登录测试")
    logging.info("=====开始运行用例并生成测试报告=====")
    runner.run(discover)

logging.info('=====开始发邮件=====')
file = last_report(report_dir)
send_mail(file)
logging.info('=====邮件发送完毕=====')

'''