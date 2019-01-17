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

        def myFunc(e):
            return e[0] + e[1]


        kPairs = []
        pairSumHeap = []

        # maxPairSum = -9999999999999999999999
            
        for val1 in nums1[:k]:
            # print("val1: " + str(val1))
            for val2 in nums2[:k]:
                # print("nums2[i2]: " + str(nums2[i2]))

                if len(kPairs) < k:
                    # print("IF")
                    kPairs.append([val1, val2])
                    heapq.heappush(pairSumHeap, -1 * (val1 + val2))


                elif val1 + val2 < (-1 * pairSumHeap[0]):
                    # print("ELIF")
                    heapq.heappop(pairSumHeap)
                    heapq.heappush(pairSumHeap, -1 * (val1 + val2))
                    kPairs.append([val1, val2])

        kPairs.sort(key=myFunc)

        return(kPairs[:k])




s = Solution()
print(s.kSmallestPairs([1,2,3], [10,20,30], 3))
