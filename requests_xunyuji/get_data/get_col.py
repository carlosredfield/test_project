class GetCol():
	idnum = 0
	requests_name = 1
	url = 2
	run = 3
	requests_way = 4
	header = 5
	cookie = 6
	case_depend = 7
	data_depend = 8
	field_depend = 9
	data = 10
	expect = 11
	result = 12

	def get_id(self):
		return self.idnum
	def get_url(self):
	    return self.url
	def get_run(self):
	    return self.run
	def get_requests_way(self):
	    return self.requests_way
	def get_header(self):
	    return self.header
	def get_cookie(self):
		return self.cookie
	def get_case_depend(self):
	    return self.case_depend
	def get_data_depend(self):
	    return self.data_depend
	def get_field_depend(self):
	    return self.field_depend
	def get_data(self):
	    return self.data
	def get_expect(self):
	    return self.expect
	def get_result(self):
	    return self.result


if __name__ == '__main__':
	x = GetCol()
	print(x.get_requests_way())