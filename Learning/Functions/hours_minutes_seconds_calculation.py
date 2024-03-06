# Using divmod to calculate hours, minutes and seconds
def x(sec):
	h, hrest = divmod(sec, 3600)
	m, mrest = divmod(hrest, 60)
	return h, m, mrest

# Then return three values and assign them to three variables in one line
hours, minutes, seconds = x(5000)
print(hours, "h", minutes, "min", seconds, "sec")