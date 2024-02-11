string = "Hello World"
slice = string [:5]
reverse = string [::-1]

print(string)
print(slice)
print(reverse)

numbers = "12345678910"

extract_every = numbers[::1]
halfreverse = numbers[5::-1]
upperhalf = numbers[5:11:1]

print(extract_every)
print(halfreverse)
print(upperhalf)

