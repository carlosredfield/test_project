import sys
sys.path.append('d:/Atest_project/requests_pytest_xunyuji')
import os
import logging
import pymysql
from util.get_data import yaml_data

DB_CONF = yaml_data('DB')
# services.msc打开MySQL服务


class DB():
    def __init__(self, db_conf=DB_CONF):
        self.conn = pymysql.connect(**db_conf, autocommit=True)
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)  # 字典格式的游标

    def query(self, sql):
        self.cur.execute(sql)
        data = self.cur.fetchall()
        logging.info(f'查询sql: {sql} 查询结果: {data}')
        return data

    def change_db(self, sql):
        result = self.cur.execute(sql)
        logging.info(f'执行sql: {sql} 影响行数: {result}')

    def close(self):
        logging.info('关闭数据库连接')
        self.cur.close()
        self.conn.close()


class UserDB(DB):
    def del_user(self, name):
        logging.info(f'删除用户: {name}')
        sql = f'DELETE FROM xunyuji WHERE name="{name}"'
        self.change_db(sql)

    def check_user(self, name):
        logging.info(f'查询用户: {name}')
        sql = f'SELECT id FROM xunyuji WHERE name="{name}"'
        res = self.query(sql)
        return True if res else False

    def add_user(self, name, pwd):
        logging.info(f'添加用户: {name}')
        sql = f'INSERT INTO xunyuji(name,pwd) VALUES ("{name}","{pwd}")'
        self.change_db(sql)

    def get_user(self, name):
        logging.info(f'获取用户: {name}')
        sql = f'SELECT name,pwd FROM xunyuji WHERE name="{name}"'
        res = self.query(sql)
        return res


if __name__ == '__main__':
    data = UserDB()
    print(data.check_user('16533907260'))
    print(data.get_user('16533907260'))
