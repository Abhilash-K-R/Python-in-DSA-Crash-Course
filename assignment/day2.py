'''Trapping Rain Water:
Given an array height[] of size n consisting of non-negative integers, 
where each element represents the height of a bar and the width of each bar is 1,
Find the total amount of water that can be trapped between the bars after it rains.'''

# leetcode 42. Trapping Rain Water

def trap(height):
        left = 0
        right = len(height)-1
        leftmax = rightmax = water = 0
        
        while left <= right :
            if height[left] < height[right] :
                if height[left] >= leftmax:
                    leftmax = height[left]
                else :
                    water += leftmax - height[left]
                left +=1

            else :
                if height[right] >= rightmax :
                    rightmax = height[right]
                else :
                    water += rightmax - height[right]
                right -=1
        return water
    
print(trap([4,2,0,3,2,5]))