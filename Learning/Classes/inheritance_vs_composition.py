# Parent and component class
class Vehicle:
	def __init__(self, model, year, km):
		self.model = model
		self.year = year
		self.km = km
	def drive(self, rate_in_kmh):
		return f"{self.model} is driving at {rate_in_kmh} Kmh"

# Inheritance example

class Car(Vehicle):
	def __init__(self, model, year, km):
		super().__init__(model, year, km)
		self.wheels = 4

	def ident(self):
		return f"I'm a car with {self.wheels} wheels!"

bmw = Car("BMW", 1993, 100000)

	# Testing the parent function
print(bmw.drive(100))

	# Testing the child function
print(bmw.ident())

# Composition example

class Amphibious:
	def __init__(self, depth):
		self.obj1 = Vehicle("Gibbs Aquada", 2000, 5000)
		self.depth = depth

	def swim(self):
		return f"This {self.obj1.model} has already swum {self.obj1.km} kilometers!"

	def dive(self):
		return f"This {self.obj1.model} can dive a {self.depth} meters deep!"


watercar = Amphibious(100)
	
	# Testing the swim method which only accesses component class methods
print(watercar.swim())

	# Testing the dive method which also accesses the depth attribute of the composite classe
print(watercar.dive())



