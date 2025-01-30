from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1
        data = list(sorted(dic.items(), key = lambda x : x[1], reverse = True))
        result =[x[0] for x in data]
        return result[0: k]

if __name__ == "__main__":
    solution = Solution()
    result = solution.topKFrequent([-1,-1], 1)
    print(result)
    result = solution.topKFrequent([1,1,1,2,2,3], 2)
    print(result)