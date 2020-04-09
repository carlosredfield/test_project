import sys
sys.path.append('d:\\Atest_project\\xunyuji_appium')
import yagmail
import os
import requests
import re
import datetime


def last_report(report_dir):
    re_list = os.listdir(report_dir)
    re_list.sort(key=lambda fn: os.path.getatime(report_dir + '/' + fn))
    file = os.path.join(report_dir, re_list[-1])  # 得到最新文件
    file = file.replace('\\', '/')
    return file


def send_mail(last_report):
    f = open(last_report, 'r', encoding='utf-8')
    mail_content = f.read()
    f.close()

    yag = yagmail.SMTP(user='zjpcarlos1230@163.com', password='163carlos1230', host='smtp.163.com')
    yag.send('zjpcarlos1230@163.com', '茶7网app自动化测试报告', mail_content, last_report)


def get_phone(exist_phone=[]):
    for page in range(1, 3):  # 循环3页
        total_url = 'https://www.yinsiduanxin.com/china-phone-number/page/%s.html' % page  # 1~6页url
        print(f'第{page}页的网址为    {total_url}')
        r = requests.get(total_url, verify=False)  # 得到全部号码的列表
        phones = re.findall(r'data-clipboard-text="(.+?)" title', r.text)  # 匹配全部号码
        print(f'第{page}页的全部号码为  {phones}')

        for phone in phones:
            if phone not in exist_phone:
                now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 获取现在的时间
                now = datetime.datetime.strptime(now, '%Y-%m-%d %H:%M:%S')  # 将str格式转化时间格式
                url = 'https://www.yinsiduanxin.com/china-phone-number/verification-code-%s.html' % phone
                r = requests.get(url, verify=False)
                ago = re.findall(r'<td style="text-align: center">(.+?)</td>', r.text)[0]  # 得到最新获取短信的时间

                if len(ago) == 19:      # '2020-02-29 12:30:13'
                    ago = datetime.datetime.strptime(ago, '%Y-%m-%d %H:%M:%S')  # 将str格式转化时间格式

                elif len(ago) == 24:    # '2020-02-29T12:30:13.000Z'
                    ago = ago.replace('T', ' ').split('.')[0]
                    ago = datetime.datetime.strptime(ago, '%Y-%m-%d %H:%M:%S')  # 将str格式转化时间格式

                elif ago == '1 分钟前':  # 1 分钟前
                    return phone

                elif int(ago.split(' ')[0]) < 60 and ago.split(' ')[1] == '秒前':     # 60 秒前
                    return phone

                else:
                    print(f'{phone},这个号码获取时间长，换下一个')
                    continue

                sec = (now - ago).seconds  # 当前时间-最新获取短信的时间要少于60秒，不然会滞后
                if int(sec) < 60:
                    return phone
                    break
            else:
                continue
        else:
            continue
        break


def get_easy_phone():
    total_url = 'https://www.yinsiduanxin.com/china-phone-number/page/1.html'
    r = requests.get(total_url, verify=False)  # 得到全部号码的列表
    phones = re.findall(r'data-clipboard-text="(.+?)" title', r.text)  # 匹配全部号码
    print(f'可用全部号码为 {phones}')

    for phone in phones:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 获取现在的时间
        now = datetime.datetime.strptime(now, '%Y-%m-%d %H:%M:%S')  # 将str格式转化时间格式
        url = 'https://www.yinsiduanxin.com/china-phone-number/verification-code-%s.html' % phone
        r = requests.get(url, verify=False)
        ago = re.findall(r'<td style="text-align: center">(.+?)</td>', r.text)[0]  # 得到最新获取短信的时间
        # ago = datetime.datetime.strptime(ago, '%Y-%m-%d %H:%M:%S')

        if len(ago) == 19:      # '2020-02-29 12:30:13'
            ago = datetime.datetime.strptime(ago, '%Y-%m-%d %H:%M:%S')  # 将str格式转化时间格式

        elif len(ago) == 24:    # '2020-02-29T12:30:13.000Z'
            ago = ago.replace('T', ' ').split('.')[0]
            ago = datetime.datetime.strptime(ago, '%Y-%m-%d %H:%M:%S')  # 将str格式转化时间格式

        else:
            print('获取失败')

        sec = (now - ago).seconds  # 当前时间-最新获取短信的时间要少于60秒，不然会滞后
        if int(sec) < 60:
            return phone
            break


def get_code(phone):
    url = 'https://www.yinsiduanxin.com/china-phone-number/verification-code-%s.html' % phone
    r = requests.get(url, verify=False)
    code = re.findall(r'xxx(.+?)xxx', r.text)
    if code:
        return code
    else:
        return None


if __name__ == '__main__':
    file = last_report('../reports')
    send_mail(file)
