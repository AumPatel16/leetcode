class Solution:
    def sortColors(self, nums: list[int]) -> None:
        i = 0
        while(i < len(nums)-1):
            if(nums[i+1] < nums[i]):
                temp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = temp
                counter = 0
                i = 0
            else:
                i +=1
        print (nums)

a = Solution()
print(a.sortColors([2,0,2,1,1,0]))
