arr = [1, 2, 5, 4, 7, 5, 4, 6, 8]
k = int(input("Which largest element do you want? ")) - 1
while(k > 0):
    highest_element = max(arr)
    high_times = arr.count(highest_element)
    for _ in range (0, high_times):
        arr.remove(highest_element)
    k -= 1
print(max(arr))