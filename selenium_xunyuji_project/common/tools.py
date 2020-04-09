from selenium import webdriver
import os
import yagmail


def last_report(report_dir):
    lists = os.listdir(report_dir)  # 获取文件夹报告列表
    lists.sort(key=lambda fn: os.path.getatime(report_dir + '/' + fn))  # fn代表其中一个元素
    file = os.path.join(report_dir, lists[-1])  # 得到最新文件
    file = file.replace('\\', '/')
    return file


def sendmail(last_report):
    f = open(last_report, 'r', encoding='utf-8')
    mail_content = f.read()
    f.close()

    yag = yagmail.SMTP(user='zjpcarlos1230@163.com', password='163carlos1230', host='smtp.163.com')
    yag.send('zjpcarlos1230@163.com', 'XunYuJi_UI_TestReport', mail_content, last_report)


if __name__ == '__main__':
    pass
