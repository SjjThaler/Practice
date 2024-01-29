x = 5
pr = [2, 3, 5]
err = []

end = int(input("Up to which number should I check for prime numbers: "))

# First approximation
while x < end:
	x += 1
	if x % 2 == 0:
		continue
	if x % 3 == 0: 
		continue
	if x % 5 == 0: 
		continue
	else:
		pr.append(x)
		for i in pr:
			err.append(i*pr[-1])


# Cleaning up mistakes
pr_flip = list(reversed(pr))

for i in pr_flip:
	if i in err:
		pr.remove(i)

print(pr)

print("You have calculated", len(pr), "prime numbers.")
input("Press any key to exit the program.")

