def square_digits(num):
    if (num == 0):
        return 0
    else:
        arr = []
        temp = num
        while (temp > 0):
            digit = temp % 10
            digit **= 2
            temp //= 10
            arr.append(digit)
        arr.reverse()
        result = ''
        n = len(arr)
        for i in range(0, n):
            result += str(arr[i])
        return int(result)
print(square_digits(91))
# 85 should give 6425 (64-25)