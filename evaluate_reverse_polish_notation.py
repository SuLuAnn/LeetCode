from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+' : lambda left, right : left + right, '-' : lambda left, right : left - right, '*' : lambda left, right : left * right, '/' : lambda left, right : int(left / right)}
        for token in tokens:
            if token in operators:
                right = stack.pop()
                left = stack.pop()
                stack.append(operators[token](left, right))
            else:
                stack.append(int(token))
        return stack.pop()
    
if __name__ == "__main__":
    solution = Solution()
    result = solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
    print(result)

