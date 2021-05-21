def num(num): #定义函数
	def num_in(nim_in): #定义函数
		return num + num_in #返回两个参数的和。
	return num_in #返回内部函数的引用。（变量名）

a = num(100) #将参数为100的函数num接收，并赋值给a，只不过这个返回值是一个函数的引用。等于 a = num_in，注意这里接收的不光是函数本身，还有已经传递的参数。
print(a)
#b = a(100) #调用函数a,即num_in，并传递一个参数100，返回值给b。