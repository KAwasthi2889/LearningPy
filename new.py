def duplicate_encode(word):
    arr = []
    temp = ''
    for i in word.lower():
        arr.append(i)
    for i in range(len(word)):
        if word.count(word[i]) > 1:
            arr[i] = ')'
        else:
            arr[i] = '('
    for k in range (0, len(arr)):
        temp += arr[k]  
    return temp
print(duplicate_encode('HGSv R NR )A'))
