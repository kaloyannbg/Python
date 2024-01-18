name = 'Boriss'
name2 = 'Popoliss'

letStr = ''

for let1 in name :
    
    if let1 in name2 and let1 not in letStr:
        letStr+=let1 

print(letStr, len(letStr), ' - Unique common letters in first and second str')
        
