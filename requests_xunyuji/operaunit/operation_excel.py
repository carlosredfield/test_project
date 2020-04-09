import xlrd
from xlutils.copy import copy

class OperationExcel():
	def __init__(self,filename=None,sheetid=None):
		if filename:
			self.filename = filename
			self.sheetid = sheetid
		else:
			self.filename = '../data/xxdata.xls'
			#self.filename = 'D:/django_restful/xunyuji_interface/data/xxdata.xls'
			self.sheetid = 0
		
		self.data = self.GetData()


	def GetData(self):
		data = xlrd.open_workbook(self.filename)
		table = data.sheets()[self.sheetid]
		return table

	def GetRowCount(self):
		table = self.data
		return table.nrows

	def GetCellValue(self,row,col):
		table = self.data
		return table.cell_value(row,col)

	def write_result(self,row,col,data):
		
		read_data = xlrd.open_workbook(self.filename)
		write_data = copy(read_data)
		sheet_data = write_data.get_sheet(0)
		sheet_data.write(row,col,data)
		write_data.save(self.filename)


#==============以下为数据依赖方法==========================
	def get_depent_data(self,caseid):
		depents_row = self.get_depent_rows(caseid)
		depent_data = self.get_depent_row_values(self,depents_row)
		return depent_data

	def get_depent_rows(self,caseid):
		num = 0
		cols = self.get_id_col()
		for col in cols:
			if col ==caseid:
				return num
			num = num + 1

	def get_depent_row_values(self,row):
		return self.data.row_values(depents_row)

	def get_id_col(self,colid=None):
		if colid!=None:
			col_data = self.data.col_values(colid)
		else:
			col_data = self.data.col_values(0)
		return col_data

if __name__=='__main__':
	opera_xls = OperationExcel()
	print(opera_xls.GetRowCount())
	print(opera_xls.GetCellValue(1,1))
	print(opera_xls)