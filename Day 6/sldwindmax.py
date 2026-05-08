# leetcode 239. Sliding Window Maximum
# Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

from collections import deque

def max_sliding (nums , k ) :
    dq = deque()
    res = []
    for i in range(len(nums)):
        if dq and dq[0] < i-k:
            dq.popleft()
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()    
        dq.append(i)
        if i >= k-1:
            res.append(nums[dq[0]])
    return res

print(max_sliding([1,3,-1,-3,5,3,6,7], 3))