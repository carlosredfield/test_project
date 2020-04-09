import requests
from operaunit.operation_json import OperationJson
class OperationCookies():
	def __init__(self,response):
		self.response = response

	def get_cookies(self):
		cookies = self.response.cookies
		return cookies

	def write_cookies(self):
		cookies = requests.utils.dict_from_cookiejar(self.get_cookies())
		self.opera_json = OperationJson('../data/xxcookies.json')
		self.opera_json.write_cookies_data(cookies)

if __name__ == '__main__':
	url = 'https://www.rzmwzc.com/'
	res = requests.get(url)

	x = OperationCookies(res)
	x.write_cookies()
	print(x.get_cookies())