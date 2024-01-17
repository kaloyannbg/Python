

def likeGregorySeries(times) :
    
    cnt = 1
    num = 1
    sign = ''
    
    formula = '4 * (  '
    
    while cnt <= times :
        
        if(cnt % 2 == 0) :
           sign = '+'
        else :
           sign = '-'
           
        if cnt == times :
            sign = ''
        formula+= '1/' + str(num) + ' ' + sign + ' '  #(1/1 − 1/3 + 1/5 − 1/7 + 1/9...)
        
        cnt+=1
        num+=2
    
        
    formula+=')'
    #print(formula)
    return eval(formula)
    
print( likeGregorySeries(1000) )
