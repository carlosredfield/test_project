import os
import time
import csv


class App():
    def __init__(self):
        self.content = ''
        self.start_time = 0

    def launch_app(self):
        cmd = 'adb shell am start -W -n com.houwei.guaishang/.activity.WelcomeActivity'
        self.content = os.popen(cmd)

    def stop_app(self):
        cmd = 'adb shell am force-stop com.houwei.guaishang'
        os.system(cmd)

    def get_launched_time(self):
        for line in self.content.readlines():
            if 'ThisTime' in line:
                self.start_time = line.split(':')[1]
                break
        return self.start_time


class Controller():
    def __init__(self, count):
        self.app = App()
        self.counter = count
        self.alldata = [('测试时间', '冷启动时间')]

    # 单次测试过程
    def test_process(self):
        self.app.launch_app()
        time.sleep(5)
        elapsedtime = self.app.get_launched_time()
        self.app.stop_app()
        time.sleep(3)
        current_time = self.get_current_time()
        self.alldata.append((current_time, elapsedtime))

    # 多次执行测试过程
    def run(self):
        while self.counter > 0:
            self.test_process()
            self.counter = self.counter - 1

    # 获取当前时间戳
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())
        return current_time

    # 数据存储
    def save_data_to_csv(self):
        csvfile = open('./data/strat_time.csv', 'w', newline='')
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()


if __name__ == '__main__':
    con = Controller(10)
    con.run()
    con.save_data_to_csv()
