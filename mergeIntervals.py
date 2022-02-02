class Solution:

    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        '''
        the criteria for merge is end point a is greater
        than start point b but less than end point b
        '''
        if(len(intervals)==1):
            return intervals
        subs = sorted(intervals, key = lambda col: col[0])
        min = subs[0][0]
        subs = sorted(intervals, key = lambda col: col[1])
        max = subs[-1][1]
        #subs = sorted(intervals, key = lambda col: col[0])
        x = 0
        i = 0
        print(subs)
        while (x != max):
            x = subs[i+1][1]
            if(subs[i][1] >= subs[i+1][0] and subs[i][1] < subs[i+1][1] and subs[i][0] < subs[i+1][0]):
                subs[i+1][0] = subs[i][0]
                subs.pop(i)
            elif(subs[i][0] >= subs[i+1][0] and subs[i][1] <= subs[i+1][1]):
                subs.pop(i)
            else:
                i+=1
            x = subs[i][1]
        return subs
    
            

intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
a = Solution()
print(a.merge(intervals))