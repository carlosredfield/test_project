import os
import time
import csv


class Controller():
    def __init__(self, count):
        # 定义测试次数
        self.counter = count
        # 定义手机数据的标题
        self.alldata = [('测试时间', '流量状态')]

    # 单次测试过程
    def test_process(self):
        # 执行获取进程的命令
        cmd = 'adb shell ps | findstr com.houwei.guaishang'
        result = os.popen(cmd)
        # 获取进程ID
        pid = result.readlines()[0].split(' ')[3]
        # 获取进程ID使用的流量
        cmd = 'adb shell cat /proc/' + pid + '/net/dev'
        traffic = os.popen(cmd)
        for line in traffic:
            if 'wlan0' in line:
                receive = line.split()[1]
                transmit = line.split()[9]

        # 计算所有流量之和
        alltraffic = int(receive) + int(transmit)
        # 按kb计算流量值
        alltraffic = alltraffic / 1024
        # 当前时间
        current_time = self.get_current_time()
        self.alldata.append((current_time, alltraffic))

    # 多次执行测试过程
    def run(self):
        while self.counter > 0:
            self.test_process()
            self.counter = self.counter - 1
            time.sleep(5)  # 每3秒采集一次数据

    # 获取当前时间戳
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())
        return current_time

    # 数据存储
    def save_data_to_csv(self):
        csvfile = open('./data/traffic_info.csv', 'w', newline='')
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()


if __name__ == '__main__':
    con = Controller(10)
    con.run()
    con.save_data_to_csv()
