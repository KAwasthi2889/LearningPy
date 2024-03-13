# Question 1
kingdoms = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']
print(kingdoms)
print(kingdoms[0])
print(kingdoms[5])
print(kingdoms[0:3])
print(kingdoms[2:5])
print(kingdoms[4:])
kingdoms.clear()
print(kingdoms)

print('\n\n')

# Question 2
kingdoms = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']
print(kingdoms[-6])
print(kingdoms[-1])
print(kingdoms[-6:-3])
print(kingdoms[-4:-1])
print(kingdoms[-2:])
kingdoms.clear()
print(kingdoms)

print('\n\n')

# Question 3
appointments = ['9:00', '10:30', '14:00', '15:00', '15:30']
print(appointments)
appointments.append('16:30')
print(appointments)
appointments = appointments + ['16:30']
print(appointments)
print('+ operator creates new list')

print('\n\n')

# Question 4
ids = [4353, 2314, 2956, 3382, 9362, 3900]
print(ids)
ids.remove(3382)
print(ids)
ids.insert(4, 4499)
print(ids)
lis = [5566, 1830]
ids.extend(lis)
print(ids)
ids.reverse()
print(ids)
print(sorted(ids))

print('\n\n')

# Question 5
alkaline_earth_metals = [['beryllium', 4], ['magnesium', 12], ['calcium', 20], ['strontium', 38], ['barium', 56], ['radium', 88]] 
print(alkaline_earth_metals[5])
print(alkaline_earth_metals[-1])
print(len(alkaline_earth_metals))
temp = []
for i in range (0 , 6):
    temp.append(alkaline_earth_metals[i][1])
print(alkaline_earth_metals[temp.index(max(temp))])

print('\n\n')

# Question 6
temps = [25.2, 16.8, 31.4, 23.9, 28, 22.5, 19.6]
print(temps)
temps.sort()
print(temps)
cool_temps = temps[0:2]
warm_temps = temps[2:]
print(cool_temps)
print(warm_temps)
temps_in_celsius = cool_temps + warm_temps
print(temps_in_celsius)

print('\n\n')

# Question 7
def same_first_last(L: list) -> bool:
    if(len(L) >= 2) and (L[0] == L[-1]):
        return True
    return False
print(same_first_last([3, 4, 2, 8, 3]))
print(same_first_last(['apple', 'banana', 'pear']))
print(same_first_last([4.0, 4.5]))


print('\n\n')

# Question 8
def is_longer(L1: list, L2: list) -> bool:
    if(len(L1) > len(L2)):
        return True
    return False
print(is_longer([1, 2, 3], [4, 5]))
print(is_longer(['abcdef'], ['ab', 'cd', 'ef']))
print(is_longer(['a', 'b', 'c'], [1, 2, 3]))


print('\n\n')

# Question 10
units = [['km', 'miles', 'league'], ['kg', 'pound', 'stone']]
print(units[0][0])
print(units[1][2])
print(units[0][0])
print(units[1][0])
print(units[0][1:])
print(units[1][0:2])

print('\n\n')

# Question 11
units = [['km', 'miles', 'league'], ['kg', 'pound', 'stone']]
print(units[-2][-3])
print(units[-1][-3])
print(units[-2][-3])
print(units[-1][-3])
print(units[-2][-2:])
print(units[-1][-3:-1])


