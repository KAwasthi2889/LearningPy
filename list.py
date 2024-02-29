arr = ['Abc', 'Def', 'Ghi', 'Jkl', 'Mno', 'Pqr', 'Stu', 'Vw', 'Xyz']
lis = [11, 22, 33, 44, 55, 66, 77, 88, 99]
# Append adds another element to list
arr.append('Xyz')
# Print everything from list
print(arr)
# Count the number of times
print(arr.count('Xyz'))
# Insert element in front of index number
lis.insert(0, 00)
print(lis)
# Remove element
arr.remove('Xyz') # by name
arr.pop() # last element
arr.pop(6) # with index

# Extend function adds the elements of list
lis.extend(arr)
print(lis)
# Range of index dosent include last range element
print(arr[1:6])

# Replace the element
lis[0] = "num"
print(lis)

# Clear list
lis.clear()
print(lis)
