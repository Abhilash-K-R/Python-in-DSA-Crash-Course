# maximum sub array

def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = total = nums[0]

        for i in range(1 ,len(nums)) :
            total = max(total + nums[i] , nums[i])
            res = max(res , total)
        return res
    
    