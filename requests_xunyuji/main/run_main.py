import sys
sys.path.append('d:/Atest_project/requests_xunyuji')
from base.method import Method
from get_data.get_run_data import GetRunData
from operaunit.operation_cookies import OperationCookies
from operaunit.operation_json import OperationJson
from operaunit.assertcontain import IsContain
from operaunit.dependent_data import DenpdentData
from operaunit.send_mail import SendMail
import json
class RunMain():
	def __init__(self):
		self.grd = GetRunData()
		self.method = Method()
		self.ascontain = IsContain()
		self.smail = SendMail()
	def GoOnRun(self):
		pass_count=[]
		fail_count=[]
		rows_count = self.grd.get_row_count()
		for i in range(1,rows_count):
			is_run = self.grd.get_run_is(i)
			if is_run:
				url = self.grd.get_run_url(i)
				requests_way = self.grd.get_run_requests_way(i)
				header = self.grd.get_run_headers_for_json(i)
				cookie = self.grd.get_run_cookie(i)
				data = self.grd.get_run_data_for_json(i)
				expect = self.grd.get_run_expect(i)
				caseid = self.grd.get_run_case_depend(i)
				depent_data = self.grd.get_run_data_depend(i)
				field_data = self.grd.get_run_field_depend(i)
				print('=======================================现在第%s行分割线======================================' %i)			

				if cookie =='write':
					res = self.method.MainWay(requests_way,url,headers=header)
					opera_cok = OperationCookies(res)
					opera_cok.write_cookies()
					print('==========写入成功==========')

				else: 
					opera_json = OperationJson('../data/xxcookies.json')
					cookie = opera_json.GetData("PHPSESSID")
					cookies = {"PHPSESSID":cookie}
						
					if caseid!=None:
						dp = DenpdentData(caseid)
						dp_data = dp.get_data_for_key(i)
						data[field_data]=dp_data
						print('1：%s,2.%s,3.%s,4.%s' %(caseid,depent_data,field_data,dp_data))
						print('='*80)
						print(data)
						res = self.method.MainWay(requests_way,url,cookies=cookies,data=data,headers=header).text
					else:
						res = self.method.MainWay(requests_way,url,cookies=cookies,data=data,headers=header).text
				
					if self.ascontain.is_contain(expect,res):
						print('pass')
						self.grd.write_result_data(i,'pass')
						pass_count.append(i)
					else:
						print('fail')
						self.grd.write_result_data(i,'fail')
						fail_count.append(i)

		self.smail.send_mail(pass_count,fail_count)




if __name__ == '__main__':
	x = RunMain()
	x.GoOnRun()