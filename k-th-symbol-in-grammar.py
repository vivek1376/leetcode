#!/usr/bin/env python3

class Solution:
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """

        if K == 1:
            return 0

        if K % 2 == 0:
            k1 = K / 2
            el = self.kthGrammar(N, k1)
            if el == 0:
                return 1
            else:
                return 0
        else:
            k1 = (K + 1) / 2
            el = self.kthGrammar(N, k1)
            if el == 0:
                return 0
            else:
                return 1



s = Solution()
print(s.kthGrammar(4, 5))