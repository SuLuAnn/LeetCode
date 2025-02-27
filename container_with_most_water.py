from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        res = 0
        while left < right:
            if height[left] <= height[right]:
                tmp_height = height[left]
                res = max(res, tmp_height * (right - left))
                left += 1
            else:
                tmp_height = height[right]
                res = max(res, tmp_height * (right - left))
                right -= 1
        return res

if __name__ == "__main__":
    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))