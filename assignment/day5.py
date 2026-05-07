# leetcode 446. Arithmetic Slices II - Subsequence

class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        n = len(nums)
        dp = [{} for _ in range(n)]
        res = 0
        
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                
                # get previous count
                count = dp[j].get(diff, 0)
                
                # add to result (only sequences of length >= 3)
                res += count
                
                # update dp
                dp[i][diff] = dp[i].get(diff, 0) + count + 1
        
        return res