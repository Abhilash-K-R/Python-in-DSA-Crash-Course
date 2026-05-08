# leetcode 496. Next Greater Element I
# Given two arrays nums1 and nums2 where nums1’s elements are a subset of nums2, find all the next greater numbers for nums1's elements in the corresponding places of nums2.

def next_great (arr):
    n = len(arr)
    stk = []
    res = [-1] * n
    for i in range(n-1, -1, -1):
        while stk and stk[-1] <= arr[i]:
            stk.pop()
        if stk:
            res[i] = stk[-1]
        stk.append(arr[i])
    return res

print(next_great([3,1,6,7,1,8]))
print(next_great([1,3,4,2]))
