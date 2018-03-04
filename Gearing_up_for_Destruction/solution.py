from fractions import Fraction

def answer(pegs):
    
	# your code here
	k=len(pegs)
    
	if(k==1 or (not pegs)):
        
		return[-1,-1]
    
	elif(k==2):
        
		rlast=(pegs[k-1]-pegs[0])
        
		rfirst=Fraction(2*float(rlast/3)).limit_denominator()
        
		return([rfirst.numerator,rfirst.denominator])

    
	elif(k>2):
        
		sign=-1
        
		value=0
        
        
		if(k%2 == 0):
            
			corner = (pegs[k-1]-pegs[0])
            
			for i in range(1,k-1):
                
				value = 2*(-1)*(sign)**(i)*pegs[i]+value
            
			value=value+corner
            
			rfirst=Fraction(2*(float(value)/3)).limit_denominator()
        
        
		else:
            
			corner= (-pegs[k-1]-pegs[0])
            
			for i in xrange(1,len(pegs)-1):
                
				value = 2*(-1)*((sign)**(i))*pegs[i]+value
            
			value=value+corner
            
			rfirst=Fraction(2*float(value)).limit_denominator()
     
        
    
	currRadius = rfirst
    
	for i in range(0,len(pegs)-2):
        
		distance = pegs[i+1]-pegs[i]
        
		nextRadius = distance-currRadius
        
	if (nextRadius < 1 or currRadius <1):
            
		return[-1,-1]
        
	else : 
            
		currRadius = nextRadius
    
	return [rfirst.numerator,rfirst.denominator]
        
            
