phrase1 = "SATI ATI"
phrase2 = "cse ece"
print(phrase1)
# Convert to uppercase
print(phrase2.upper())
# check if it is lowercase
print(phrase2.islower())
print(phrase2.upper().isupper())

# Gives the length
print(len(phrase1))
# Gives the specific letter through index
print(phrase1[2])
print(phrase1[:6]) # Slicing a string
# Find the index of a letter
print(phrase1.index("I")) 
# Replace a word
print(phrase2.replace("ece", "cec"))

# For loop in string
num = 60
res = ''
for i in str(num):
    res += str(int(i)**2)
print(int(res))

# len can also give the length of words
word = 'ABC'
print(len(word))

# Methods can be used in series
dna = 'ATCGAATTCCGG' # replace() will replace the letter
dna = dna.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()
print(dna)

a = 'String Work'
print(a.count('g')) # Count the number of times a letter is present
print(a.split()) # Spliting the elements to a list using split method
print(a) # The split method returns the list but dosent convert the variable

b = 'Atta'
print(b * 2) # Multiplication of strings repeats the string.
print(3 * b) # Order dosent matter here.
print(0 * b) # 0 gives empty string.
print(b * -2) # Negative also gives empty string.

print(a + b) # Concatenation (Addition of strings) joins them.
name = 'Jhon'
age = '70' # Here 70 acts as a string
print("There once was a man named " + name + ",")
print("He was " + age + " years old.")
print("He liked the name " + name + ",")
print("but disliked being " + age + " years old.")
# \' and \" give quotation mark without breaking the string quotations.
# \t gives tab, \b gives backspace, \\ gives a baclslash.
print('He said, "That' + "'s" + ' better."') # Use both quotation marks ("" '') together.
print('He said, "That\'s better."') # Another way to use both quotation marks ("" '') together.
# Use of comma can give auto spacing as it substitutes the variable instead of concatenation.
age = 70 # Now age is a number/integer.
print("There once was a man named", name, "\b,") # Can use \b to remove default spacing of comma.
print("He was", age, "years old.")
print("He liked the name", name, ",")
print("but disliked being", age, "years old.")

print(1, 2, 3) # Here comma gives space between them as it seperates each value.
print(1,2,3) # Same as above.
print(1,2,3, sep = '* ') # sep can stylise the use of comma.
print() # Only gives newline (\n).
print("Hello", end = '') # Removes the automatic newline.
print(" World")
