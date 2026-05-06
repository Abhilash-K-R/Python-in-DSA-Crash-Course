# Given an array of integers and a number d, find the length of the longest subsequence such that the difference between adjacent elements in the subsequence is d.
# leetcode 1218. Longest Arithmetic Subsequence of Given Difference

def mx_len_ss (arr,difference):
        max_l =1
        dp = {}
        for i in arr :
            if i-difference in dp:
                dp[i] = dp[i-difference]+1
            else:
                dp[i] = 1
            max_l = max(max_l,dp[i])
        return max_l

arr = [1,2,3,4,5,9,6,7,8]
difference = 2
print(mx_len_ss(arr,difference))