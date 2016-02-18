class TestMetaClass(type):
	def __new__(cls, name, base, attrs):
		if name=='Test':
			print('current cls is : ', cls)
			print('current name is : %s' % name)
			return type.__new__(cls, name, base, attrs)
		print("current cls is : ", cls)
		print('current name is : %s' % name)
		return type.__new__(cls, name, base, attrs)

class Test(object, metaclass=TestMetaClass):
	def __init__(self):
		print("this is Test")

class User(Test):
	def __init__(self):
		print("this is User")

user = User()
