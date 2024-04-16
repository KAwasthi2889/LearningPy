'''What value does each of the following expressions evaluate to? Verify your
answers by typing the expressions into the Python shell.
a. 'Computer' + ' Science'
b. 'Darwin\'s'
c. 'H2O' * 3
d. 'CO2' * 0
'''
print('Computer' + ' Science') # ComputerScience
print('Darwin\'s') # Darwin's
print('H2O' * 3) # H2OH2OH2O
print('CO2' * 0) # <empty>



'''Express each of the following phrases as Python strings using the
appropriate type of quotation marks (single, double, or triple) and, if
necessary, escape sequences. There is more than one correct answer for
each of these phrases.
a. They'll hibernate during the winter.
b. “Absolutely not,” he said.
c. “He said, 'Absolutely not,’” recalled Mel.
d. hydrogen sulfide
e. left\right
'''
print("They'll hibernate during the winter.")
print('"Absolutely not," he said.')
print('"He said, \'Absolutely not,\'" recalled Mel.')
print('hydrogen sulfide')
print('left\\right')



# Rewrite the following string using single or double quotes instead of triple
# quotes:
# '''A
# B
# C'''
print('"A\nB\nC"')



# Use built-in function len to find the length of the empty string.
print(len(''))



'''Given variables x and y, which refer to values 3 and 12.5, respectively, use
function print to print the following messages. When numbers appear in
the messages, variables x and y should be used.
a. The rabbit is 3.
b. The rabbit is 3 years old.
c. 12.5 is average.
d. 12.5 * 3
e. 12.5 * 3 is 37.5.
'''
x = 3
y = 12.5
print('The rabbit is', x, '.')
print('The rabbit is', x, 'years old.')
print(y, 'is average.')
print(y,'*', x)
print(y, '*', x, 'is 37.5.')



'''Consider this code:
>>> first = 'John'
>>> last = 'Doe'
>>> print(last + ', ' + first)
What is printed by this code?
''' # Doe, Jhon
first = 'John'
last = 'Doe'
print(last + ', ' + first)



'''Use input to prompt the user for a number, store the number entered as
a float in a variable named num, and then print the contents of num.
'''
# num = float(input('Enter a number: '))
# print(num)



'''Complete the examples in the docstring and then write the body of the
following function:
def repeat(s: str, n: int) -> str:
# Return s repeated n times; if n is negative, return the empty string.
>>> repeat('yes', 4)
'yesyesyesyes'
>>> repeat('no', 0)
>>> repeat('no', -2)
>>> repeat('yesnomaybe', 3)
'''
def repeat(s: str, n: int) -> str:
    return s * n
print(repeat('yes', 4))
print(repeat('no', 0), end = '')
print(repeat('no', -2), end = '')
print(repeat('yesnomaybe', 3))



'''Complete the examples in the docstring and then write the body of the
following function:
def total_length(s1: str, s2: str) -> int:
Return the sum of the lengths of s1 and s2.
>>> total_length('yes', 'no')
5
>>> total_length('yes', '')
>>> total_length('YES!!!!', 'Noooooo')
'''
def total_length(s1: str, s2: str) -> int:
    return len(s1 + s2)
print(total_length('yes', 'no'))
print(total_length('yes', ''))
print(total_length('YES!!!!', 'Noooooo'))