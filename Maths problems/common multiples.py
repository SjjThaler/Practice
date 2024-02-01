
sumlist = []

n = 0

endthree = int(1000 / 3)
endfive = int(1000 / 5 - 1)

while n < endthree:
	n += 1
	sumlist.append(n*3)

n = 0

while n < endfive:
	n += 1
	if n*5 not in sumlist:
		sumlist.append(n*5)
		

print(sum(sumlist))


