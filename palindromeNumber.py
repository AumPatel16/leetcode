class Solution:
    def isPalindrome(self, x: int) -> bool:
        strx = str(x)
        if(len(strx) < 2):
            return True
        for i in range (len(strx)//2):
            if(strx[i] != strx[len(strx)-(i+1)]):
                return False
        return True

x = 1000021
a = Solution()
print(a.isPalindrome(x))