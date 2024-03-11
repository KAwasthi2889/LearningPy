# Print the message n times
n = int(input("How many times do you want to print a?\n"))


# Specify data type as input is inherintly a string
print("a" * n)


# Absolute value and Rounding
r = -9
print(abs(r))
print(round(5.5))


# Largest and Smallest number
print(max(4, 8 ,3, 11, 9))
print(min(4, 8 ,3, 11, 9))


# integer division // gives floor of division
print(53 // 20) # 2.65
print (-53 // 20)
print (53 // -20)
print (-53 // -20)


# % gives the remainder to floor and sign of second oprend
print (53 % 20) # 13
print (-53 % 20)
print (53 % -20)
print (-53 % -20) # When booth are negative, ot takes celing of expression and sign of second operand


# ** raises the power
print (3 ** 2)
print (-3 ** 2) # -3 ** 2 is read same as -(3 ** 2)
print ((-3) ** 2)
print (3 ** -2) # Here -power converts 3 to 0.333
print (-3 ** -2)


# Assignment dosent change the output if not specified
difference = 20
double = 2 * difference
print(double)
difference = 5
print(double) # Now double is not 10 but 40 as before bcz double is not reassigned