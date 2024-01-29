#Define the Field class
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


#Define each field
f1 = Field(False, "-")
f2 = Field(False, "-")
f3 = Field(False, "-")
f4 = Field(False, "-")
f5 = Field(False, "-")
f6 = Field(False, "-")
f7 = Field(False, "-")
f8 = Field(False, "-")
f9 = Field(False, "-")


#Define winning condition and turn
victory = False
turn = False

#Main Loop
while victory == False:
	if turn == False:
		turn = True
		print("Spieler 1 gibt ein: ")
		x = input()
		if x == "f1":
			f1.black()
		if x == "f2":
			f2.black()
		if x == "f3":
			f3.black()
		if x == "f4":
			f4.black()
		if x == "f5":
			f5.black()
		if x == "f6":
			f6.black()
		if x == "f7":
			f7.black()
		if x == "f8":
			f8.black()
		if x == "f9":
			f9.black()

	if turn == True:
		turn = False
		print("Spieler 2 gibt ein: ")
		x = input()
		if x == "f1":
			f1.white()
		if x == "f2":
			f2.white()
		if x == "f3":
			f3.white()
		if x == "f4":
			f4.white()
		if x == "f5":
			f5.white()
		if x == "f6":
			f6.white()
		if x == "f7":
			f7.white()
		if x == "f8":
			f8.white()
		if x == "f9":
			f9.white()
		
	





input("Press any key to close the application.")