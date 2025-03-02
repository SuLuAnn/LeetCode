from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        res, r, l = 0, 0, len(height) - 1
        tmp_r, tmp_l = r + 1, l - 1
        while tmp_r <= tmp_l:
            if height[r] < height[l]:
                if height[r] <= height[tmp_r]:
                    r = tmp_r
                else:
                    res += height[r] - height[tmp_r]
                tmp_r += 1
            else:
                if height[l] <= height[tmp_l]:
                    l = tmp_l
                else:
                    res += height[l] - height[tmp_l]
                tmp_l -= 1
        return res

if __name__ == "__main__":
    solution = Solution()
    result = solution.trap([4,2,0,3,2,5])
    print(result)


