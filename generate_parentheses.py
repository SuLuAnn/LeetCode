from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = set()
        left_count = n
        right_count = n
        self.putParenthesis(left_count, right_count, '', result)
        return list(result)
    
    def putParenthesis(self, left_count, right_count, parenthesis, result):
        if left_count == 0 and right_count == 0:
            result.add(parenthesis)
            return
        if left_count > 0:
            self.putParenthesis(left_count - 1, right_count, parenthesis + '(', result)
        if left_count < right_count:
            self.putParenthesis(left_count, right_count - 1, parenthesis + ')', result)


if __name__ == "__main__":
    solution = Solution()
    result = solution.generateParenthesis(4)
    print(result)