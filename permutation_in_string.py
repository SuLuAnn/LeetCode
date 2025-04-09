class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_record = [0] * 26
        cur_record = [0] * 26
        s1_len = len(s1)
        a_ascii = ord('a')
        for s in s1:
            index = ord(s) - a_ascii
            s1_record[index] += 1
        left = 0
        for i, s in enumerate(s2):
            if i - left == s1_len:
                return True
            index = ord(s) - a_ascii
            if not s1_record[index]:
                cur_record = [0] * 26
                left = i + 1
                continue
            elif s1_record[index] == cur_record[index]:
                while s2[left] != s:
                    left_index = ord(s2[left]) - a_ascii
                    cur_record[left_index] -= 1
                    left += 1
                left += 1
            else:
                cur_record[index] += 1
        return i - left + 1 == s1_len
    
if __name__ == "__main__":
    solution = Solution()
    result = solution.checkInclusion("ab", "eidbaooo")
    print(result)

            
                
