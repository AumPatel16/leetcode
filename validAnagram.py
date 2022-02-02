import unittest


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        dic = {}
        for i in s:
            dic[i] = 0
        dic2 = dic.copy()
        for i in s:
            dic[i] +=1
        for i in t:
            if(i in s):
                dic2[i] += 1
            else:
                return False
        print(dic, dic2)
        if(dic == dic2):
            return True
        else:
            return False

class testVA(unittest.TestCase):
    obj = Solution()

    def test_case1(self):
        result = testVA.obj.isAnagram("rat", "car")
        self.assertFalse(result)

    def test_case2(self):
        result = testVA.obj.isAnagram("anagram", "nagrama")
        self.assertTrue(result)

    def test_case3(self):
        result = testVA.obj.isAnagram("aacc", "ccac")
        self.assertFalse(result)


unittest.main()

