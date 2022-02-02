import unittest

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        if(n == 0):
            return
        if(m == 0):
            print(nums1)
            nums1[:] = nums2
            print("this is after" ,nums1)
            return

        i = 0 #for nums1
        j = 0 #for nums2
        k = m
        while(j < n and i < k):
            if(nums2[j]<nums1[i]):
                nums1.insert(i,nums2[j])
                j+=1
                k+=1
            else:
                i+=1

        while(j<n): 
            nums1.insert(i,nums2[j])
            j+=1
            i+=1

        while(len(nums1)>m+n):
            nums1.pop(m+n)
        """
        Do not return anything, modify nums1 in-place instead.
        """

class testmsa(unittest.TestCase):

    ob = Solution()

    def testCaseOne(self):
        nums1 = [1]
        nums2 = [0]
        m = 1
        n = 0
        testmsa.ob.merge(nums1,m,nums2,n)
        merged = [1]
        self.assertEqual(nums1, merged)

    def testCaseTwo(self):
        nums1 = [1,2,3,0,0,0]
        nums2 = [2,5,6]
        m = 3
        n = 3
        testmsa.ob.merge(nums1,m,nums2,n)
        merged = [1,2,2,3,5,6]
        self.assertEqual(nums1, merged)

    def testCaseThree(self):
        nums1 = [1,0]
        nums2 = [2]
        m = 1
        n = 1
        testmsa.ob.merge(nums1,m,nums2,n)
        merged = [1,2]
        self.assertEqual(nums1, merged)

if __name__ == '__main__':
    unittest.main()
    '''
    nums1 = [0]
    nums2 = [1,3,5,7,89]
    m = 0
    n = 1
    ob = Solution()
    ob.merge(nums1,m,nums2,n)
    print(nums1)'''