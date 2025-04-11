from collections import defaultdict, deque

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_record = defaultdict(int)
        t_record = defaultdict(int)
        position_record = deque()
        for c in t:
            t_record[c] += 1

        total, need = 0, len(t)
        res, resLen = [-1, -1], float("infinity")

        for i, c in enumerate(s):
            if not t_record[c]:
                continue
            if s_record[c] < t_record[c]:
                total += 1
            s_record[c] += 1
            position_record.append(i)
            if total == need:
                while s_record[s[position_record[0]]] > t_record[s[position_record[0]]]:
                    s_record[s[position_record.popleft()]] -= 1
                if resLen > i - position_record[0] + 1:
                    res = [position_record[0], i]
                    resLen = i - position_record[0] + 1
        return s[res[0] : res[1] + 1] if total == need else ""

if __name__ == "__main__":
    solution = Solution()
    result = solution.minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd")
    print(result)

