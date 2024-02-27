# Convert Celsius to Fahrenheit
C = 32
print( "F = " + str(9*C/5 + 32))
# Here str is used as integer can't be added with string so we convert the integer to string

# Anothe way to do it
# Convert Fahrenheit to Celsius
F = 32
print("C =", (F-32)*5/9)

# Remove \n that is automaticaly at end of print
F = 32
print("C =", end='')
print((F-32)*5/9)
