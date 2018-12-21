#!/usr/bin/env python3

import re


class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        sLen = len(s)

        dp = [[0 for i in range(sLen)] for j in range(sLen)]

        if len(wordDict) == 0:
        	return False

        #print(dp)
        isMatched = False
        for word in wordDict:
        	#print(word)
        	#match = re.search(word, s)
        	matches = re.finditer(word, s)
        	#print(matches)
        	if matches:
        		for mt in matches:
        			#print("word: " + str(word))
        			#print(mt)
        			isMatched = True
        			dp[mt.start()][mt.end() - 1] = 1
        		#pass
        		#print(mt.start())
        		#if match:
        		#print(match)
        		#print(match.start())
        #print(dp)

        #print("===2===")
        for word in wordDict:
        	#print(word)
        	s2= s[::-1]
        	word2 = word[::-1]
        	#match = re.search(word2, s2)
        	matches = re.finditer(word2, s2)
        	#print(matches)
        	if matches:
        		for mt in matches:
        			#print(mt)
        			isMatched = True
        			m = mt.start()
        			n = mt.end()

        			m2 = sLen - n;
        			n2 = sLen - 1 - m; 
        			dp[m2][n2] = 1


        if isMatched == False:
        	return False


        #print(dp)

        # check if last column has any 1

        #for i in range(0, sLen):
        #	if dp[i][sLen - 1] == 1:

        dp2 = [0 for i in range(sLen)]

        dp2[sLen-1] = 1

        #print(dp2)
        finalAns = False
        for j in range(sLen - 1, -1, -1):
        	for i in range(0, sLen):
        		if dp2[j] == 1:
        			if dp[i][j] == 1:
        				if (i > 0):
        					dp2[i - 1] = 1;
        				else:
        					dp2[i] = 1;
        					finalAns = True
        	#print(dp2)


        #for i in range(sLen - 2, -1, -1):

        #if dp2[0] == 1:
        #	return True
        #else:
        #	return False
        return finalAns

        #print(dp2)


s = Solution()
#s.wordBreak("leetcode", ["leet","code"])
print(s.wordBreak("applepenapple", ["apple", "pen"]))


#print(s.wordBreak("a", ["b"]))

#print(s.wordBreak("aaaaaaa", ["aaaa","aa"]))

#   "aaaaaaa"
#  ["aaaa","aa"]

#print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
#print(s.wordBreak("catsandog", []))