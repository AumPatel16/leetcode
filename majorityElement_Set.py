class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        for i in (set(nums)):
            cnt = nums.count(i)
            if cnt > n/2:
                return i

a = Solution()
print(a.majorityElement([1,2,3,4,1,1,1,1]))