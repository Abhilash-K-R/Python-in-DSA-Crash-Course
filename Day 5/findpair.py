# find pair from 2 array to get the target sum
# leetcode 167. Two Sum II - Input array is sorted
'''
input: 
arr1 = [1,2,3,4,5]
arr2 = [6,7,8,9,10]
target = 10

output:
(1,9) , (2,8) , (3,7) , (4,6)

use one loop to find the pair'''

def find_pair(arr1, arr2, target):
    pairs = []
    for num in arr1: # 1 2 3 4 5
        complement = target - num # 10-1=9 10-2=8 10-3=7 10-4=6 10-5=5
        if complement in arr2: # if 9 in arr2 => True   if 8 in arr2 => True   if 7 in arr2 => True   if 6 in arr2 => True   if 5 in arr2 => False
            pairs.append((num, complement)) # pairs = [(1,9)] pairs = [(1,9),(2,8)] pairs = [(1,9),(2,8),(3,7)] pairs = [(1,9),(2,8),(3,7),(4,6)]
    pairs.sort(key=lambda x: x[0]) # sort the pairs based on the first element of the pair
    return pairs


arr1 = [1,2,3,4,5]
arr2 = [6,7,8,9,10]
target = 10
print(find_pair(arr1, arr2, target))