# Absolute value
r = -9
print(abs(r))


# Rounding value
print(round(5.5))
print(round(45.9632541, 3)) # Rounds to 3rd decimal digit


# Largest and Smallest number
print(max(4, 8 ,3, 11, 9))
print(min(4, 8 ,3, 11, 9))


# integer division // gives floor of division
print(53 // 20) # 2.65
print (-53 // 20)
print (53 // -20) # Negative second operator makes it take the ceiling of the expression 
print (-53 // -20)


# % gives the remainder to floor and sign of second oprend
print (53 % 20) # 13
print (-53 % 20) 
print (53 % -20)
print (-53 % -20) # When second operand is negative, it takes celing of expression.


# ** raises the power like pow
print (3 ** 2)
print (-3 ** 2) # -3 ** 2 is read same as -(3 ** 2)
print ((-3) ** 2)
print (3 ** -2) # Here -power converts 3 to 0.333
print (-3 ** -2)
print(pow( -2, 4)) # But pow evaluates like (-2)**4
print(pow(6, 2, 3)) # Evaluates like 6**2 and then % 3


# Assignment dosent change the output if not specified
difference = 20
double = 2 * difference
print(double)
difference = 5
print(double) # Now double is not 10 but 40 as before bcz double is not reassigned


# Assignment operator works after expression on right is evaluated
d = 5
d *= 2+3
print(d)

# Typecasting
v = 30
v = int(v)
print(v + 1)

# Typecasting a function
def sum(a : float, b : float) -> int: # Here :<type> and -> <type> is for programmers to error check.
    return int(a + b)
# Here the function take only integer parameter and returns an integer
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
print("The sum of", x,"and", y,"in integer is", sum(x, y))
# Typecasting before and after can lead to varrying results, try 25.8 and 25.9
x1, y1 = int(x), int(y)
print("The sum of", x,"and", y,"in integer is", sum(x1, y1)) 

