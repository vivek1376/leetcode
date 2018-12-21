#!/usr/bin/env python3

# Optimize : space

class Solution:


    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        rowCount = len(A)
        colCount = len(A[0])

        #print(rowCount)
        #print(colCount)

        dp = [[0 for i in range(colCount)] for j in range(rowCount)]


        
        # dp initialize
        for i in range(0, colCount):
            dp[rowCount-1][i] = A[rowCount-1][i]

        for i in range (rowCount - 2, -1, -1):
            #print("i:" + str(i))
            for j in range(0, colCount):
                #print("j:" + str(j))
                # calc MIN if col 1st
                min = 100000000000
                val = []

                if (j > 0):
                    val.append(j-1)
                    val.append(j)
                elif (j==0):
                    val.append(j)

                if (j < colCount - 1):
                    val.append(j+1)

                #print("val:"+str(val))

                for v in val:
                    if ((A[i][j] + dp[i+1][v]) < min):
                        min = A[i][j] + dp[i+1][v]
                
                dp[i][j] = min

                #print ("min:"+str(min))

        min = 100000000000
        for i in range (0, rowCount):
            if (dp[0][i] < min):
                min = dp[0][i]


        #print("dp:")
        #print(dp)
        
        return min


s = Solution()
print(s.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))
#print(s.minFallingPathSum([[1,2,3,5],[4,5,6,2],[7,8,9,3]]))
