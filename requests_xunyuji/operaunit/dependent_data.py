from get_data.get_run_data import GetRunData
from base.method import Method
from bs4 import BeautifulSoup 
from operaunit.operation_excel import OperationExcel
from operaunit.operation_json import OperationJson
import re
class DenpdentData():
	def __init__(self,caseid):
		self.caseid = caseid
		self.grdata = GetRunData()
		self.dpmethod = Method()
		self.opera_xls = OperationExcel()
 
	def run_dapent(self):
		dprow = self.opera_xls.get_depent_rows(self.caseid)
		opera_json = OperationJson('../data/xxcookies.json')
		cookie = opera_json.GetData("PHPSESSID")
		dpcookies = {"PHPSESSID":cookie}

		dpurl = self.grdata.get_run_url(dprow)
		dprequests_way = self.grdata.get_run_requests_way(dprow)
		dpheader = self.grdata.get_run_headers_for_json(dprow)
		# dpcookies = self.grdata.get_run_cookie(dprow)
		dpdata = self.grdata.get_run_data_for_json(dprow)
		print(dpcookies)

		dpres = self.dpmethod.MainWay(dprequests_way,dpurl,cookies=dpcookies,data=dpdata,headers=dpheader)
		return dpres.text

	def get_data_for_key(self,row):
		depend_data = self.grdata.get_run_data_depend(row)
		response_data = self.run_dapent()
		r = BeautifulSoup(response_data,"html.parser")
		dp_data = r.find_all('div',depend_data)[0].string
		dp_data = re.split(r' +',dp_data)[1]	#	寻渔记-日照铭万网络科技有限公司版权所有
		dp_data = dp_data.strip()
			#寻渔记-日照铭万网络科技有限公司版权所有       鲁公网安备 37110302000118号       鲁ICP备17003630号-1
		return dp_data