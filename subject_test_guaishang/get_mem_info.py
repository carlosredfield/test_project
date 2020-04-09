import os
import time
import csv


class Controller():
    def __init__(self):

        # 定义手机数据的标题
        self.alldata = [('序号', '虚存', '实存')]

    # 分析数据
    def analysis_data(self):
        content = self.read_file()
        i = 0
        for line in content:
            if 'com.houwei.guaishang' in line:
                print(line)
                vss = line.split()[5].strip('K')  # 获取虚存
                rss = line.split()[6].strip('K')  # 获取实存
                self.alldata.append((i, vss, rss))
                i = i + 1

    # 读取内存文件
    def read_file(self):
        memfile = open('./data/meminfo', 'r')
        content = memfile.readlines()
        memfile.close()
        return content

    # 数据存储
    def save_data_to_csv(self):
        csvfile = open('./data/meminfo_info.csv', 'w', newline='')
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()


if __name__ == '__main__':
    con = Controller()
    con.analysis_data()
    con.save_data_to_csv()
