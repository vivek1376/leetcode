#!/usr/bin/env python3

class Solution():
	def lengthOfLIS(self, nums):
		def recursiveFunc(nums, i, currLen, currHighestNum):
			# print("func: i: " + str(i)+" currLen: " + str(currLen))
			if i==n:
				return currLen

			# len, currHighestNum = recursiveFunc(nums, i-1);

			len1=recursiveFunc(nums, i+1, currLen, currHighestNum)

			if nums[i] <= currHighestNum:
				return len1

			# l1= 1+currLen
			len2=recursiveFunc(nums, i+1, currLen+1, nums[i])
	
			return max(len1, len2)


		n=len(nums)
		return recursiveFunc(nums, 0, 0, -9999999999999999)



s = Solution()
#print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))
print(s.lengthOfLIS([2,2]))




