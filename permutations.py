#!/usr/bin/env python3

class Solution:

    def __init__(self):
        self.permutations = []

        
    def func2(self, availableNumList, permuteString):
        if not availableNumList:
            self.permutations.append(permuteString)
            return

        
        for i in range(len(availableNumList)):
            newAvailableNumList = availableNumList[:]
            del newAvailableNumList[i]
            
            newPermuteString = permuteString[:]
            newPermuteString.append(availableNumList[i])
            
            self.func2(newAvailableNumList, newPermuteString)
            
            
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.func2(nums, [])

        return(self.permutations)





s = Solution()
print(s.permute([1,2,3]))



        
