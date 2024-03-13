def duplicate_encode(word):
    temp = []
    for i in word:
        temp.append(i)
    for i in word: 
        if (word.count(i) > 1):
            temp[temp.index(i)] = '('
        else:
            temp[temp.index(i)] = ')'
    
    print(temp)
duplicate_encode('ABBCCC') 