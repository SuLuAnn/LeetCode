from collections import defaultdict
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 數字 -> 長度
        records = defaultdict(int)
        max_count = 0
        for num in nums:
            if not records[num]:
                records[num] = records[num-1] + records[num+1] + 1
                records[num - records[num-1]] = records[num]
                # num = 5, num-1 = 4, records[num-1] = 2, records[num-1] 的開頭在 3, so 5-2 = 3
                records[num + records[num+1]] = records[num]
                max_count = max(max_count, records[num])
            else:
                continue
        return max_count

if __name__ == "__main__":
    print(Solution().longestConsecutive([9, 1, 2, 5, 3, 4, 7, 0, 10]))

