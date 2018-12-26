#!/usr/bin/env python3

class Solution:
    def __init__(self):
        self.permutations = []
    
    def func2(self, list1, list2):

        if not list1:
            self.permutations.append(list2)
            return

        newList1 = newList2 = []
        for val in list1:
            #print("for:")
            #print("newlist1: " + str(newList1))
            #print("newList2: " + str(newList2))
            
            newList1 = list1[:]
            newList1.remove(val)
            
            newList2 = list2[:]
            newList2.append(val)
            
            self.func2(newList1, newList2)

            # backtrack
            

            
            
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.func2(nums, [])

        return(self.permutations)





s = Solution()
print(s.permute([1,2,3]))



        
