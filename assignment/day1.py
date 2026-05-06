# This function takes an array as input and calculates the sum of elements at odd and even indices. It then returns the absolute difference between the two sums.
# leetcode 2544. Alternating Digit Sum

def abhi(arr):
    odd_sum = 0
    even_sum = 0

    for i in range(len(arr)):
        if i % 2 == 0:
            even_sum += arr[i]
        else:
            odd_sum += arr[i]

    if even_sum > odd_sum:
        return even_sum - odd_sum
    else:
        return odd_sum - even_sum

print(abhi([4,6,1,3,8]))