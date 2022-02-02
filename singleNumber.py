class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for i in range (len(nums)):
            if(not(nums[i] in nums[0:i] or nums[i] in nums[i+1:])):
                return nums[i]
                #print(str(nums[i]) + " double exists")

a = Solution()
print(a.singleNumber([2,2,1]))