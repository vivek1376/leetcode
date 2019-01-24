#!/usr/bin/env python3

class Solution():
    def lengthOfLIS(self, nums):
        def recursiveFunc(rDepth, funcNo, nums, i, maxLimit):
            # print('   ' * rDepth + "(" + str(funcNo) + ") > Fn{{ i: " + str(i) + " maxLimit:" + str(maxLimit))
            # print("func: i: " + str(i)+" currLen: " + str(currLen))

            if i == -1:
                # print('   ' * rDepth + '> 0')
                return 0

            # len, currHighestNum = recursiveFunc(nums, i-1);

            # if currHighestNum >= minVal:
            if not dp[i][maxLimit-minVal] == -1:
                # print('   '*rDepth+str(dp))
                # print('   '*rDepth+'>> '+str(dp[i][maxLimit]))

                return dp[i][maxLimit-minVal]

            # print('   '*rDepth+"func0"+" i: "+str(i+1)+" maxLimit:"+str(maxVal+1))
            len1 = recursiveFunc(rDepth + 1, 1, nums, i - 1, maxLimit )

            # print("i+1:" + str(i+1)+" currHighestNum-minVal: "+str(currHighestNum-minVal))
            # print(i-1, maxLimit)
    
            if i-1>=0:
                dp[i-1][maxLimit-minVal]=len1
                # print(i-1, maxLimit, str(dp))

            # if maxLimit <=
            if nums[i] >= maxLimit:
                # print(dp)
                # print('   ' * rDepth + '>> ' + str(len1))

                return len1

            # l1= 1+currLen
            # print('   '*rDepth+"func1"+" i: "+str(i+1)+" maxLimit:"+str(maxLimit))
            len2 = recursiveFunc(rDepth + 1, 2, nums, i - 1, nums[i])
    
            if i-1>=0:
                dp[i-1][nums[i]-minVal]=len2
                # print(str(dp))

            # print('   ' * rDepth + '>>> ' + str(max(len1, len2+1)) + " [" + str(nums[i]) + "]")
            # dp[i][currHighestNum]=max(len1, len2)
            return max(len1, len2+1)

        ## MAIN ##
        n = len(nums)
        if n==0:
            return 0

        minVal = min(nums)
        maxVal = max(nums)

        # minVal -= 1

        if minVal > 0:
            minVal=0

        dp = [[-1 for j in range(maxVal-minVal+2)] for i in range(n+1)]
        # dp = [[-1 for j in range(maxVal+2)] for i in range(n+1)]
        # print(dp)

        ans = recursiveFunc(0, 0, nums, n - 1, maxVal + 1)
        # print(dp)
        return ans


s = Solution()
# print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))
print(s.lengthOfLIS([-1,-2,-3,-4,-5,-6]))
# print(s.lengthOfLIS([2,1,3,1,4]))
# print(s.lengthOfLIS([3,2,1,2]))
# print(s.lengthOfLIS([3, 2, 1]))
