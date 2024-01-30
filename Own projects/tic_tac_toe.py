#Define the Field class and player methods
class Field:
	def __init__(self, value, color):
		self.value = value
		self.color = color

	def black(self):
		if self.value == False:
			self.color = "x"
			print(f1.color,f2.color,f3.color)
			print(f4.color,f5.color,f6.color)
			print(f7.color,f8.color,f9.color)
		if self.value == True:
			global turn
			turn = "a"
			print("Field is already taken.")

	def white(self):
		if self.value == False:
			self.color = "0"
			print(f1.color,f2.color,f3.color)
			print(f4.color,f5.color,f6.color)
			print(f7.color,f8.color,f9.color)
		if self.value == True:
			global turn
			turn = "b"
			print("Field is already taken.")
			


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


#Define winning and turn variable
victory = False
turn = "a"


#Main Loop
while victory == False:
	#Black turn
	if turn == "a":
		turn = "b"
		print("Spieler 1 gibt ein: ")
		x = input()
		if x == "f1":
			f1.black()
			f1.value = True
			
		if x == "f2":
			f2.black()
			f2.value = True
			
		if x == "f3":
			f3.black()
			f3.value = True
			
		if x == "f4":
			f4.black()
			f4.value = True
			
		if x == "f5":
			f5.black()
			f5.value = True
			
		if x == "f6":
			f6.black()
			f6.value = True
			
		if x == "f7":
			f7.black()
			f7.value = True
			
		if x == "f8":
			f8.black()
			f8.value = True
		
		if x == "f9":
			f9.black()
			f8.value = True

	#Black winning conditions
	if f1.color == "x" and f2.color == "x" and f3.color == "x":
			victory = True
			break
	if f4.color == "x" and f5.color == "x" and f6.color == "x":
			victory = True
			break
	if f7.color == "x" and f8.color == "x" and f9.color == "x":
			victory = True
			break
	if f1.color == "x" and f4.color == "x" and f7.color == "x":
			victory = True
			break
	if f2.color == "x" and f5.color == "x" and f8.color == "x":
			victory = True
			break
	if f3.color == "x" and f6.color == "x" and f9.color == "x":
			victory = True
			break
	if f1.color == "x" and f5.color == "x" and f9.color == "x":
			victory = True
			break
	if f3.color == "x" and f5.color == "x" and f7.color == "x":
			victory = True
			break

	#White turn		
	if turn == "b":
		turn = "a"

		print("Spieler 2 gibt ein: ")
		x = input()
		if x == "f1":
			f1.white()
			f1.value = True
			
		if x == "f2":
			f2.white()
			f2.value = True
			
		if x == "f3":
			f3.white()
			f3.value = True
			
		if x == "f4":
			f4.white()
			f4.value = True
			
		if x == "f5":
			f5.white()
			f5.value = True
			
		if x == "f6":
			f6.white()
			f6.value = True
			
		if x == "f7":
			f7.white()
			f7.value = True
			
		if x == "f8":
			f8.white()
			f8.value = True
			
		if x == "f9":
			f9.white()
			f9.value = True
			

	#White winning conditions
	if f1.color == "0" and f2.color == "0" and f3.color == "0":
			victory = True
			
	if f4.color == "0" and f5.color == "0" and f6.color == "0":
			victory = True
			
	if f7.color == "0" and f8.color == "0" and f9.color == "0":
			victory = True
			
	if f1.color == "0" and f4.color == "0" and f7.color == "0":
			victory = True
			
	if f2.color == "0" and f5.color == "0" and f8.color == "0":
			victory = True
			
	if f3.color == "0" and f6.color == "0" and f9.color == "0":
			victory = True
			
	if f1.color == "0" and f5.color == "0" and f9.color == "0":
			victory = True
			
	if f3.color == "0" and f5.color == "0" and f7.color == "0":
			victory = True
			

		
if victory == True:
	print("Somebody won?!")

input("Press any key to close the application.")