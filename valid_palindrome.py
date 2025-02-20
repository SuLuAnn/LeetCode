class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while(left < right):
            left_char = s[left]
            right_char = s[right]
            if not left_char.isalnum():
                left += 1
                continue
            if not right_char.isalnum():
                right -= 1
                continue
            if left_char >= 'A' and left_char <= 'Z':
                left_char = left_char.lower()
            if right_char >= 'A' and right_char <= 'Z':
                right_char = right_char.lower()
            if left_char != right_char:
                return False
            left += 1
            right -= 1
        return True

