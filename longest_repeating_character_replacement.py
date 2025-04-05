from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int)  -> int:
        left, max_char, longest_substring = 0, 0, 1
        record = defaultdict(int)
        for i, c in enumerate(s):
            record[c] += 1
            cur_length = i - left + 1
            max_char = max(max_char, record[c])
            if cur_length > max_char + k:
                record[s[left]] -= 1
                left += 1
            else:
                longest_substring = max(longest_substring, cur_length)
        return longest_substring
if __name__ == "__main__":
    print(Solution().characterReplacement('AABABBA', 1))
