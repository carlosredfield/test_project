import logging
import pytest


class TestShoppingCar():

    def test_shopping_car_001(self, shopping_car_page):
        logging.info('购物车模块测试：没有选择商品的情况下点击结算，弹出‘还没有选择商品按钮')
        goods_page = shopping_car_page.go_to_classify_page().choose_goods()
        goods_page.add_shopping_car()
        toast = goods_page.get_toast_text()
        goods_page.go_to_home_page().go_to_shopping_car_page()
        shopping_car_page.settlement()
        toast = shopping_car_page.get_toast_text()
        shopping_car_page.delete_all()
        assert '还没有选择商品' in toast, '预期弹出“还没有选择商品按钮”，实际值弹出%s' % toast

    def test_shopping_car_002(self, shopping_car_page):
        logging.info('购物车模块测试：商品添加至购物车，在购物车内成功添加')
        goods_page = shopping_car_page.go_to_classify_page().choose_goods()
        goods_page.add_shopping_car()
        toast = goods_page.get_toast_text()
        goods_page.go_to_home_page().go_to_shopping_car_page()
        shopping_car_page.delete_all()
        assert '加入购物车成功' in toast, '预期弹出“加入购物车成功”，实际值弹出%s' % toast

    def test_shopping_car_003(self, shopping_car_page):
        logging.info('购物车模块测试：商品添加3件商品至购物车，在购物车内是否被正确添加3件')
        goods_page = shopping_car_page.go_to_classify_page().choose_goods()
        goods_page.add_shopping_car()
        toast = goods_page.get_toast_text()
        name = goods_page.get_goods_name()
        goods_page.go_to_home_page().go_to_shopping_car_page()
        goods_num = int(shopping_car_page.get_goods_num())
        shopping_car_page.delete_all()
        assert '铁观音2号' in name, '预期显示商品名称，实际显示%s' % name
        assert goods_num == 2, '预期显示商品数量为2，实际显示%s' % name


if __name__ == '__main__':
    pytest.main(['-s', 'test_shopping_car.py'])
