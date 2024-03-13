phrase1 = "SATI ATI"
phrase2 = "cse ece"
print(phrase1)
# Convert to uppercase
print(phrase2.upper())
# check if it is lowercase
print(phrase2.islower())
print(phrase2.upper().isupper())

# Gives the lenght
print(len(phrase1))
# Gives the specific letter through index
print(phrase1[2])
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
