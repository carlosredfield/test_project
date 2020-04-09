from operaunit.operation_excel import OperationExcel
from operaunit.operation_json import OperationJson
from get_data.get_col import GetCol

class GetRunData():
	def __init__(self):
		self.opera_xls = OperationExcel()
		self.get_col = GetCol()

	def get_row_count(self):
		return self.opera_xls.GetRowCount()

	def get_run_url(self,row):
		col = self.get_col.get_url()
		return self.opera_xls.GetCellValue(row,col)

	def get_run_header(self,row):
		col = self.get_col.get_header()
		return self.opera_xls.GetCellValue(row,col)

	def get_run_is(self,row):
		col = self.get_col.get_run()
		res = self.opera_xls.GetCellValue(row,col)
		if res =='yes':
			return True


	def get_run_requests_way(self,row):
		col = self.get_col.get_requests_way()
		return self.opera_xls.GetCellValue(row,col)

	def get_run_header(self,row):
		col = self.get_col.get_header()
		return self.opera_xls.GetCellValue(row,col)
	
	def get_run_cookie(self,row):
		col = self.get_col.get_cookie()
		return self.opera_xls.GetCellValue(row,col)

	def get_run_case_depend(self,row):
		col = self.get_col.get_case_depend()
		is_dp = self.opera_xls.GetCellValue(row,col)
		if is_dp =='':
			return None
		else:
			return is_dp
	
	def get_run_data_depend(self,row):
		col = self.get_col.get_data_depend()
		return self.opera_xls.GetCellValue(row,col)

	def get_run_field_depend(self,row):
		col = self.get_col.get_field_depend()
		return self.opera_xls.GetCellValue(row,col)

	def get_run_data(self,row):
		col = self.get_col.get_data()
		res = self.opera_xls.GetCellValue(row,col)
		return res

	def get_run_headers_for_json(self,row):
		self.opera_json = OperationJson('../data/xxheader.json')
		return self.opera_json.GetData(self.get_run_header(row))

	def get_run_data_for_json(self,row):
		self.opera_json = OperationJson('../data/xxdatalogin.json')
		return self.opera_json.GetData(self.get_run_data(row))

	def get_run_expect(self,row):
		col = self.get_col.get_expect()
		return self.opera_xls.GetCellValue(row,col)

	def get_run_result(self,row):
		col = self.get_col.get_result()
		return self.opera_xls.GetCellValue(row,col)

	def write_result_data(self,row,data):
		col = col = self.get_col.get_result()
		return self.opera_xls.write_result(row,col,data)




if __name__=='__main__':
	x = GetRunData()
	print(x.get_id_col())
