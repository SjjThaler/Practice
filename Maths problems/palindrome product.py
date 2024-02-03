x = 999
y = 999
pal = False
largepal = set()

def palindrome():
	z = str(x*y)
	if z[-1] == z[0] and z[-2] == z[1] and z[-3] == z[2]:
		global pal
		pal = True
		global largepal
		largepal.add(z)


while y > 800:
	x -= 1
	palindrome()
	if x == 900:
		y -= 1
		x = 999

print("The largest palindrome is:", max(largepal))
