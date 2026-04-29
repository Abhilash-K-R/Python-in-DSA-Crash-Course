# Rat count house:

def rch (r,u,arr):
    if len(arr) == 0 :
        return -1
    
    freq = r*u
    bag = 0
    
    for i in range(len(arr)): #range(6) => 0,1,2,3,4,5
        bag += arr[i] # 0+2 = 2, 2+3 = 5, 5+1 = 6, 6+4 = 10, 10+5 = 15, 15+6 = 21
        
        if bag >= freq : #21 >= 8
            return i+1 #return 6
    return 0

print(rch(4,2,[2,3,1,4,5,6]))
print(rch(8,3,[2,3,1,4,5,6]))
print(rch(8,3,[]))