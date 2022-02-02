import unittest
from unittest.main import main


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if(len(magazine) < len(ransomNote)):
            return False

        dict = {}
        for i in magazine:
            if(i in dict.keys()):
                dict[i] +=1
            else:
                dict[i] = 1
        print(dict)
        for j in ransomNote:
            if(j in dict.keys()):
                dict[j] -=1
            else:
                return False
        print(dict)
        for k in dict.values():
            if(k<0):
                return False
        return True

class testCC(unittest.TestCase):
    obj = Solution()

    def test_Case1(self):
        result = testCC.obj.canConstruct("a", "b")
        self.assertFalse(result)
    def test_Case2(self):
        result = testCC.obj.canConstruct("aa", "ab")
        self.assertFalse(result)
    def test_Case3(self):
        result = testCC.obj.canConstruct("aa", "aab")
        self.assertTrue(result)


unittest.main()