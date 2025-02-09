from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        for index, height in enumerate(heights):
            start_index = index
            while stack:
                prev_height, prev_index = stack[-1]
                if prev_height > height:
                    ans = max((index - prev_index) * prev_height, ans)
                    stack.pop()
                    start_index = prev_index
                else:
                    break
            stack.append((height, start_index))
        hight_len = len(heights)
        for prev_height, prev_index in stack:
            ans = max((hight_len - prev_index) * prev_height, ans)

        return ans
    
if __name__ == "__main__":
    solution = Solution()
    result = solution.largestRectangleArea(heights = [2,1,2])
    print(result)
