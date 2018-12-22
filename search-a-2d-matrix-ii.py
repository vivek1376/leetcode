#!/usr/bin/env python3

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        rowCount = len(matrix)
        if rowCount:
        	colCount = len(matrix[0])
        else:
        	colCount = 0

        # select row
        for i in range(rowCount):
        	if colCount == 0:
        		continue
        		
        	if not (target >= matrix[i][0] and target <= matrix[i][colCount-1]):
        		continue

        	# binary search
        	m = 0
        	n = colCount - 1
        		
        	isFound = False
        	while (n >= 0 and n >= 0 and m <= n):
        		m1 = int((m + n) / 2)

        		if target == matrix[i][m1]:
        			isFound = True
        			break

        		elif target > matrix[i][m1]:
        			m = m1 + 1
        		else:
        			n = m1 - 1

        	if isFound:
        		return True

        return False

        
s = Solution()
print(s.searchMatrix(
	[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
29))
