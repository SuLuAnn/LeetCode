from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for t in enumerate(temperatures):
            while stack:
                if stack[-1][1] < t[1]:
                    index = stack.pop()[0]
                    ans[index] = t[0] - index
                else:
                    break
            stack.append(t)
        return ans

if __name__ == "__main__":
    solution = Solution()
    result = solution.dailyTemperatures([73,74,75,71,69,72,76,73])
    print(result)

                