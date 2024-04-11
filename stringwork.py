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