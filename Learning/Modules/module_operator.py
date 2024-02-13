from operator import mul 

def mult_two(x,y):
	return x * y

print(mult_two(1,2))

print(mul(5,5))
	
# Also remember that you will get this error message if you 
# name any file exactly like the module (here operator) in the same directory.

# ImportError: cannot import name '...' from partially initialized module '...' (most likely due to a circular import)
