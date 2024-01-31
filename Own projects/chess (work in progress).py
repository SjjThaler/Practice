# Define parent class

class piece:
	def __init__(self, kind, x, y, color):
		self.kind = kind
		self.x = x
		self.y = y
		self.color = color

	def positioncall(self):
		abc = self.x

		if self.x == 1:
			abc = "a"
		if self.x == 2:
			abc = "b"
		if self.x == 3:
			abc = "c"
		if self.x == 4:
			abc = "d"
		if self.x == 5:
			abc = "e"
		if self.x == 6:
			abc = "f"
		if self.x == 7:
			abc = "g"
		if self.x == 8:
			abc = "h"
		print("Die Figur befindet sich auf:", abc + str(self.y))
		
# Define inherited pawn child class

class pawns(piece):

	#def doppelsprung
	#def pawnattack

	def pawnmove(self):
		self.x = xachse
		self.y = int(yachse) 

	def pawnattack(self):
		self.x = self.x + 1
		self.y = self.y + 1


# Instantiate white pawns
p9 = pawns ("P", 1, 2, 0)
p10 = pawns("P", 2, 2, 0)
p11 = pawns("P", 3, 2, 0)
p12 = pawns("P", 4, 2, 0)
p13 = pawns("P", 5, 2, 0)
p14 = pawns("P", 6, 2, 0)
p15 = pawns("P", 7, 2, 0)
p16 = pawns("P", 8, 2, 0)

# Instantiate black pawns
p25 = pawns("P", 1, 7, 1)
p26 = pawns("P", 2, 7, 1)
p27 = pawns("P", 3, 7, 1)
p28 = pawns("P", 4, 7, 1)
p29 = pawns("P", 5, 7, 1)
p30 = pawns("P", 6, 7, 1)
p31 = pawns("P", 7, 7, 1)
p32 = pawns("P", 8, 8, 1)


#White pieces
p1 = piece("R", 1, 1, 0)
p2 = piece("N", 2, 1, 0)
p3 = piece("B", 3, 1, 0)
p4 = piece("Q", 4, 1, 0)
p5 = piece("K", 5, 1, 0)
p6 = piece("B", 6, 1, 0)
p7 = piece("N", 7, 1, 0)
p8 = piece("R", 8, 1, 0)



#Black pieces
p17 = piece("R", 1, 8, 1)
p18 = piece("N", 2, 8, 1)
p19 = piece("B", 3, 8, 1)
p20 = piece("Q", 4, 8, 1)
p21 = piece("K", 5, 8, 1)
p22 = piece("B", 6, 8, 1)
p23 = piece("N", 7, 8, 1)
p24 = piece("R", 8, 8, 1)



p18.x = 3
p18.y = 6 

p18.positioncall()



# Defining piece check function


# Main loop variables
turn = True

# Game loop
while turn == True:
	xachse = input("Gib die X-Achse ein.")
	if xachse == "a":
		xachse = 1
	if xachse == "b":
		xachse = 2
	if xachse == "c":
		xachse = 3
	if xachse == "d":
		xachse = 4
	if xachse == "e":
		xachse = 5
	if xachse == "f":
		xachse = 6
	if xachse == "g":
		xachse = 7
	if xachse == "h":
		xachse = 8

	yachse = input("Gib die Y-Achse ein.")

	# Work in progress: need to research how to access instance variables of class instances, i.e. how to check which piece
	# is on a particular position

	print(getattr(self, xachse, yachse))


input("Drücke eine beliebe Taste, um das Programm zu beenden.")

