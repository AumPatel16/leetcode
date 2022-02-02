'''

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        dataBase = {"1":"", "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        counter = [0 for i in range(len(digits))]
        for i in range(len(digits)):
            counter[i] = len(dataBase[digits[i]])
        lez
        print(counter)
        localStr = ""
        sol = []
        #print(dataBase["2"])
        #for i in digits:



        return 0


a = Solution()
digits = "23"
print(a.letterCombinations(digits))
        
        '''