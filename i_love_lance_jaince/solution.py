def answer(s):
  def reversel(strg):
    str1 = ""
    for k in strg:
      str1 = k + str1
    return (str1)

  inputlist = "abcdefghijklmnopqrstuvwxyz"
  ilist = list(inputlist)
  revrselist = reversel(inputlist) 
  rlist = list(revrselist)
  newlist=[]
  slist =list(s)

  for i in range(0,len(slist)):
  
    if(s[i].islower()):
      for j in range(0,len(ilist)):
    
        if(slist[i]== ilist[j]):
          newlist.append(rlist[j])
    else:
      newlist.append(slist[i])

  str1 = ''.join(newlist)
  return(str1)



