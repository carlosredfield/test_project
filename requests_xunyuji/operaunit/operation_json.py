import json

class OperationJson():
	def __init__(self,filename):
		self.filename = filename
		self.data = self.ReadData()

	def ReadData(self):
		with open(self.filename) as fp:
			data = json.load(fp)
			return data

	def GetData(self,name):
		if name == '':
			return None
		else:
			return self.data[name]

	def write_cookies_data(self,data):
		with open('../data/xxcookies.json','w') as fp:
			fp.write(json.dumps(data))

if __name__=='__main__':
	opera_json = OperationJson('../data/xxdatalogin.json')
	print(opera_json.GetData("login001"))
	print("="*100)
	opera_json = OperationJson('../data/xxheader.json')
	print(opera_json.GetData("headers"))
	print("="*100)
	
