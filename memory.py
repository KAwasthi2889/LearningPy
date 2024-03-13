# id gives the memory address (identity) of a constant and functions
x = 4
print(id(4))
print(id(x))
print(id(print))
print(id(id))
# But larger numbers are floater point values and may not have same address
y = 3000000000
z = 3000000000
print(id(y))
print(id(z))