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

        if numRows > 1:
        	totalCols = math.ceil((sLen / (2*(numRows-1))) * (numRows-1))
        else:
        	totalCols = sLen

        arr = [[0 for j in range(totalCols)] for i in range(numRows)]

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

        		arr[i][j] = s[si]
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
        		arr[i][j] = s[si]
        		si += 1

        	i = 0
        	j += 1

        	#print(arr)

        #print(arr)
        st =""
        for m in range(0, numRows):
        	for n in range(0, totalCols):
        		if arr[m][n] != 0:
        			st = st + arr[m][n]

        return st




s = Solution()
print(s.convert("PAYPALISHIRING", 3))