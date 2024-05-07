# id gives the memory address (identity) of a constant and functions
x = 4
y = 4
print(id(4))
print(id(x))
print(id(y))
print(id(print))
print(id(id))
# But larger numbers are floater point values and may not have same address
y = 325555644444755555155555
z = 325555644444755555155555
print(id(y))
print(id(z))