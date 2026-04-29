#Rat count House

def rch(R,Units,Arr):
    req = R*Units
    
    House = len(Arr)
    
    if House < 1 :  #if 0 house return 0
        return -1
    hou=0
    for i in range(House):
        hou += Arr[i]
        
        if hou >= req :
            return i+1
        
    return 0
    
    

print(rch(4,2,[]))
print(rch(4,2,[2,3,1,4,5,6]))