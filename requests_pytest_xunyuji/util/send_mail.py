import yagmail
from util.get_data import yaml_data


def send_mail():
    data = yaml_data(send_mail)
    send_user = data['send_user']
    password = data['password']
    subject = data['subject']
    rece_user = data['rece_user']
    subject = data['subject']
    contents = data['contents']
    host = data['host']

    yag = yagmail.SMTP(user=send_user, password=password, host=host)
    yag.send(rece_user, subject, contents, ['../data/xxdata.xls'])

    #，成功率为%.2f%，失败率为%.2f%,,pass_percent,fail_percent
