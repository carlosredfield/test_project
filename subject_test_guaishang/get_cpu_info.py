import os
import time
import csv


class Controller():
    def __init__(self, count):
        # 设置执行次数
        self.counter = count
        # 设置表头
        self.alldata = [('测试时间', 'cpu状态')]

    # 单次测试过程
    def test_process(self):
        cmd = 'adb shell dumpsys cpuinfo | findstr com.houwei.guaishang'
        result = os.popen(cmd)
        # 获取cpu占用率
        cpu_value = result.readline().split('%')[0].strip()
        current_time = self.get_current_time()
        self.alldata.append((current_time, cpu_value))
        print(self.alldata)

    # 多次执行测试过程
    def run(self):
        while self.counter > 0:
            self.test_process()
            self.counter = self.counter - 1
            time.sleep(3)  # 每3秒采集一次数据

    # 获取当前时间戳
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())
        return current_time

    # 数据存储
    def save_data_to_csv(self):
        csvfile = open('./data/cpu_info.csv', 'w', newline='')
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()


if __name__ == '__main__':
    con = Controller(10)
    con.run()
    con.save_data_to_csv()
