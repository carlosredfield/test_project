import sys
sys.path.append('d:/Atest_project/requests_pytest_xunyuji')
import json
import logging
import pytest
from util.get_data import data
from util.db import UserDB
from util.method import Method



@pytest.fixture(scope='class')
def login():
    method = Method()
    url_home = 'https://www.rzmwzc.com/'
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }
    logging.info('获取cookies')
    r = method.main_way('get', url=url_home, headers=header)
    cookies = r.cookies
    logging.info('返回cookies')

    url_login = 'https://www.rzmwzc.com/member/common/actlogin'
    data = {"sUserName": "16533907260", "sPassword": "xunyuji123"}
    logging.info('登录')
    r = method.main_way('post', url=url_login, headers=header, cookies=cookies, data=data)
    res = r.json()['status']
    if res == 1:
        logging.info('登录成功')
    else:
        logging.error('登录失败')
    return cookies




if __name__ == '__main__':
    login()
