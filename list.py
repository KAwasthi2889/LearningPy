arr = ['Abc', 'Def', 'Ghi', 'Jkl', 'Mno', 'Pqr', 'Stu', 'Vw', 'Xyz']
lis = [11, 22, 33, 44, 55, 66, 77, 88, 99]
# Append adds another element to list
arr.append('Xyz')
# Print everything from list
print(arr)
# Gives the lenght
print(len(arr))
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
# Slicing of index dosent include last range element
print(arr[1:6])

# Replace the element
lis[0] = "num"
print(lis)

# Clear list
lis.clear()
print(lis)

# Sorting the list
lis = [11, 22, 23, 94, 85, 26, 17, 48, 9]
print(sorted(lis)) # Using sorted function returns sorted list but dosent change the list itself
print(lis)
lis.sort() # Sort method sorts the list itself but returns None
print(lis)

'''lists are mutable, i.e., like pointers any change in one can do the change in another.
This is because lists share the same memory address when assigned to eachother.'''

lis = [11, 22, 23, 94, 85, 26, 17, 48, 9]
lis2 = lis
lis2[0] = 12
print(lis) # Change in lis2 also updates lis as it's mutable
print(lis.index(94)) # Finds the index of element
lis.reverse() # Reverses the list but returns None
print(lis)
print(lis[-1::-1]) # Printing the list in reverce through negative indexing.



