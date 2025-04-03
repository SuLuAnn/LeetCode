class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximun_length, left, right, str_length = 0, 0, 0, len(s)
        record = {}
        while right < str_length:
            if s[right] in record and left <= record[s[right]]:
                maximun_length = max(maximun_length, right - left)
                left = record[s[right]] + 1
            record[s[right]] = right
            right += 1
        maximun_length = max(maximun_length, right - left)
        return maximun_length

if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring('abcabcbb'))
        