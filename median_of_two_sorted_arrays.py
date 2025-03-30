from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = []
        total = (len(nums1) + len(nums2))
        target = total // 2 + 1
        index1, index2 = 0, 0
        nums1_max_index = len(nums1) - 1
        nums2_max_index = len(nums2) - 1
        while index1 <= nums1_max_index and index2 <= nums2_max_index:
            if nums1[index1] <= nums2[index2]:
                num.append(nums1[index1])
                index1 += 1
            else:
                num.append(nums2[index2])
                index2 += 1
            if len(num) == target:
                ans = num[target - 1]
                if total % 2 == 0:
                    ans += num[target - 2]
                    ans /= 2
                return ans
        if index1 <= nums1_max_index:
            num += nums1[index1:]
        else:
            num += nums2[index2:]
        ans = num[target - 1]
        if total % 2 == 0:
            ans += num[target - 2]
            ans /= 2
        return ans
                
if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([], [1]))