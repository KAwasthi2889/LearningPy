# Sum of all the divisors except itself is equal to itself.
def perfect_num(limit):
    numbers = []
    for num in range(2, limit + 1):
        sum = 1 
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                sum += divisor + num / divisor
        if sum == num:
            numbers.append(num)
    return numbers
limit = 10000
print(perfect_num(limit))