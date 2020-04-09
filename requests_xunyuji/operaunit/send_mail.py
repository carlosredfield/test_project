import yagmail

class SendMail():

	def send_mail(self,passlist,faillist):
		rece_user = ['zjpcarlos1230@163.com']#,'380983372@qq.com','1185957403@qq.com']
		subject = '寻渔记项目接口自动化测试报告'
		pass_num = float(len(passlist))
		fail_num = float(len(faillist))
		count_num = pass_num+fail_num
		pass_percent = '%.2f%%' %(pass_num/count_num *100)
		fail_percent = '%.2f%%' %(fail_num/count_num *100)
		contents = ('本次测试共%s条用例，其中成功%s条，失败%s条，成功率为%s，失败率为%s' %(count_num,pass_num,fail_num,pass_percent,fail_percent))
		yag = yagmail.SMTP(user='zjpcarlos1230@163.com',password='163carlos1230',host='smtp.163.com')
		yag.send(rece_user,subject,contents,['../data/xxdata.xls'])

		#，成功率为%.2f%，失败率为%.2f%,,pass_percent,fail_percent