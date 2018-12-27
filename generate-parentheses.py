#!/usr/bin/env python3


class Solution:
    def __init__(self):
        self.ans = []
        self.n = 0

    def makeParenStr(self, l):
        str = ""
        for i in range(len(l)):
            if i % 2 == 0:
                str += ('(' * l[i])
            else:
                str += (')' * l[i])

        return str

    def func(self, valList, n_new):
        #print("func: " + str(n_old))
        sum = 0
        sum2 = 0
        #print(valList)
        if len(valList) % 2 == 0:
            odd = 0
            even = 0
            for i in range(len(valList)):
                if i % 2 == 0:
                    even += valList[i]
                    sum2 += valList[i]
                else:
                    odd += valList[i]
                    sum2 -= valList[i]

                if sum2 < 0:
                    return
                
                sum += valList[i]

                if sum == self.n and even == odd:
                    print(valList)
                    self.ans.append(self.makeParenStr(valList))
                    #print(self.makeParenStr(valList))
                    return

        for i in range(1, n_new + 1):
            newValList = valList[:]
            newValList.append(i)
            self.func(newValList, n_new - i)


        return self.ans
    
            
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #newParenList = []
        self.n = n*2
        return self.func([], n*2)
            
            
        
        

s = Solution()
print(s.generateParenthesis(3))
