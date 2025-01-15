from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for str in strs:
            temp = ''.join(sorted(str))
            group = dic.get(temp)
            if group is None:
                group = [str]
                dic[temp] = group
            else:
                group.append(str)

        return list(dic.values())

if __name__ == "__main__":
    solution = Solution()
    result = solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    print(result)