class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #first subtract i from targer, and see if it exists in list.
        sub = 0
        for x in nums:
            sub = target-x
            if (sub in nums[nums.index(x)+1:]):
                if (nums.index(sub,nums.index(x)+1,len(nums)) != nums.index(x)):
                    return [nums.index(x), nums.index(sub,nums.index(x)+1,len(nums))]
            else:
                print("not there")
nums = [3,2,4]
a = Solution()
print (a.twoSum(nums, 6))