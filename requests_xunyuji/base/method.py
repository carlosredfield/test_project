import requests

class Method():

	def GetWay(self,url,params=None,headers=None,cookies=None):
		res = requests.get(url=url,params=params,headers=headers,cookies=cookies,verify=False)
		return res

	def PostWay(self,url,data=None,headers=None,cookies=None):
		res = requests.post(url=url,data=data,headers=headers,cookies=cookies,verify=False)
		return res

	def MainWay(self,method,url,data=None,headers=None,cookies=None):
		if method =='get':
			res = self.GetWay(url,data,headers,cookies)

		else:
			res = self.PostWay(url,data,headers,cookies)

		return res

if __name__ == '__main__':
	url = 'https://www.rzmwzc.com/Shop/add_car'
	requests_way = 'post'
	header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0', 'Accept-Encoding': 'gzip, deflate, br', 'Connection': 'keep-alive', 'Referer': 'https://www.rzmwzc.com/', 'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'}
	data = {'num': 1, 'gid': 14, '__hash__': 'e69a1ff15e43aa74dd9f564d66c10868_be92ff3ff4160057c5083977318a64e9'}
	x = Method()
	res = x.MainWay(requests_way,url,data=data,headers=header)
	print(res.text)

	# url = 'https://www.rzmwzc.com/member/common/actlogin'
	# data = {
	# 		"sUserName":"13590323747","sPassword":"xycarlos1230"
	# 		}
	# requests_way = 'post'
	# header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0', 'Connection': 'keep-alive', 'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2', 'Referer': 'https://www.rzmwzc.com/', 'Accept-Encoding': 'gzip, deflate, br'}
	# x = Method()
	# res = x.MainWay(requests_way,url,data=data,headers=header)
	# print(res.text)
	# print(res.status_code)