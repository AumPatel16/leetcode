#from ast import get_source_segment
import unittest

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        gsum,lsum = nums[0], nums[0]
        for i in range(1,len(nums)):
            lsum = max(nums[i],lsum+nums[i])
            if(lsum > gsum):
                gsum = lsum
        return gsum

class test(unittest.TestCase):
    def test_maxSubArray(self):
        obj = Solution()
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        result = obj.maxSubArray(nums)
        self.assertEqual(result,6)

    def test_maxSubArrayZeros(self):
        obj = Solution()
        nums = [0,0,0,0,0,0,0]
        result = obj.maxSubArray(nums)
        self.assertEqual(result,0)

    def test_maxSubArrayOne(self):
        obj = Solution()
        nums = [1]
        result = obj.maxSubArray(nums)
        self.assertEqual(result,1)

if __name__ == '__main__':
    unittest.main()

