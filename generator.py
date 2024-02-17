import random

def kalaGenerator():
    maxNums = 32
    generated_str = ''
    
    for i in range(maxNums):
        randomNtoChar = chr(random.randint(33, 126))  # Adjusted range to exclude DEL (ASCII 127)
        
        while randomNtoChar in [' ', '\\', '\n', '\x7F']:  # Ensure DEL is excluded
            randomNtoChar = chr(random.randint(33, 126))  

        generated_str += randomNtoChar

    return generated_str

def multiRandStrGen(fileN, rowsToSave) :

    rowsToSave = abs(rowsToSave)

    with open(fileN, "w") as file:
    # Code to work with the file goes here
    # File is automatically closed at the end of the block
        currentRow = 0
        while(rowsToSave > currentRow ) :

            impo = generator.kalaGenerator()
            file.write(f'{impo}\n')
            currentRow+=1

multiRandStrGen('randStrs.txt', 30000)
