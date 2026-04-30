# s = [7,5,2,1]

def s5(arr):
    length=len(arr)
    
    for i in range(length):
        l=i
        res = 1
        for j in range(0,length):
            if j!=l:
                res*=arr[j]
        arr[i]=res
    return arr

print(s5([7,5,2,1]))