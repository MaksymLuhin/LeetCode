
def maxArea(height) -> int:
    #list -> basically array
    #index -> x coordinate
    #value of corresponding index -> y value
    #volume -> area
    #rectangle area formula = length * width

    #most obvious solution is using 2 for loops
    #takes too much time
    #-----------------------------------------------------------------------------------
    # maxArea = 0
    # for i in range(0, len(height)):
    #     for b in range(1, len(height)):
    #         #get the lowest value for y since container cant have water where one side if higher
    #         minHeight = min(height[i], height[b])
    #         newArea = minHeight * (b-i)
    #         if(newArea > maxArea):
    #             maxArea = newArea
    #         else:
    #             continue
    
    # return maxArea

    #using hint from leetcode, by setting 2 pointers
    left = 0
    right = (len(height)-1)
    maxArea = 0


    while(left < right):
        minHeight = min(height[left], height[right])
        newArea = minHeight * (right-left)

        if(newArea > maxArea):
            maxArea = newArea
        
        if(height[left] > height[right]):
            right -= 1
        else:
            left += 1

    return maxArea

