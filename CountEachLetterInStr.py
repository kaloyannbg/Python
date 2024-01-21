#Exercise 12.4 Count how often each letter occurs in a string (case-insensitively). You can
#ignore every character that is not a letter. Print the letters with their counts, in order from
#highest count to lowest count.

#sentence = 'The quick brown fox jumps over 3 lazy dogs.'
sentence = 'Hello World'
sentList = []
numList = []
ignoreList = []

for char in sentence :
    if char.isalpha() :
        sentList.append(char.lower())
index = 0

for elem in sentList :
    if elem in ignoreList :
        continue
    else :
        index+=1
        ignoreList.append(elem)
        numList.append([elem, sentList.count(elem)])

numList.sort(key=lambda x: x[1], reverse=True)

for key, count in numList :
    print(key, ' = ' , count)

