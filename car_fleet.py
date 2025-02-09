from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = 0
        prev_time = 0
        indexed_position = list(enumerate(position))
        indexed_position.sort(key= lambda x : x[1], reverse= True)
        for index, p in indexed_position:
            time = (target - p) / speed[index]
            if prev_time < time:
                ans += 1
                prev_time = time
        return ans

if __name__ == "__main__":
    solution = Solution()
    result = solution.carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3])
    print(result)
            
