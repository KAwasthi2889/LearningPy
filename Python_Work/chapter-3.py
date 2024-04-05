# Following the function design recipe, define a function that has one parameter, a number, and returns that number tripled.
def triple(num):
    return num * 3
print(triple(8))

# Following the function design recipe, define a function that has two parameters, both of which are numbers, and returns the absolute value of the difference of the two.
def diff(num1, num2):
    return abs(num1 - num2)
print(diff(8, 2))
print(diff(2, 8))

# Following the function design recipe, define a function that has one parameter, a distance in kilometers, and returns the distance in miles.
def km_to_mile(num):
    return num / 1.6
print(km_to_mile(20))

# Following the function design recipe, define a function that has three parameters, grades between 0 and 100 inclusive, and returns the average of those grades.
def average(num1, num2, num3):
    if 0 <= num1 <= 100 and 0 <= num2 <= 100 and 0 <= num3 <= 100:
        return (num1 + num2 + num3) / 3
    else:
        return "INVALID! Please enter numbers between 1 to 100 only."
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))
print(average(num1, num2, num3))

# Following the function design recipe, define a function that has four parameters, all of them grades between 0 and 100 inclusive, and returns the average of the best 3 of those grades.
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
d = int(input("Enter 4th number: "))
temp = [a, b, c, d]
temp.remove(min(a, b, c, d))
print('The average of the best 3 numbers is', average(temp[0], temp[1], temp[2]))

def weeks_elapsed(day1: int, day2: int) -> int:
#(int, int) -> int
# day1 and day2 are days in the same year. Return the number of full weeks
# that have elapsed between the two days.
# >>> weeks_elapsed(3, 20)
# 2
# >>> weeks_elapsed(20, 3)
# 2
# >>> weeks_elapsed(8, 5)
# >>> weeks_elapsed(40, 61)
    return int(abs(day2 - day1) / 7)
print(weeks_elapsed(20, 3))

def square(num):
#(number) -> number
# Return the square of num.
# >>> square(3)
# 9
    return num * num
print(square(3))