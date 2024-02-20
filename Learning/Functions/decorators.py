# A simple version of taking a function as the input of another function
def simpledecorator(func):
	print("Hello")
	func()

def inputfunc():
	print("World")

simpledecorator(inputfunc)

# A way to create a new function from two functions
def decorator(func):
	
	def wrapper():
		a_function()
		print("Now I've been decorated")

	return wrapper


dec_func = decorator(a_function)


dec_func()




