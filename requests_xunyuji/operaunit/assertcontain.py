class IsContain():
	def is_contain(self,str_one,str_two):
		falg = None
		if str_one in str_two:
			falg = True
		else:
			falg = False
		return falg