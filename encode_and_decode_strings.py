from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f'{len(s)},{s}' for s in strs)

    def decode(self, s: str) -> List[str]:
        i = 0
        num_end = 0
        end = len(s)
        result = []
        while(num_end < end):
            if s[num_end] != ',':
                num_end += 1
                continue
            s_len = int(s[i: num_end])
            i = num_end + 1
            num_end = i + s_len
            result.append(s[i: num_end])
            i = num_end
        return result

if __name__ == "__main__":
    solution = Solution()
    result = solution.encode(["we","say",":","yes","!@#$%^&*()"])
    print(result)
    result = solution.decode(result)
    print(result)