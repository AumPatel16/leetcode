class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        d1 = {}
        for x in nums:
            d1[x] = 0

        for y in nums:
            d1[y] += 1
        
        for z in nums:
            if(d1[z] > (len(nums)/2)):
                return z

a = Solution()
print(a.majorityElement([1,2,3,4,1,1,1,1]))