x = 5
pr = [2, 3, 5]
err = []

end = 10000

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


# Checking for largest prime factor of large

large = 600851475143
pf = []

for i in pr:
	if large % i == 0:
		pf.append(i)

print(pf)

