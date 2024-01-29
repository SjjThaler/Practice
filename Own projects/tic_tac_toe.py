class Field:
	def __init__(self, value, color):
		self.value = value
		self.color = color

	def black(self):
		self.color = "x"
		print(f1.color,f2.color,f3.color)
		print(f4.color,f5.color,f6.color)
		print(f7.color,f8.color,f9.color)

	def white(self):
		self.color = "0"
		print(f1.color,f2.color,f3.color)
		print(f4.color,f5.color,f6.color)
		print(f7.color,f8.color,f9.color)


f1 = Field(False, "-")
f2 = Field(False, "-")
f3 = Field(False, "-")
f4 = Field(False, "-")
f5 = Field(False, "-")
f6 = Field(False, "-")
f7 = Field(False, "-")
f8 = Field(False, "-")
f9 = Field(False, "-")



f1.white()


input("Press any key to close the application.")