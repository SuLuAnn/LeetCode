class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while(left < right):
            left_char = s[left]
            right_char = s[right]
            if left_char >= 'A' and left_char <= 'Z':
                left_char = left_char.lower()
            elif not (left_char >= 'a' and left_char <= 'z') and not (left_char >= '0' and left_char <= '9'):
                left += 1
                continue
            if right_char >= 'A' and right_char <= 'Z':
                right_char = right_char.lower()
            elif not (right_char >= 'a' and right_char <= 'z') and not (right_char >= '0' and right_char <= '9'):
                right -= 1
                continue
            if left_char != right_char:
                return False
            left += 1
            right -= 1
        return True

