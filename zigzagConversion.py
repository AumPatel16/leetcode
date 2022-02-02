class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #get the number of rows 
        rows = ["" for i in range(numRows)]
        direction = 1 #-1 means downwards and -1 will mean upwards
        rowNum = 0 #this is the row in which the lettes are being inserted
        for i in s:
            rows[rowNum] += i
            if(rowNum == numRows-1):
                direction = -1
            elif(rowNum == 0):
                direction = 1
            rowNum += direction    
        result = ""
        for i in rows:
            result += i
        return result

a  = Solution()
print(a.convert("PAYPALISHIRING",4))
