# Testing whether num % 3 really evaluates to 'False'
def shortmodulo(num: int):
	return "False" if num % 3 else "True"

print(shortmodulo(9))

# Alternatively this works too
def longmodulo(num: int):
	return "False" if num % 3 != 0 else "True"

print(longmodulo(8))
print(longmodulo(9))