# s = [7,5,2,1]
# leetcode 238. Product of Array Except Self

def s5(arr):
    length=len(arr)
    res = []
    for i in range(length):
        res = 1
        for j in range(0,length):
            if i !=j:
                res*=arr[j]
        res.append(res)
    return arr

print(s5([7,5,2,1]))