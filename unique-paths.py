#!/usr/bin/env python3

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        dp = [[0 for i in range(m)] for j in range(n)]
        
        #print(dp)

        for i in range(0, m):
            dp[n-1][i] = 1
        
        #print(dp)
            
        for j in range(0, n):
            dp[j][m-1] = 1
                
        #print(dp)

        for j in range(n-2, -1, -1):
            for i in range(m-2, -1, -1):
                #print("j,i: " + str(j) + "," + str(i))

                dp[j][i] = dp[j][i+1] + dp[j+1][i]

        return dp[0][0]
    



s = Solution()
print(s.uniquePaths(3, 2))
        
