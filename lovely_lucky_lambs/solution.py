
def stingy(total_lambs):
  lambshenchmen = []
  lambshenchmen.append(1)
  max = len(lambshenchmen) - 1
  henchmen = 1
  
  while(sum(lambshenchmen) <= total_lambs):
    if(henchmen == 1):
      lambshenchmen.append(1);
      max = len(lambshenchmen)-1
      henchmen = henchmen + 1
    else:
      lastguy = lambshenchmen[max] + lambshenchmen[max-1]
      lambshenchmen.append(lastguy)
      #if(sum(lambshenchmen) <= total_lambs):
      henchmen = henchmen + 1
      #break
      max = len(lambshenchmen) - 1
  return max


def generous(total_lambs):
 
    genhenchmen = 1
    prev = 0
    lastguy = 1
    total_lambs -= 1
    while(total_lambs > 0):
        if((total_lambs) < (2* lastguy)):
            if(total_lambs >=(lastguy + prev)): 
                genhenchmen = genhenchmen + 1
            break
        genhenchmen = genhenchmen + 1
        prev = lastguy
        lastguy = 2*(lastguy)
     
        total_lambs = total_lambs - lastguy
    return genhenchmen
def answer(total_lambs):
    return (stingy(total_lambs) - generous(total_lambs))



