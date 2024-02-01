fibonacci = [2,3]
fib = []

# Calculate fibonacci sequence up to four million

while fibonacci[-1] < 4000000:
	fibonacci.append(fibonacci[-1] + fibonacci[-2])

fibonacci.remove(fibonacci[-1])

print(fibonacci)

# Determine even fibonacci numbers

for i in fibonacci:
	if (int(str(i)[-1])) == 0:
		fib.append(i)
		
for i in fibonacci:
	if (int(str(i)[-1])) == 2:
		fib.append(i)
		
for i in fibonacci:
	if (int(str(i)[-1])) == 4:
		fib.append(i)
		
for i in fibonacci:
	if (int(str(i)[-1])) == 6:
		fib.append(i)
		
for i in fibonacci:
	if (int(str(i)[-1])) == 8:
		fib.append(i)

print(fib)

# Print even fibonacci sum

print(sum(fib))

