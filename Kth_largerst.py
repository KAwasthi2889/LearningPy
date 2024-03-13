arr = [1, 2, 5, 4, 7, 5, 4, 6, 8]
n = len(arr)
k = int(input("Which largest element do you want? ")) - 1
temp = []
for i in range (0, n):
    temp.append(arr[i])
while(k > 0):
    highest_element = max(temp)
    high_times = temp.count(highest_element)
    for _ in range (0, high_times):
        temp.remove(highest_element)
    k -= 1
print(max(temp))