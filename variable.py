name = 'Jhon'
age = '70'
#  Here 70 acts as a string
print("There once was a man named " + name + ",")
print("He was " + age + " years old.")
print("He liked the name " + name + ",")
print("but disliked being " + age + " years old.")


# Typecasting
v = 30
v = int(v)
print(v + 1)

# Typecasting a function
def sum(a : int, b : int) -> int:
    return a + b
# here the function take only integer parameter and returns an integer
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
print("The sum of", x,"and", y,"is", sum(x, y))