#!/usr/bin/env python3

import math

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        # calc size of array

        sLen = len(s)


        arr2 = ['' for i in range(numRows)]

        #print(arr)

        i = j = si = 0

        while si < sLen:
        	# DOWN
        	#print("#########")
        	#print("")
        	#print("")
        	for i in range(0, numRows):
        		if si >= sLen:
        			break

        		arr2[i] += s[si]

        		si += 1

        	i1 = i # reset?
        	#print(arr)
        	#print("==============")
        	# UP
        	#print(j)
        	for i in range(i1 - 1, 0, -1):
        		#print(i)
        		if si >= sLen:
        			break

        		j += 1
        		arr2[i] += s[si]

        		si += 1

        	i = 0
        	j += 1

        	#print(arr)

        #print(arr)

        st2 = ""

        for i in range(numRows):
        	st2 += arr2[i]
        
        return st2




s = Solution()
print(s.convert("PAYPALISHIRING", 3))