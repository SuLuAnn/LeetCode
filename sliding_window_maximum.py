from typing import List
import heapq


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        priority_queue = []
        for i in range(0, k - 1):
            heapq.heappush(priority_queue, (-nums[i], i))
        for i in range(k - 1, len(nums)):
            left = i - k + 1
            heapq.heappush(priority_queue, (-nums[i], i))
            while True:
                max_value, max_index = priority_queue[0]
                if max_index >= left:
                    ans.append(-max_value)
                    break
                heapq.heappop(priority_queue)
        return ans
    
if __name__ == "__main__":
    solution = Solution()
    result = solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
    print(result)