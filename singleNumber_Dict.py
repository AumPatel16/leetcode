class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        d1 = {}
        for x in nums:
            d1[x] = 0
            print(d1)
        for y in nums:
            d1[y] += 1
            print(d1)

        for z in nums:
            if(d1[z]==1):
                return nums.index(z)
a = Solution()
print(a.singleNumber([1,1,2,3,3,4,4]))