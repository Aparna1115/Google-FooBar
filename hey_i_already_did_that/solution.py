def answer(n,b):
  listFinal=[]
  l=len(listFinal)
  listFinal.append(n)
  k = len(n)
  diff=0
  count=0
  while(count == 0):
  
    listAsc = ''.join(sorted(n))
    yVal=int(listAsc, b) 
    listDes = ''.join(sorted(n,reverse=True)) 
    xVal = int(listDes, b)
    zVal = toStr(xVal - yVal, b)
    zvalue = int(zVal, b)
    z = toStr(zvalue, b)

    if (len(z)< k): 
      z = z.zfill(k)
				
    n = z
    for z in listFinal:
      diff=len(listFinal) - j
      count=1
  			
  listFinal.append(z)
  return diff
	
def toStr(n,base):
  convertString = "0123456789ABCDEF"
  if n < base:
    return convertString[n]
  else:
    return toStr(n//base,base) + convertString[n%base]
