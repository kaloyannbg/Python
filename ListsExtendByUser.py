#Exercise Write a program that asks the user to enter some data, for instance the names
#of their friends. When the user wants to stop providing inputs, he just presses Enter. The
#program then displays an alphabetically sorted list of the data items entered. Do not just
#print the list, but print each item separately, on a different line.

userInp = input('Please enter some names: ')
splitted = userInp.split()
splitted.sort()
for name in splitted :
    print(name)

listNames = []

while True :
    userInp = input('[separator = space, end = enter] Please enter some names: ')
    if(userInp == '') :
        break
    listNames.extend(userInp.split())
print(listNames)    
listNames.sort()
for name in listNames :
    print(name)
