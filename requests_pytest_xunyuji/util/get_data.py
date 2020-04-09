import logging
import yaml
import json


def data(test_class, case):
    file_path = '../data/%s.json' % test_class
    with open(file_path, encoding='utf-8') as f:
        data = json.load(f)
    logging.info(f"加载用例{case}的json文件")
    return data[case]



def yaml_data(title):
    file_path = '../config/config_data.yaml'
    with open(file_path, encoding='utf-8') as f:
        data = yaml.safe_load(f)
    logging.info(f"加载配置{title}的yaml文件")
    return data.get(title)



if __name__ == '__main__':
    # data = data('TestShoppingCar', 'test_shopping_car_success')
    # print(data['data'])
    data = yaml_data('DB')
    print(data)
