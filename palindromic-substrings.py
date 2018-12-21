#!/usr/bin/env python3



class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        sLen = len(s)
        dp = [[0 for i in range(sLen)] for j in range(sLen)]
        
        totalCount = 0

        
        for i in range(0, sLen):
        	dp[i][i] = 1
        	totalCount += 1

        #print(dp)

        for substrSize in range(2, sLen + 1):
        	#print("substr: " + str(substrSize))
        	for i in range(0, sLen - substrSize + 1):
        		if substrSize == 2:
        			if s[i] == s[i+ substrSize - 1]:
        				dp[i][i + substrSize - 1] = 1
        				totalCount += 1
        		else:
        			if dp[i+1][i + substrSize - 1- 1] == 0:
        				dp[i][i + substrSize - 1] = 0
        			else:
        				if (s[i] == s[i + substrSize - 1]):
        					dp[i][i + substrSize - 1] = 1
        					totalCount += 1
        				else:
        					dp[i][i + substrSize - 1] = 0


        	#print(substrSize)

        #print(dp)


        #print(dp)
        return totalCount
        #print("totalCount: " + str(totalCount))



s = Solution()
print(s.countSubstrings("bbccaaca"))

#print(s.countSubstrings("bbccaaca"))
