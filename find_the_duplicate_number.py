from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        records = [0] * len(nums)
        for num in nums:
            if records[num] == 1:
                return num
            records[num] = 1