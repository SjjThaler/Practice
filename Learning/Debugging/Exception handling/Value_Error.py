# Example 1: Raising a ValueError with a custom message
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

# Example 2: Raising a ValueError without a custom message
def check_age(age):
    if age < 0 or age > 120:
        raise ValueError("Invalid age")

# Using the functions
try:
    result = divide(10, 0)
except ValueError as e:
    print("Error:", e)

try:
    check_age(150)
except ValueError as e:
    print("Error:", e)

# This crashes the program
check_age(150)