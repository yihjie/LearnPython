#!/usr/bin/python3


'''
使用 class 來實現 switch 的功能
1. 創建一個 switch 的 class 繼承自 object
2. 定義一個 match 的function
3. 重寫 __iter__() function
4. 使用方法為使用 for ... in .... 來使用 switch class
'''

# switch class
class switch(object):
	def __init__(self, value):		# 初始化需要匹配的值 value
		self.value = value
		self.fall  = False		# 如果 case 內沒有break,則為 False

	def __iter__(self):
		yield self.match		# 調用match 返回一個 iteration
		raise StopIteration		# StopIteration 異常來判斷 for loop 是否結束

	def match(self, *args):			# 模擬 case 子句
		if self.fall or not args:	# 如果 fall = True 則繼續執行下面的case 或 case 沒有 break 則執行 default case
			return True
		elif self.value in args:	# match
			self.fall = True
			return True
		else:				# non-match
			return False	


# ----------------------------------------------------------------------------------------------------------------------------

#operator = ""  # not match
#operator = "+" # case('+')
operator = "%" # not match

x = 1
y = 2

for case in switch(operator):			# switch 只能用於 for in loop 
	if case('+'):
		print(x + y)
		break
	if case('-'):
		print(x - y)
		break
	if case('*'):
		print(x * y)
		break
	if case('/'):
		print(x / y)
		break
	if case('%'):
		print(x % y)
	if case():
		print("not match")
