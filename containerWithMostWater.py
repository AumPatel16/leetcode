import math

class Solution:
    def maxArea(self, height: list[int]) -> int:
        p1 = 0
        p2 = 1
        maxArea = 0
        sumMax = 0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                
                if((min(height[i],height[j])) + ((j-i)) >= (sumMax) and (min(height[i],height[j])) != 0):
                    if(min(height[i],height[j]) * (j-i) > maxArea):
                        #print(min(height[i],height[j]),(j-i),sumMax)
                        maxArea = min(height[i],height[j]) * (j-i)
                        #print(maxArea)
                        sumMax = min(height[i],height[j]) + (j-i)
                    

        return maxArea



height = [1,2,4,3]
a = Solution()
print(a.maxArea(height))