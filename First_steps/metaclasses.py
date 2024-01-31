class Parent:
	def __init__(self, name, age):
		self.name = name
		self.age = age

p1 = Parent('Ben', 37)

class Child(Parent):
	pass

c1 = Child('Emilia', 1)

# Created by Child
print(type(c1))

# Created by Parent
print(type(p1))

# Supposedly created by a meta class
print(type(Parent))

# See also 3.3.3.1 in: 
# https://docs.python.org/3/reference/datamodel.html