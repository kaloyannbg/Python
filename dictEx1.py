

#Exercise The code below contains a list of words. Build a dictionary that contains all
#these words as keys, and their quantities as values. Print the words with their quantities.
#listing1305.py

wordlist = ["apple","durian","banana","durian","apple","cherry",
"cherry","mango","apple","apple","cherry","durian","banana",
"apple","apple","apple","apple","banana","apple"]

wordListAdded = []
wordDict = {}

for elem in wordlist :
    if elem in wordListAdded :
        continue
    wordListAdded.append(elem)
    wordDict[elem] = wordlist.count(elem)

print(wordDict)

