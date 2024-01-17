#without eval

def likeGregorySeries(times) :
    
    cnt = 1
    num = 3
    totalFormula = 1/1
    
    while cnt < times :
        
        if(cnt % 2 == 0) :
           #sign = '+'
           totalFormula = totalFormula + 1 / num
        else :
           #sign = '-'
           totalFormula = totalFormula - 1 / num
           
        
        cnt+=1
        num+=2
    
    totalFormula = 4 * totalFormula 
    return totalFormula
  
print( likeGregorySeries(1000) )
