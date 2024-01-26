#Exercise The code block below contains a string that is a list of words, separated by
#commas. Build a dictionary that contains all these words as keys, and how often they
#occur as values. Then print the words with their quantities.
#listing1306.py
text = "apple,durian,banana,durian,apple,cherry ,cherry ,mango ," + \
"apple,apple,cherry,durian,banana,   apple,apple ,apple ," + \
"apple,banana,apple"
justWord = ''
wordList = []

for i in range(len(text)) :
    if text[i] == ',' :
        wordList.append(justWord.strip())
        justWord = ''
    elif i == (len(text)-1) :
        justWord+=text[i]
        wordList.append(justWord.strip())
    elif text[i] != ',' :
        justWord += text[i]

wordListAdded = []
wordDict = {}

for elem in wordList :
    if elem in wordListAdded :
        continue
    wordListAdded.append(elem)
    wordDict[elem] = wordList.count(elem)

print(wordDict)




