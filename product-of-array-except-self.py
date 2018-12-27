#!/usr/bin/env python3


class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums2 = nums[::-1]

        temp_nums = temp_nums2 = 1
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1]
            nums2[i] *= nums2[i - 1]


        nums2 = nums2[::-1]
        
        for i in range(len(nums)):
            if i == 0:
                temp_nums = 1
            else:
                temp_nums = nums[i-1]

            if i == len(nums) - 1:
                temp_nums2 = 1
            else:
                temp_nums2 = nums2[i+1]
                
            nums2[i] = temp_nums * temp_nums2
            
        #print(nums)
        #print(nums2)

        return nums2

        
s = Solution()
print(s.productExceptSelf([1,2,3,4]))
