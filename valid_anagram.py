class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = [0] * 26
        for i in s:
            counter[ord(i) - ord('a')] += counter[ord(i) - ord('a')] + 1
        for i in t:
            counter[ord(i) - ord('a')] += counter[ord(i) - ord('a')] - 1
        return all(i == 0 for i in counter)