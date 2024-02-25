class parent:
	def __init__(self):
		self._prot = "protected variable"
		self.__priv = "private variable"

class child(parent):
	def __init__(self):
		super().__init__()

	def prot(self):
		print("Accessing " + self._prot)
	# __priv can't and shouldn't be accessed outside of parent as it's a private variable
	# Instead it has to be accessed through name mangling
	def priv(self):
		print("Accessing " + self._parent__priv)


obj1 = child()

obj2 = parent()

# Printing the class variables from the parent class
print(obj2._prot)

# Print(obj2.__priv) doesn't work, as the private variable has undergone name mangling
print(obj2._parent__priv)

# Printing the class variables through child methods
obj1.prot()
obj1.priv()




