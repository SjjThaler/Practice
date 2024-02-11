nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing an element in the nested list
x = nested_list[0][0]  
y = nested_list[1][2]
z = nested_list[2][2]

print(x,y,z)

# Trying out [::] on nested lists

reverse = nested_list[::-1]
double_reverse = nested_list[0][::-1]
full_reverse = nested_list[::-1][::-1]

print(reverse)  
print(double_reverse)

# Fully reversing both the list and the sublists doesn't
# seem to be possible this way
print(full_reverse)