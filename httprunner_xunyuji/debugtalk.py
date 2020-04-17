import os
import random


def ENV(keyname):
    '''
    获取环境keyname对应的值
    :return:
    '''
    value = os.environ.get(keyname, '')
    return value

# 前置操作


def setup():
    print('setup')

# 后置操作


def teardown():
    print('teardown')

# 生成随机商品id


def rand():
    goods_id = random.randint(1, 60)
    return goods_id

# 拼接符合要求提交的格式


def change_carids(carids):
    return '0,' + str(carids)

# 读取文件内容


def get_file(filePath):
    return open(filePath, "rb")


if __name__ == '__main__':
    print(change_carids(3756))
