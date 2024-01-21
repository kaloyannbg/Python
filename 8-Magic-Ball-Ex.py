import random
#Exercise 12.1 A magic 8-ball, when asked a question, provides a random answer from a
#list. The code below contains a list of possible answers. Create a magic 8-ball program that
#asks a question, then gives a random answer.
#exercise1201.py

answers = [ "It is certain", "It is decidedly so", "Without a \
doubt", "Yes, definitely", "You may rely on it", "As I see it, \
yes", "Most likely", "Outlook good", "Yes", "Signs point to yes",
"Reply hazy try again", "Ask again later", "Better not tell you \
now", "Cannot predict now", "Concentrate and ask again", "Don ' t \
count on it", "My reply is no", "My sources say no", "Outlook \
not so good", "Very doubtful" ]

userInp = ''
while True :
    userInp = input("[type 'e' and enter to exit]: Please ask something the magic ball: ")
    if userInp != 'e' :
        randomInteger = random.randint(0, len(answers)-1)
        print(randomInteger)
        print(answers[randomInteger])
    else :
        break

