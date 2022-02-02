class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        #have three iterators that iterate to find all three pairs.
        #make a list of all sub lists and take out duplicates by making a set
        ansList = []
        for i in range (len(nums)):
            for j in range (i+1,len(nums)):
                for k in range (j+1,len(nums)):
                    if(nums[i]+nums[j]+nums[k] == 0):
                        if(sorted([nums[i],nums[j],nums[k]]) not in ansList):
                            ansList.append(sorted([nums[i],nums[j],nums[k]]))
        return ansList
a = Solution()
print(a.threeSum([-1,0,1,2,-1,-4]))