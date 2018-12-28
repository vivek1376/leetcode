#!/usr/bin/env python3

# TODO : make iterative

class Solution:
    def __init__(self):
        self.parenStrList = []
        self.n = 0

    def func(self, funcNo, indent, parenStr, numOpen, numClose):
        #print("func: " + str(n_old))
        print(' ' * indent + "func" + str(funcNo) + ": " + str(parenStr))
        if len(parenStr) == self.n * 2:
            self.parenStrList.append(parenStr)
            return

        if numOpen < self.n:
            parenStr2 = parenStr[:]
            parenStr2 += '('
            self.func(1, indent+2, parenStr2, numOpen + 1, numClose)

        if numOpen > numClose:
            parenStr2 = parenStr[:]
            parenStr2 += ')'
            self.func(2, indent+2, parenStr2, numOpen, numClose + 1)


        return self.parenStrList
    
            
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #newParenList = []
        self.n = n
        return self.func(0, 0, "", 0, 0)
            
            
        
        

s = Solution()
print(s.generateParenthesis(3))
