#!/usr/bin/env python3

import re


class Solution:
    def __init__(self):
        self._end = '*'
        self.trie =dict()


    def make_trie(self, words):
    # creates our root dict() 

        for word in words:
            # create a temporary dict based off our root
            # dict object
            temp_dict = self.trie
        
            for letter in word:
                # update our temporary dict and add our current
                # letter and a sub-dictionary
                temp_dict = temp_dict.setdefault(letter, {})
                #print(temp_dict)
            # If our word is finished, add {'*': '*'}  
            # this tells us our word is finished
            temp_dict[self._end] = self._end
        
        #return trie

        #print(self.trie)


    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        sLen = len(s)
        dp = [0 for i in range(sLen+1)]
        dp[0] = 1
        #print(dp)

        self.make_trie(wordDict)

        
        # iterate over dp array
        for i in range(0, sLen+1):
            if dp[i] == 1:
                j = i
                #print("s[i:] " + str(s[i:]))

                sub_trie = self.trie
                
                for letter in s[i:]:
                    #print("letter: " + str(letter))
                    if letter in sub_trie:
                        #print("Y")
                        sub_trie = sub_trie[letter]
                        if self._end in sub_trie:
                            dp[j + 1] = 1
                            
                    else:
                        break

                    j += 1



        #print(dp)

        if dp[sLen] == 1:
            return True
        else:
            return False     



s = Solution()
#print(s.wordBreak("leetcode", ["leet","code"]))
#print(s.wordBreak("applepenapple", ["apple", "pen"]))


#print(s.wordBreak("a", [""]))

print(s.wordBreak("aaaaaaa", ["aaaa","aa"]))

#   "aaaaaaa"
#  ["aaaa","aa"]

#print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
#print(s.wordBreak("catsandog", []))