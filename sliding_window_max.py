#!/usr/bin/env python3

#write  own code


import collections

class Solution:
    def maxSlidingWindow(self, nums, k):

        res = []

        if not k or not nums:
            return res

        if k >= len(nums):
            return [max(nums)]

        # Use a queue to store currently seen max values
        max_window = collections.deque()

        i = 0
        j = len(nums)

        while (i < j):

            # Process sliding window, i,e remove element from our
            # max queue if the last element of our queue is the
            # same one as the element left out as the sliding window
            # moved.
            if ((i - k) >= 0 and max_window[-1] == (i - k)):
                max_window.pop()

            # This is main optimization in this problem.

            # As we see new element, we prune our queue from
            # left by checking if this new value is greater than the
            # values in queue front, if so we remove those items.

            # The reason for doing this is, if the newly seen
            # element is greater than already seen older elements, then
            # we can be sure that older elements can never be a maximum
            # value in our sliding window, so removing them from the queue
            # will always ensure that our queue holds list of maximum values
            # in the window moved by i.
            while(max_window and nums[i] > nums[max_window[0]]):
                max_window.popleft()
            max_window.appendleft(i)

            # Since this loop starts with index 0, add the max value
            # to our res list only after we have moved i atleast window size.
            if (i >= k-1):
                res.append(nums[max_window[-1]])

            i += 1

        return res



s =Solution();

print(s.maxSlidingWindow([8,2,8,0,1,7,3,4], 3))
