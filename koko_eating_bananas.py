import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_num, max_num = 1, max(piles)
        res = 1
        while min_num <= max_num:
            mid = (max_num + min_num) // 2
            accu_h = 0
            for pile in piles:
                accu_h += math.ceil(pile / mid)
            if accu_h > h:
                min_num = mid + 1
            else:
                res = mid
                max_num = mid - 1

        return res
    
if __name__ == "__main__":
    solution = Solution()
    result = solution.minEatingSpeed([312884470], 312884469)
    print(result)

