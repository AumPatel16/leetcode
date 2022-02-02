class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        prev = -101
        counter = 0
        k = 0
        for x in nums:
            if(x == prev):
                nums[counter]=101
                k+=1
            else:
                prev = x
            counter +=1
        nums.sort()
        print(nums)
        return (len(nums)-k)

nums = [1,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,5,5,5]
a = Solution()
p = a.removeDuplicates(nums)
print(nums)
print(p)
