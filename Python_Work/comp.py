print(True and not False)
print(True or True and False)
print(True or True and False)
print(True and not False)
print(not True or not False)
print(True and not False)
print(True and not 0)
print(True and not False)
print(52 < 52.3)
print(True and not False)
print(1 + 52 <  52.3)
print(True and not False)
print(4 != 4.0)


x = True
y = True
# True iff both variables are True
print(x and y)
# True iff x is False
print(not x)
# True if atleast one of the variable is True
print(x or y)

# True iff atmost one of the variable is True
full = True
empty = False
print(not full or not empty)

# True if a and b refer to different values and should return False otherwise
a = 20
b = 19
print(a != b)

pop = 15000000
area = 2000000
# Write an if statement that will print the population if it is less than 10,000,000
if(pop < 10000000):
    print(pop)
# Write an if statement that will print the population if it is between 10,000,000 and 35,000,000
if(pop >= 10000000 and pop <= 35000000):
    print(pop)
# Write an if statement that will print “Densely populated” if the land density is greater than 100, and “Sparsely populated” otherwise.
if(pop/area >= 100):
    print("Densly populated")
else:
    print("Sparsely populated")