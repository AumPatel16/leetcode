import unittest
'''
I use a dictonary here, but there are solutions which take advantage of a set
sets dont have duplicates so you can check a set for reference.
    Example:
return len(nums) > len(set(nums))
    OR for more efficiency:
record = set()
        for num in nums:
            if num in record:
                return True
            else:
                record.add(num)
        else:
            return False

'''

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if(len(nums)<=1):
            return False   
        database = {}
        for i in nums:
            database[i] = 1
        for i in nums:
            #print(database)
            database[i] += 1
            if(database[i] > 2):
                return True
        return False

class Test(unittest.TestCase):
    def test_containsDuplicate(self):
        nums = [1,2,3,3,4]
        sol = Solution()
        result = sol.containsDuplicate(nums)
        self.assertEqual(result,True)

if __name__ == '__main__':
    unittest.main()
