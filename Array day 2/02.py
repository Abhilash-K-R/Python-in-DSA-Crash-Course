# max subarray sum 
#important

def max_arr(arr):
    tmax = fmax =arr[0]
    for i in range(1,len(arr)):
        tmax = max(arr[i],tmax+arr[i])
        fmax = max(fmax,tmax)
    return fmax

# print(max_arr([-2,1,-3,4,-1,2,1,-5,4]))
print(max_arr([4,-2,-3,7,-3]))
