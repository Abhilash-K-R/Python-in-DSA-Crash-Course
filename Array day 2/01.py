# maximum water trap between lines
#important


def maxwater(arr):
    left = 0 
    right = len(arr) - 1
    maxwater = 0
    while left<right :
        temp = min(arr[left],arr[right]) * (right-left)
        maxwater = max(maxwater,temp)
        if arr[left] < arr[right] :
            left +=1
        else :
            right -=1
    return maxwater

print(maxwater([6,1,2,3,5]))