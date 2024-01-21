#Exercise 12.3 A first-in-first-out (FIFO) structure, also called a “queue,” is a list
# that gets
#new elements added at the end, while elements from the front are removed and processed.
#Write a program that processes a queue. In a loop, ask the user for input. If the user just
#presses the Enter key, the program ends. If the user enters anything else, except for a
#single question mark (?), the program considers what the user entered a new element and
#appends it to the queue. If the user enters a single question mark, the program pops the
#first element from the queue and displays it. You have to take into account that the user
#might type a question mark even if the queue is empty
fifoList = []

while True :
    userInput = input('Please enter FIFO Element: ')
    if userInput == '' :
        break
    elif userInput == '?' and len(fifoList) > 0 :
        print(fifoList[0])
    elif userInput == '?' and len(fifoList) < 1 :
        print('The first element do not exist. Sorry try again')
    else :
        if(len(fifoList) < 1) :
            fifoList.append(userInput)
        else :
            fifoList.pop(0) #fifoList.remove(fifoList[0]) works too
            fifoList.append(userInput)
