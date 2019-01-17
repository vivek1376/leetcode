#!/usr/bin/env python3

# AC not fast

import heapq

class Solution:

    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """

        l2 = len(nums2)
        
        index2 = [0 for i in range(len(nums1))]
        kPairs = []

        for i1 in range(k):
            minVal = 999999999999999
            minIndex = -1
            
            if k > len(nums1):
                l1 = len(nums1)
            else:
                l1 = k
                
            for i in range(0, l1):
                # print("i: " + str(i) + " index2[i]: " + str(index2[i]))
                if index2[i] < l2 and nums1[i] + nums2[index2[i]] < minVal:
                    minVal = nums1[i] + nums2[index2[i]]
                    minIndex = i

            if not minIndex == -1:
                kPairs.append([nums1[minIndex], nums2[index2[minIndex]]])
                index2[minIndex] += 1

            # print("kPairs: " + str(kPairs))
            
        return(kPairs)



s = Solution()
#print(s.kSmallestPairs([1,2,3], [10,20,30], 3))
print(s.kSmallestPairs([1,2,4,5,6],[3,5,7,9], 20))
