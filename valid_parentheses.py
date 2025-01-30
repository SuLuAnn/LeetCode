from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        left_char = {')':'(', ']':'[', '}':'{'}
        for c in s:
            left_char_tmp = left_char.get(c)
            if left_char_tmp is not None:
                if not stack or left_char_tmp != stack.pop():
                    return False
            else:
                stack.append(c)
        return not any(stack)

if __name__ == "__main__":
    print(Solution().isValid('()'))
