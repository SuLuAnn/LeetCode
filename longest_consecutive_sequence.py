from collections import defaultdict
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        records = {}
        max_count = 0
        for i in range(len(nums)):
            if records.get(nums[i]) is None:
                if records.get(nums[i]-1) is None and records.get(nums[i]+1) is None:
                    records[nums[i]] = Record(nums[i], nums[i], 1)
                elif records.get(nums[i]-1) is not None and records.get(nums[i]+1) is None:
                    records[nums[i]] = Record(records[nums[i]-1].start, nums[i], records[nums[i]-1].count + 1)
                    records[records[nums[i]-1].start] = records[nums[i]]
                elif records.get(nums[i]-1) is None and records.get(nums[i]+1) is not None:
                    records[nums[i]] = Record(nums[i], records[nums[i]+1].end, records[nums[i]+1].count + 1)
                    records[records[nums[i]+1].end] = records[nums[i]]
                else:
                    records[nums[i]] = Record(records[nums[i]-1].start, records[nums[i]+1].end, records[nums[i]-1].count + records[nums[i]+1].count + 1)
                    records[records[nums[i]-1].start] = records[nums[i]]
                    records[records[nums[i]+1].end] = records[nums[i]]
                max_count = max(max_count, records[nums[i]].count)
            else:
                continue
        return max_count

class Record:
    def __init__(self, start, end, count):
        self.start = start
        self.end = end
        self.count = count
    
    def reset(self, start, end, count):
        self.start = start
        self.end = end
        self.count = count

if __name__ == "__main__":
    print(Solution().longestConsecutive([9, 1, 2, 5, 3, 4, 7, 0, 10]))

