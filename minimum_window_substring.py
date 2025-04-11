from collections import defaultdict, deque

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_record = defaultdict(int)
        t_record = defaultdict(int)
        position_record = deque()
        ans = s
        for c in t:
            t_record[c] += 1

        total = 0

        for i, c in enumerate(s):
            if not t_record[c]:
                continue
            if s_record[c] < t_record[c]:
                total += 1
            s_record[c] += 1
            position_record.append(i)
            while s_record[s[position_record[0]]] > t_record[s[position_record[0]]]:
                s_record[s[position_record.popleft()]] -= 1
            if total == len(t) and len(ans) > i - position_record[0] + 1:
                ans = s[position_record[0]: i + 1]
        return ans if total == len(t) else ""

if __name__ == "__main__":
    solution = Solution()
    result = solution.minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd")
    print(result)

