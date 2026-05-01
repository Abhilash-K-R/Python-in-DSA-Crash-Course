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
    
print(trap([5,4,1,2]))