from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        records = deque()
        for i in range(0, k - 1):
            while records and nums[i] >= nums[records[-1]]:
                records.pop()
            records.append(i)
            
        for i in range(k - 1, len(nums)):
            while records and nums[i] >= nums[records[-1]]:
                records.pop()
            records.append(i)
            while records[0] <= i - k:
                records.popleft()
            
            ans.append(nums[records[0]])

        return ans
    
if __name__ == "__main__":
    solution = Solution()
    result = solution.maxSlidingWindow([1], 1)
    print(result)