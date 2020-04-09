import os
import time
import csv


class Controller():
    def __init__(self, count):
        # 定义测试次数
        self.counter = count
        # 定义手机数据的标题
        self.alldata = [('测试时间', '电量状态')]

    # 单次测试过程
    def test_process(self):
        # 执行获取进程的命令
        cmd = 'adb shell dumpsys battery'
        result = os.popen(cmd)

        for line in result:
            if 'level' in line:
                # 以空格分割wlan0行字符串
                power = line.split(':')[1].strip()
                break

        # 当前时间
        current_time = self.get_current_time()
        self.alldata.append((current_time, power))

    # 多次执行测试过程
    def run(self):
        #os.popen('adb shell dumpsys battery set status 1')
        while self.counter > 0:
            self.test_process()
            self.counter = self.counter - 1
            time.sleep(5)  # 每5秒采集一次数据

    # 获取当前时间戳
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())
        return current_time

    # 数据存储
    def save_data_to_csv(self):
        csvfile = open('./data/power_info.csv', 'w', newline='')
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()


if __name__ == '__main__':
    con = Controller(10)
    con.run()
    con.save_data_to_csv()
