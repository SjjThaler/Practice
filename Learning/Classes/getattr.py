class animal:
	def __init__(self, species, age):
		self.species = species
		self.age = age

Justus = animal("dog", 10)
Mausi = animal("cat", 15)

print(getattr(Justus,'species'))
print(getattr(Mausi, 'age'))

combage = getattr(Justus,'age') + getattr(Mausi,'age')

print(combage)

def vetcheck(animal):
	if getattr(animal, 'age') > 10:
		print("The animal should get checked by a veternarian.")

vetcheck(Justus)
vetcheck(Mausi)