def bss(arr):   #[3,1,4,8]
    l=len(arr)
    res = 0
    for i in range(l):  #0,1,2,3
        for j in range(i+1,l):  #1,2,3  2,3  3  x
            res = max(res , arr[j] - arr[i])
            #res = max(0, 1-3) = 0
            #res = max(0, 4-3) = 1
            #res = max(1, 8-3) = 5
            #res = max(5, 4-1) = 5
            #res = max(5, 8-1) = 7
            #res = max(7, 8-4) = 7
    return res


print(bss([78,34,56,12,38]))
print(bss([3,1,4,8]))
print(bss([9,8,7,6]))