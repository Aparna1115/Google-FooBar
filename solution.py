import math


def answer(area):
  
	list=[]
  
	diff=area
  
	while (diff!=0) : 
	  
		n=math.sqrt(area)
	  
		nFloor = math.floor(n)
	  
		diff = area - (nFloor*nFloor)
	  
		list.append(nFloor*nFloor)
	  
		area=diff
  
	return list