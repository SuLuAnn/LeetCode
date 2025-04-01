import sys
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = [-sys.maxsize - 1] + nums1 + [sys.maxsize]
        nums2 = [-sys.maxsize - 1] + nums2 + [sys.maxsize]
        left, right = 0, len(nums1) - 1
        target_len = (len(nums1) + len(nums2)) // 2
        is_even = (len(nums1) + len(nums2)) % 2 == 0
        while True:
            mid = (left + right) // 2
            mid2 = target_len - (mid + 1) - 1
            if mid >= len(nums1) - 1 or mid2 < 0 or (mid2 < len(nums2) - 1 and nums1[mid] > nums2[mid2 + 1]):
                right = mid - 1
            elif mid < 0 or mid2 >= len(nums2) - 1 or (mid < len(nums1) - 1 and nums2[mid2] > nums1[mid + 1]):
                left = mid + 1
            else:
                if is_even:
                    return (max(nums1[mid] , nums2[mid2]) + min(nums1[mid + 1] , nums2[mid2 + 1])) / 2
                return min(nums1[mid + 1] , nums2[mid2 + 1])
 
if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([4, 5, 6, 8, 9], []))